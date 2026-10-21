# Agent instructions for WorkoutTrainer

This repository is a knowledge base, not a software project. Agents working here
research resistance-training topics and turn the findings into a training guide.

## Goals of the knowledge base

- Help an intermediate lifter build and run an effective strength and
  hypertrophy program.
- Support a variable schedule: some weeks 5 to 6 training days, other weeks
  only 3. Every recommendation must say how it changes with available days.
- Prefer evidence from peer-reviewed research, then well-cited practitioner
  sources (Stronger By Science, Renaissance Periodization, Barbell Medicine,
  MASS Research Review, program authors' own writing). Say which is which.

## Where things go

- `research/<topic>.md`: one topic per file. Dense notes with citations. Keep
  exact numbers (sets, reps, percentages, effect sizes). Record conflicting
  findings instead of picking a side silently. Add a dated "Last updated" line
  at the top. Do not rewrite another note's conclusions; add a new note or an
  addendum section with the date.
- `guide/NN-<chapter>.md`: synthesized, actionable chapters. Every rule should
  trace back to a research note. Numbered for reading order.
- `templates/<days>-day-*.md`: concrete weekly layouts with exercises, sets,
  reps, and progression rules. Templates must state how they scale up or down.

## Research conventions

- Search broadly, then verify specific claims against the primary source.
- Cite with author, year, and journal or site, plus a URL when available.
- Distinguish strength outcomes from hypertrophy outcomes.
- Mark older foundational work (pre-2016) as such.
- Note paywall or copyright status when describing a named program, and
  describe rather than reproduce copyrighted material.

## Updating the guide

1. Write or update the research note first.
2. Change the guide chapter, referencing the note.
3. Update any template the change affects.
4. Add a line to `CHANGELOG.md` describing what changed and why.

## Style

- Markdown. Tables for comparisons. Short sentences.
- Units: the user lifts in pounds. Templates, progression rules, worked examples,
  and `data/track-state.md` are in pounds. `data/history.csv` stores kilograms
  internally; research notes quote whatever the source used. Be consistent
  within a file.
- No medical advice beyond general training guidance; flag when a reader should
  consult a professional.
