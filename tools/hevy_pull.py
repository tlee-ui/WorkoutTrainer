#!/usr/bin/env python3
"""Pull the full workout history from the Hevy API and write it to data/.

Usage:
    HEVY_API_KEY=... python3 tools/hevy_pull.py [--inspect] [--since 2024-01-01]

Reads the key from the HEVY_API_KEY environment variable, or relies on a network-secret
proxy that adds it to requests for api.hevyapp.com. Never pass the
key on the command line or commit it.

Outputs:
    data/raw/hevy_workouts.jsonl   one workout JSON object per line (gitignored)
    data/history.csv               normalized set-level log, see tools/README.md

The Hevy API is Pro-only. Endpoint and field names below follow the published
API (GET /v1/workouts with page and pageSize, api-key header) as described in
research/mobile-workout-trackers.md; the exact response schema could not be
verified from the research sandbox. Run with --inspect first: it fetches one
page, prints the raw JSON, and exits, so the field names can be checked and the
FIELD MAP below adjusted if needed.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

BASE = "https://api.hevyapp.com/v1"
PAGE_SIZE = 10  # the API's documented maximum per page

# FIELD MAP: adjust if --inspect shows different names.
F_WORKOUTS = "workouts"
F_PAGE_COUNT = "page_count"
F_TITLE = "title"
F_START = "start_time"
F_EXERCISES = "exercises"
F_EX_TITLE = "title"
F_EX_NOTES = "notes"
F_SETS = "sets"
F_SET_INDEX = "index"
F_SET_TYPE = "type"
F_WEIGHT = "weight_kg"
F_REPS = "reps"
F_RPE = "rpe"

HISTORY_COLUMNS = [
    "date", "workout_title", "exercise", "set_index", "set_type",
    "weight_kg", "reps", "rpe", "notes", "source",
]


def get(path, key, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {"accept": "application/json"}
    if key:
        headers["api-key"] = key  # otherwise a network-secret proxy adds it
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                sys.exit(f"Hevy API refused the request (HTTP {e.code}). Set HEVY_API_KEY or a network secret for "
                         "api.hevyapp.com, and check that the account has Pro.")
            if e.code == 429 and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise
        except urllib.error.URLError as e:
            sys.exit(f"Could not reach {BASE}: {e.reason}. If this runs in a cloud sandbox, api.hevyapp.com must be on the environment's allowed domains.")


def iter_workouts(key):
    page = 1
    while True:
        data = get("/workouts", key, {"page": page, "pageSize": PAGE_SIZE})
        workouts = data.get(F_WORKOUTS, [])
        for w in workouts:
            yield w
        page_count = data.get(F_PAGE_COUNT)
        if not workouts or (page_count is not None and page >= page_count):
            return
        page += 1


LOCAL_TZ = ZoneInfo("America/New_York")  # the lifter's zone; set by --tz


def local_date(stamp):
    """Calendar date of a start time in the lifter's zone (the API reports UTC)."""
    if not stamp:
        return ""
    try:
        return dt.datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(LOCAL_TZ).date().isoformat()
    except ValueError:
        return stamp[:10]


def workout_rows(w):
    date = local_date(w.get(F_START))
    title = w.get(F_TITLE, "")
    for ex in w.get(F_EXERCISES, []):
        for s in ex.get(F_SETS, []):
            yield {
                "date": date,
                "workout_title": title,
                "exercise": ex.get(F_EX_TITLE, ""),
                "set_index": s.get(F_SET_INDEX, ""),
                "set_type": s.get(F_SET_TYPE, "normal"),
                "weight_kg": s.get(F_WEIGHT, ""),
                "reps": s.get(F_REPS, ""),
                "rpe": s.get(F_RPE, "") if s.get(F_RPE) is not None else "",
                "notes": (ex.get(F_EX_NOTES) or "").replace("\n", " "),
                "source": "hevy-api",
            }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inspect", action="store_true", help="fetch one page, print raw JSON, exit")
    ap.add_argument("--since", help="keep workouts on or after this date (YYYY-MM-DD)")
    ap.add_argument("--out", default="data/history.csv")
    ap.add_argument("--raw", default="data/raw/hevy_workouts.jsonl")
    ap.add_argument("--tz", default="America/New_York", help="time zone for workout dates (IANA name)")
    args = ap.parse_args()
    global LOCAL_TZ
    LOCAL_TZ = ZoneInfo(args.tz)

    # The key comes from HEVY_API_KEY, or is injected by the sandbox proxy when it is stored as a
    # network secret for api.hevyapp.com (then the variable is unset). Never store it in the repo.
    key = os.environ.get("HEVY_API_KEY")

    if args.inspect:
        print(json.dumps(get("/workouts", key, {"page": 1, "pageSize": 1}), indent=2)[:6000])
        return

    os.makedirs(os.path.dirname(args.raw), exist_ok=True)
    n_workouts = n_rows = 0
    with open(args.raw, "w") as raw, open(args.out, "w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=HISTORY_COLUMNS)
        writer.writeheader()
        for w in iter_workouts(key):
            date = local_date(w.get(F_START))
            if args.since and date < args.since:
                continue
            raw.write(json.dumps(w) + "\n")
            n_workouts += 1
            for row in workout_rows(w):
                writer.writerow(row)
                n_rows += 1
    print(f"Wrote {n_workouts} workouts, {n_rows} sets to {args.out} (raw JSON in {args.raw}).")


if __name__ == "__main__":
    main()
