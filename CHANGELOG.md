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
- Weekly coaching cadence. New research note `research/coaching-check-ins.md`
  covers readiness questionnaires (Saw 2016; Hooper & Mackinnon 1995), RIR
  autoregulation, and supervision (Mazzetti 2000; Fisher 2022). New chapter
  `guide/08-weekly-coaching-cadence.md` sets out a Sunday 6:47 pm ET check-in
  (five questions, then the guide 03 section 4.1 procedure) and a night-before
  brief Mon-Sat at 7:47 pm ET. New `coach/` runbooks for the scheduled sessions,
  plus `data/weekly-plan.md`, `data/checkins/` and `data/manual-log.csv` for
  state. Results come from the Hevy API when `HEVY_API_KEY` is set, otherwise
  from the chat. Why: the user asked for a personal-trainer rhythm; the program
  rules are unchanged.
- Equipment: the lifter's smallest plate is 2.5 lb, so every barbell load is now a
  multiple of 5 lb. Bench and press move 5 lb after every second successful heavy
  top set (a step counter in `templates/progression-tracks.md` section 5 and
  `data/track-state.md`), instead of the 2.5 lb steps that needed 1.25 lb plates.
  All computed loads (back-offs, V sets, warm-ups, deloads, resets) round to the
  nearest 5 lb. Accessory loads are a single weight, not a range. The guide 03
  worked example, the guide 07 sample rows, the Liftosaur file, the coach runbooks
  and the seeded week plan were recalculated. Rationale: addendum in
  `research/periodization-and-progression.md`. Why: the user reported uneven
  load sizes they could not build with their plates.
