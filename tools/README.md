# Tools

Scripts for getting training history into the repo and reading it back out.
Python 3, standard library only.

| Script | Purpose |
|---|---|
| `hevy_pull.py` | Pull the full workout history from the Hevy API (Pro required) into `data/history.csv`. Key read from the `HEVY_API_KEY` environment variable, or added by the sandbox proxy when it is stored as a network secret for `api.hevyapp.com`. `--inspect` prints one raw page so the field names can be checked against the API docs before a full pull. |
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

## What is committed

`data/history.csv` and `data/history-summary.md` are tracked so agents in later
sessions can read them. `data/raw/` is gitignored (large, and the API JSON may
include fields you do not want in git). The API key is never written anywhere.

## Verified 2026-10-21

A live pull returned 52 workouts and 685 sets: the same sets as the app's CSV export in `data/history.csv`. The fields `workouts`, `page_count`, `exercises[].sets[].weight_kg`, `reps`, `rpe`, `index` and `type` are as the script expects. Two differences:

- The API's `start_time` is UTC. `hevy_pull.py` now converts it to the lifter's zone (`--tz`, default America/New_York), so evening sessions keep their local date.
- A few exercise titles differ from the export (for example "Bulgarian Split Squat" vs "Bulgarian Split Squat (Dumbbell)"). None of them is a main lift.

Routines: `PUT /v1/routines/{id}` with `{"routine": {"title", "exercises": [...]}}` works. Leave `rep_range` out of a set that has fixed `reps`; a null value is rejected. Weights are `weight_kg`. Write the pound value x 0.45359237 at full precision, so the app shows exact pounds.
