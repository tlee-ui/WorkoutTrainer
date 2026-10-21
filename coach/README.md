# Coach runbooks

Last updated: 2026-10-21

Agent instructions for the weekly coaching cadence in `guide/08-weekly-coaching-cadence.md`. Two scheduled tasks start a fresh Claude session and point it at one of these files.

| Scheduled task | When (America/New_York) | Runbook | Ends with |
|---|---|---|---|
| Sunday training check-in | Sun 6:47 pm | `sunday-checkin.md` | The five questions. After your answers: the week plan and Monday's workout |
| Tomorrow's workout | Mon-Sat 7:47 pm | `nightly-brief.md` | Tomorrow's session, or nothing on a rest day |

## Files

| File | Read | Written |
|---|---|---|
| `data/track-state.md` | both | both (after an H exposure, a miss, or a pointer move) |
| `data/weekly-plan.md` | both | Sunday writes it; nightly amends it |
| `data/checkins/YYYY-MM-DD.md` | Sunday reads the last one | Sunday |
| `data/history.csv` | both | `tools/hevy_pull.py` (when `HEVY_API_KEY` is set) |
| `data/manual-log.csv` | both | both, when sets are reported in the chat (`templates/log-template.csv` columns, pounds) |
| `templates/*.md` | both | never (the program is changed only by the CLAUDE.md update procedure) |

## Rules every run follows

1. **Branch.** Work on the branch named in the scheduled task's prompt. Fetch it first, then commit and push the files above at the end of the run. Other files are never touched by these runs.
2. **Dates.** Get today's date with `TZ=America/New_York date +%F`. "Tomorrow" means tomorrow in that time zone.
3. **Units.** Pounds everywhere the lifter sees. `data/history.csv` stores kilograms (x 0.45359237); convert when reading it.
4. **Never** advance a load on a miss, during a deload, from a V exposure, or from a substitute lift (`guide/07-tracking-and-apps.md` §4).
5. **Never** invent results. If the log has no data for a session and the lifter hasn't said, ask. Don't assume it went to plan.
6. **Rules come from the repo, not memory.** Loads: `templates/progression-tracks.md`. Week shape: `templates/README.md` and `guide/03-flexible-scheduling.md` §4. Session content: the matching `templates/N-day-week.md`.
7. **Medical.** For pain that changes movement, or illness, suggest a physician or physiotherapist. Give only general training guidance.
8. **Record changes.** Write what changed and why as a dated line in the check-in record (Sunday), or in the `Changes this week` list in `data/weekly-plan.md` (nightly).
9. **The last message is the deliverable.** The final text of the run is what the lifter sees in the notification. Put the questions or the brief there, not a summary of the git work.

## Getting the week's results

1. If `HEVY_API_KEY` is set: `python3 tools/hevy_pull.py`. It rewrites `data/history.csv` from the full Hevy history. On the first run, or after a schema error, run `--inspect` and check the field names against `tools/README.md` "Unverified items" before trusting the output.
2. Rows whose `workout_title` is a slot name (L1-U3, Full A/B/C) map onto the rotation. A workout with another title: ask which slot it was.
3. If there is no key, or the pull fails: take the results from the chat and append them to `data/manual-log.csv`. Mention the failure once in the message.
