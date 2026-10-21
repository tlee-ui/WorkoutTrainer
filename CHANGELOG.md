# Changelog

## 2026-10-21

- Initial repository structure: `research/`, `guide/`, `templates/`.
- First research round: training frequency and volume evidence, splits and named
  programs, flexible-frequency programming, periodization and progression,
  exercise selection and session design, recovery, nutrition, and cardio.
- First edition of the training guide and 3/4/5/6-day templates.
- Guide chapters 00-06 written from the research notes; chapter 01 and 04 wording
  aligned with the rotation design in chapter 03 (one pass per calendar week in
  any 3-6-day week; at least 2 exposures per muscle, 3 for large muscles).
- Research note on mobile workout trackers added (Liftosaur and Hevy Pro are the
  two apps with an agent-writable program path).
- Chapter 07 on tracking and apps, a Liftosaur rendering of the rotation under
  `templates/liftosaur/`, and `templates/log-template.csv`.
- Added `tools/`: Hevy API pull, Hevy CSV import, history analysis that proposes
  starting loads per the progression tracks; `data/` for the normalized log.
- Imported the user's Hevy export (52 sessions, 2024-03 to 2026-10) to
  `data/history.csv`; `data/history-summary.md` holds the analysis and proposed
  starting loads. Analyzer gained alias exclusions and a pounds column.
- Added `data/track-state.md`: the live state of the six progression tracks in
  kilograms, seeded from the imported history, with the rotation pointer at L1.
- Converted templates, progression rules, the chapter 03 worked example, and the
  Liftosaur file from kilograms to pounds (5 lb squat and deadlift steps, 2.5 lb
  bench and press steps). Research notes and study citations stay in their
  source units.
- Added `tools/hevy_push.py` and `tools/hevy_program.json`: write the pound loads
  in `data/track-state.md` into the nine Hevy routines (dry run by default), so the
  app is ready before each session. The existing routines still held the kilogram
  loads. Research note addendum records the Hevy API spec, checked live.
