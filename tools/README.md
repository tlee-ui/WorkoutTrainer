# Tools

Scripts for getting training history into the repo and reading it back out.
Python 3, standard library only.

| Script | Purpose |
|---|---|
| `hevy_pull.py` | Pull the full workout history from the Hevy API (Pro required) into `data/history.csv`. Key read from the `HEVY_API_KEY` environment variable only. `--inspect` prints one raw page so the field names can be checked against the API docs before a full pull. |
| `hevy_push.py` | Write the next loads into the Hevy routines (Pro required). Reads main-lift loads from `data/track-state.md` and the routine layout from `hevy_program.json`, prints a per-routine diff, and writes only with `--apply`. Touches only the routines in the program's folder (`Rotation 2026-10`). |
| `hevy_program.json` | The nine routines (L1-U3, Full A-C) as Hevy sees them: exercise template IDs, sets, rep ranges, rest, supersets, accessory loads in pounds. Mirrors `templates/6-day-week.md` and `templates/3-day-week.md`; edit it when those change or an accessory load moves up. |
| `hevy_csv_import.py` | Convert a CSV exported from the Hevy app (Profile > Settings > Export & Import Data) into `data/history.csv`. Works without Pro or network access. |
| `analyze_history.py` | Summarize `data/history.csv`: sessions per year, per-exercise best e1RM, and proposed starting loads for the six main-lift progression tracks. Writes `data/history-summary.md`. |
| `lift_aliases.json` | Maps the six main lifts to the exercise names used in the log. Edit to match your names; `analyze_history.py --list-exercises` shows them. |

## Normalized log format

`data/history.csv` is the single format every analysis reads. One row per set.

| Column | Meaning |
|---|---|
| `date` | YYYY-MM-DD |
| `workout_title` | Session name as logged (Hevy routine title); for this program use L1, U1, L2, U2, L3, U3, Full A, Full B, Full C |
| `exercise` | Exercise name as logged |
| `set_index` | 0-based set order within the exercise |
| `set_type` | normal, warmup, failure, drop |
| `weight_kg` | Load in kg, converted from the pound values in the Hevy export (bodyweight exercises: added load, or empty). The program files and `data/track-state.md` are in pounds; the analyzer prints both. |
| `reps` | Reps completed |
| `rpe` | Logged RPE, if any |
| `notes` | Exercise notes |
| `source` | hevy-api, hevy-csv, or manual |

`templates/log-template.csv` is the manual-entry version of the same thing with fewer columns; `analyze_history.py` reads either.

## Typical flow

```bash
# Option A: API (Pro). Needs HEVY_API_KEY as an environment secret and
# api.hevyapp.com allowed by the sandbox's network policy.
python3 tools/hevy_pull.py --inspect          # check field names once
python3 tools/hevy_pull.py                    # full pull

# Option B: app export. Export from the Hevy app, put the file in data/raw/.
python3 tools/hevy_csv_import.py data/raw/hevy_export.csv

# Then
python3 tools/analyze_history.py --list-exercises   # fix tools/lift_aliases.json if needed
python3 tools/analyze_history.py                    # writes data/history-summary.md
```

## Pushing the next week to Hevy

After `data/track-state.md` is updated (after each heavy exposure, or weekly):

```bash
python3 tools/hevy_push.py            # dry run: per-routine diff, request bodies in data/raw/hevy_push_plan.json
python3 tools/hevy_push.py --apply    # write to Hevy
python3 tools/hevy_push.py            # confirm every routine reads "unchanged"
```

Loads are planned in pounds and sent as `lb x 0.45359237` kg, the factor the app
uses for pound entries, so they show as round numbers in an app set to pounds.
Warm-ups follow the template rule: a ramp (bar x 10, 40% x 8, 60% x 5, 80% x 2)
on the session's first main lift and one feeder set at 65% on later ones, rounded
to 5 lb. While the deadlift track is unset, L2 and Full B carry the work-up from
`data/track-state.md` as warm-up sets and leave the top set blank. Routine sets
have no RPE field, so RPE targets and the progression rule go in each exercise's
notes. Deloads are not generated; edit the track state or push by hand for a
deload week.

In the Claude Code cloud sandbox the proxy adds the `api-key` header, so
`HEVY_API_KEY` can stay unset for `hevy_push.py`. `hevy_pull.py` still requires
the variable; any placeholder value works there.

## What is committed

`data/history.csv` and `data/history-summary.md` are tracked so agents in later
sessions can read them. `data/raw/` is gitignored (large, and the API JSON may
include fields you do not want in git). The API key is never written anywhere.

## Verified items

On 2026-10-21 the live spec at `https://api.hevyapp.com/docs/` was reachable.
It confirms the workout fields `hevy_pull.py` reads, including a per-set `rpe`.
It also gives the routine write schema `hevy_push.py` uses: `PUT /v1/routines/{id}`
with `title`, `notes` and `exercises[]` (`exercise_template_id`, `superset_id`,
`rest_seconds`, `notes`, and `sets[]` of `type`, `weight_kg`, `reps`, `rep_range`).
See the addendum in `research/mobile-workout-trackers.md`.

## Unverified items

The Hevy API response schema (`workouts`, `page_count`, `exercises[].sets[].weight_kg`,
`reps`, `rpe`, `index`, `type`) and the app export's column names follow the
published API and the community SDK described in
`research/mobile-workout-trackers.md`, but could not be checked against
`api.hevyapp.com/docs` from the research sandbox. Both scripts print what they
found so a mismatch is visible on the first run.
