# Current track state

Last updated: 2026-10-21. Units: kilograms. The program runs in kilograms; set the Hevy app's weight unit to kg so future exports need no conversion (`tools/hevy_csv_import.py` converts either way).

This file is the live state of the six main-lift tracks defined in `templates/progression-tracks.md`. Update it after every heavy (H) exposure. Agents read it to plan the next week.

## Where the rotation stands

| Item | State |
|---|---|
| Rotation pointer | **L1** (Lower A). The sessions of 17-21 Oct 2026 were a return-to-training block, not a pass of the rotation, so the program starts fresh. |
| Block week | 1 of 6 when the first pass starts. Deload falls in week 5-7 or when two readiness flags persist (`templates/README.md`). |
| Rest before starting | 2-4 days planned after four sessions in five days. All six lifts were exposed within the last 7 days, so the gap table in section 8 does not fire for the first pass. If the rest stretches past 8 days from the dates below, hold the loads rather than add. |
| First week | Count the days available and open the matching template. 3 days: Full A, Full B, Full C. 6 days: L1, U1, L2, U2, L3, U3. |

## The six tracks

Starting loads come from `data/history-summary.md` (80% of the estimated 1RM from the sets of 17-20 Oct 2026, rule in `templates/progression-tracks.md` section 2). Back-offs are the top set x 0.93, V sets 90% of the track load, both rounded to 2.5 kg.

| Lift | Top set for next H (4 @ RPE 8) | Back-offs (x 4) | V exposure load | Rep target | Miss counter | Last exposure | e1RM history |
|---|---|---|---|---|---|---|---|
| Squat | **60** | 55 | 55 (4 x 6; 3 x 6 merged) | 4 | 0 | 2026-10-17 (61 x 8, 8, 8) | 78 (estimate from 17 Oct, 8s at no logged RPE) |
| Bench press | **42.5** | 40 | 37.5 (4 x 6) | 4 | 0 | 2026-10-20 (43 x 8, 8, 6) | 55 |
| Deadlift | **work up** | 2 x 4 at -7% of the load found | 90% of the load found (3 x 4) | 4 | 0 | 2025-04-14 | 84 (Sep 2024 peak); none recent |
| Overhead press | **27.5** | 25 | 25 (3 x 5) | 4 | 0 | 2026-10-17 (29.5 x 7, 5) | 36 |
| Barbell row | **32.5** for 4 x 6-8 | n/a (double progression) | 30 (3 x 8-10) | 6-8 | 0 | 2026-10-18 (29.5 x 12, 12, 12) | 41 |
| Pull-up / pulldown | **57.5** pulldown for 4 x 5-8 | n/a | 50-52.5 (3 x 6-8 at RPE 7) | 5-8 | 0 | 2026-10-17 (61 x 6, 6) | 73 |

Notes on each:

- **Squat.** 60 kg will feel light against the 2024 peak (113 x 5). That is intended. If the top set comes in at RPE 7 or lower, section 5 allows +5 kg jumps until it stops; expect to reach 70-75 within three heavy exposures.
- **Bench.** The recent 43 x 8 sets were at an unknown RPE. 42.5 x 4 should be about RPE 6-7; take the +2 kg jump when it is.
- **Deadlift.** Untrained for 18 months. On the first L2 (or Full B): warm up, then 40 x 4, 50 x 4, 60 x 4, 65 x 4, adding 5 kg per set until 4 reps feel like RPE 8. Stop there, log that load as the track load, then do 2 back-offs at 93%. The 2024 history (70 x 6) suggests the stopping point will be somewhere between 60 and 70 kg, but let the RPE decide.
- **Overhead press.** 27.5 is 80% of the recent estimate. Fractional plates matter here: without 0.5 kg plates, add 2.5 kg every second successful exposure.
- **Row.** The recent rows were 12s at 29.5. 32.5 for 4 x 6-8 at RPE 8 may be light; if all four sets hit 8 at RPE 7 or lower, go straight to 35 next time.
- **Pulldown.** Running as the pull-up track until a pulldown set at about bodyweight reaches 8 reps; then switch to the bar (section 2). You did bodyweight pull-ups for up to 8 in 2024, so this switch may come early.

## Accessory starting loads (double progression, first set with 2-3 reps in reserve)

From the recent log where one exists; otherwise choose on the day and record here.

| Exercise (template slot) | Start | Source |
|---|---|---|
| Incline DB press (U1) | 2 x 15 kg dumbbells, 3 x 8-12 | Oct 2026 incline barbell 20 x 12 was an empty bar; 2024 incline DB 34 x 8 |
| Lateral raise (U1, U2, U3) | 7.5-9 kg, 3 x 12-15 | 2024 peak 18 x 8; recent 13 kg e1RM estimate |
| DB curl (U2, U3) | 12.5 kg, 3 x 8-12 | Recent 19 kg e1RM estimate; 2024 peak 22.7 x 8 |
| Overhead triceps extension (U1) | 12.5 kg DB, 3 x 10-15 | Oct 2026 extensions logged |
| Lying or seated leg curl (L1, L2, L3) | choose on the day | Two sessions logged Oct 2026; load not carried over |
| Romanian deadlift (L1) | 50 kg, 3 x 8-10 | One barbell RDL logged 18 Oct 2026; 2024 DB RDL 45 x 8 |
| Reverse lunge or split squat (L2) | 2 x 15 kg, 3 x 10 per leg | Oct 2026 reverse lunge 13.6 x 16 |

## Log format

Per set in Hevy, name the routine after the slot (L1, U1, ..., Full A, Full B, Full C) so exports map straight onto the rotation. Use Hevy's RPE field on top sets at minimum. After each H exposure, update the table above and append a line to the e1RM history. The Markdown fallback is `templates/log-template.csv`.
