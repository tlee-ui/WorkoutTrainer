# Variable-Frequency Lifting Programming (3 to 6 sessions/week, scaling week to week)

**Research-method note for the report writer:** In this session WebFetch failed with DNS errors on every domain (strongerbyscience.com, pubmed, thefitness.wiki, forum.barbellmedicine.com) and curl was blocked at the proxy, so no page could be read in full. Every finding below comes from search-engine result summaries of the cited pages, not from the pages themselves. Treat quoted numbers as "reported by the search summary of [Source]" and verify any load-bearing figure against the primary page before publishing. Where a claim could not be tied to a URL it is listed under Gaps or clearly labelled as an inference.

---

## KQ1. What approaches do coaches recommend for inconsistent schedules (rotating/floating splits, full-body defaults, collapsing upper/lower, PPL rotation, weekly volume targets)?

### Takeaway
The dominant practitioner pattern is a **sequence-driven ("floating"/rotating) split** that advances to the next session in a fixed order whenever you train, decoupled from the calendar week; the main alternative is a **full-body default** which is explicitly described as the most forgiving structure when sessions get skipped. No source I found offers a single named program that formally scales 3→6 days; the scaling comes from the rotation plus volume rules (KQ3).

### Cited Findings
- A Renaissance Periodization article describes a "Pull-Legs-Push floating split" where the order is Pull, Legs, Push, repeat; "floating" means "there are no assigned days of the week": you take a rest day when you need recovery and "roll right into the next session when you feel good," allowing 5–7 training days/week without being tied to a calendar; the rotation is organised as two alternating microcycles, A and B — [RP Strength: Dr. Mike's Exact Training Split](https://rpstrength.com/blogs/video-guides/dr-mikes-exact-training-split-to-get-to-6-body-fat)
- Splitline (iOS tracker) is built on a "sequence-driven rotation system" that "automatically adjusts the training sequence based on actual workout completion rather than a fixed weekly schedule," replacing calendar-based scheduling — [Splitline listing](https://marlvel.ai/api/llm/apps/health-fitness/splitline)
- A Huberman Lab Q&A summary states consistency matters more than a strict 7-day split and that workouts "do not necessarily have to align with the calendar week" — [Huberman Lab AI summary](https://ai.hubermanlab.com/s/LyqZA5gY)
- A separate Huberman Lab summary says a missed session on an upper/lower split "can lead to imbalanced training frequencies for muscle groups," and full-body routines are presented as the more forgiving option when schedules slip; a Jeff Cavaliere summary in the same results argues full-body training reduces the likelihood of missing sessions — [Huberman Lab AI summary](https://ai.hubermanlab.com/s/KzMpBlrW)
- Coaches on the Starting Strength forum field questions from lifters on 5-on/2-or-3-off oil-field rotations asking for the training days to "rotate around my schedule instead of being fixed" — [Starting Strength forum](https://startingstrength.com/resources/forum/general-programming/69192-programming-rotational-schedule.html)
- A trainer-platform feature request (ABC Trainerize) asks for a "rotating" option because the calendar "doesn't allow a split like workout 1 … revolving through the weeks" — evidence that the rotation model is a common coaching need not well served by calendar-based apps — [ABC Trainerize ideas](https://ideas.abcfitness.com/forums/167887-coach-trainer-abc-trainerize/suggestions/41288233-flexability-in-scheduling-workouts)
- The r/Fitness Basic Beginner Routine alternates Workout A and Workout B with a rest day between sessions (A/B/A one week, B/A/B the next), i.e. a 2-session rotation that is indifferent to which weekday it lands on — [thefitness.wiki BBR](https://thefitness.wiki/routines/r-fitness-basic-beginner-routine/); Weightology's "2–3 Day Per Week Whole Body" plan uses the same ABA/BAB alternation and is explicitly marketed for 2 or 3 days — [Weightology](https://weightology.net/?p=7759)
- Boostcamp's program library lets users filter programs by days per week (2–6) and advises that "days per week should be a schedule you can keep for the program's full length"; individual programs list one fixed day count, and the app's accommodation for a bad week is a "reschedule sessions" feature rather than a program that changes shape — [Boostcamp program library](https://www.boostcamp.app/features/program-library)
- Built With Science's help centre tells users who miss a workout to mostly "stick to continuing with the schedule," noting that one or two missed workouts make little long-run difference; the alternative they describe is moving the missed session to the next day and pushing the rest back (swapping a rest day) — [Built With Science help](https://help.builtwithscience.com/en/what-happens-if-i-miss-a-workout)
- A Freeletics support reply describes the simplest rotation rule: skipped training days are "simply moved to the next scheduled training day" — [Freeletics forum](https://forum.freeletics.com/t/how-to-move-training-days-in-a-week/9058/6)
- Community forum consensus (Cathe forums, multiple threads) on missed sessions in a rotation: (a) shift the rotation forward a day so nothing is lost, which "avoids a lopsided week, such as doing upper body twice with no lower body"; (b) double up only when the two sessions are compatible and "not on consecutive days" for heavy work; (c) never skip a strength session but do skip missed cardio — [Cathe forum 225177](https://cathe.com/forum/threads/what-do-you-do-when-missing-days-in-rotation.225177); [Cathe forum 197583](https://cathe.com/forum/threads/rotation-miss-a-day-do-you-do-double-the-next-day.197583)

### Inferences
- **Rotation rule (strongest practitioner support):** Define an ordered list of sessions (e.g., Full A, Full B, Full C or Push, Pull, Legs; or Upper A, Lower A, Upper B, Lower B). Every time you train, do the next one. A 3-day week completes one pass of a 3-session rotation; a 6-day week completes two. Nothing is "missed," so there is no make-up logic needed.
- **If 3 days available → full-body rotation** (A/B/C or A/B alternating). If 4 → upper/lower. If 5–6 → PPL rotation or upper/lower + extra. The cited sources agree full body is the most robust at low frequency and that PPL is the standard floating split at 5–7 days.
- **Collapse rule for upper/lower:** The Huberman/Cavaliere summaries imply the failure mode of U/L is lopsided weeks. A designer should therefore either (a) run U/L as a strict rotation (never skip ahead), or (b) when a week drops to 3 days, switch that week to full-body sessions built from the U/L exercise pool so every muscle is still trained twice.
- Apps (Boostcamp, Trainerize) mostly do NOT scale programs; they reschedule. The scaling logic must live in the program design itself.

### Gaps
- I found no Reddit (r/Fitness, r/weightroom, r/naturalbodybuilding) threads via search; results were dominated by other forums. Community terminology ("rolling split," "floating split") is attested only in the RP article and the Splitline listing.
- No source gives a formal rule for "weekly volume target filled by however many sessions are available"; that method is an inference supported by the frequency literature in KQ3, not a named coaching protocol I could cite.

---

## KQ2. How do 5/3/1 (Wendler), GZCL (LeFever), and Stronger By Science (Nuckols) handle 2-day / variable-day training and missed days?

### Takeaway
Wendler's official position is that 5/3/1 fits "2, 3, or 4 days per week" and has a dedicated "Twice A Week" template; the mechanism is that the cycle stretches in calendar time rather than compressing content (3 days/week → a 4-lift cycle takes 5+ weeks instead of 4). GZCLP is a 4-session rotation that is routinely run on 3 days by continuing the sequence. Nuckols' position is that frequency is largely a tool for distributing volume, so sessions can be redistributed freely as long as weekly sets are preserved. Specific "missed day" rules from Wendler and LeFever could not be verified from primary text.

### Cited Findings
**5/3/1 (Wendler)**
- Wendler's own product page states 5/3/1 "is flexible enough to fit any schedule — 2, 3, or 4 days per week," and the 2nd Edition includes "full body training" — [jimwendler.com 5/3/1 2nd Edition](https://www.jimwendler.com/products/5-3-1-second-edition-ebook)
- Wendler's "Training Templates" eBook (via EliteFTS) lists 14 templates including one titled "The Twice A Week," alongside the original three-day template — [EliteFTS: Training Templates by Jim Wendler](https://elitefts.com/products/training-templates-by-jim-wendler-ebook)
- A third-party guide reports the two-day option runs within a 4-week cycle, starting with the main lifts and adding assistance, keeping sessions ~60 minutes — [Muscle & Strength](https://www.muscleandstrength.com/node/4458)
- The same guide states that a 5/3/1 mesocycle "lasts 4 weeks if you train 4 days per week, and 5+ weeks if you train 3 days per week," i.e. the four main-lift sessions are run in sequence regardless of calendar week — [Muscle & Strength](https://www.muscleandstrength.com/node/4458)
- 5/3/1 Forever structure: "Leaders" are volume blocks (two 3-week waves with higher-volume supplemental work such as Boring But Big); "Anchors" are intensity blocks (one 3-week wave with higher-intensity templates like First Set Last/Widowmaker, AMRAP on the top set); the standard sequence is Leader, Leader, 7th Week Protocol, Anchor, 7th Week Protocol. The book's core philosophy is 3–4 days/week with one main barbell lift per day — [train531.com](https://train531.com/blog/531-forever/)
- On the T-Nation Jim Wendler coaching forum, a thread titled "Leader/Anchor 4 Day Forever Templates 2 Days a Week" contains the suggestion to "run 2 days a week with all four lifts but only go heavy on 2 and do supplemental for the other 2 and then swop the next week" (i.e., each session = one heavy 5/3/1 lift + one supplemental lift, alternating which pair is heavy) — [T-Nation thread](https://t-nation.com/t/leader-anchor-4-day-forever-templates-2-days-a-week/275860)
- Lift Vault hosts 5/3/1 spreadsheets for multiple day counts — [Lift Vault 5/3/1](https://liftvault.com/programs/powerlifting/jim-wendlers-531-spreadsheet/)
- Wendler's blog has a tag page for 5/3/1 Forever content — [jimwendler.com blog](https://www.jimwendler.com/blogs/jimwendler-com/tagged/5-3-1-forever)

**GZCL / GZCLP (Cody LeFever)**
- GZCLP is a beginner linear progression built on three tiers: T1 primary lift (heavy), T2 secondary lift (lighter, higher reps), T3 accessories. It is described in a 3-day and a 4-day version; when you fail a T1/T2, you rotate to the next rep scheme (e.g. 5x3 → 6x2 → 10x1) rather than immediately resetting weight — [thefitness.wiki GZCLP](https://thefitness.wiki/routines/gzclp/); [Boostcamp GZCLP](https://boostcamp.app/cody-lefever/gzcl-program-gzclp); [StrongrFastr GZCLP 4-day](https://www.strongrfastr.com/fr/programmes_entra%C3%AEnement/20271-gzclp_sur_4_jours)
- The program's four workouts (A1, B1, A2, B2) are described as a rotation; the 3-day version runs the same four sessions in order across weeks (the fitness.wiki page recommends reading LeFever's original r/gzcl post and infographic for applications) — [thefitness.wiki GZCLP](https://thefitness.wiki/routines/gzclp/)

**Stronger By Science (Greg Nuckols)**
- Nuckols' research spotlight: the Norwegian Frequency Project found that in well-trained powerlifters, training each lift 6x/week beat 3x/week when volume was equated (the 3x group did twice as many sets per session) — [SBS research spotlight: frequency](https://www.strongerbyscience.com/research-spotlight-frequency/)
- Nuckols reports the pool of volume-matched frequency studies doubled from 8 to 16 (c. 2017–2018), that a meta-analysis found frequency had no meaningful impact on strength for upper or lower body, and that higher frequency may still help by allowing higher volume and/or higher average set quality — [SBS research spotlight: frequency](https://www.strongerbyscience.com/research-spotlight-frequency/)
- Nuckols' practical rule: "If you're doing fewer than ~10 sets per muscle group, per week, a once-per-week training frequency is probably perfectly fine" — [SBS research spotlight: frequency](https://www.strongerbyscience.com/research-spotlight-frequency/)
- SBS also hosts a video describing Pak's PhD work on the minimum effective training dose for strength in powerlifters — [SBS videos](https://www.strongerbyscience.com/videos/page/3/)

### Inferences
- **5/3/1 scaling rule:** Treat the four main-lift days as a rotation (Press, Deadlift, Bench, Squat). Advance one per session. 2 days/week → cycle takes 2 weeks per "week" of the program; 3 days → 4 weeks of content take ~5.3 weeks; 4 days → 4 weeks. Progression (training-max increase) happens per completed 3-week wave of content, not per calendar block.
- **5/3/1 compression rule (from the T-Nation thread):** On a short week, pair lifts: Session 1 = heavy Squat + Bench as supplemental; Session 2 = heavy Press + Deadlift as supplemental; next week swap which lift is heavy. This keeps all four lifts touched every week.
- **GZCL tier-priority rule (inference from tier structure, not a quoted LeFever rule):** When time or days are cut, keep T1 intact, trim T2 sets, drop T3 first. This follows from the tiers being defined by priority (T1 heaviest/most specific), but I could not find LeFever's own text stating it.

### Gaps
- Could not retrieve the actual content of Wendler's "Twice A Week" template, the "5/3/1 for busy people"/2x2x2 article, or 5/3/1 Forever's 2-day chapter. Search returned no jimwendler.com article with those titles; one T-Nation thread and the product-page quote are the only Wendler-attributable evidence. Wendler's rule for a skipped day inside a wave is unverified.
- Could not retrieve LeFever's blog (swoleateveryheight.blogspot.com) or r/gzcl guidance on missed days; the "GZCL Applications & Adaptations" material did not surface.
- The SBS article's full text (and any newer SBS pieces on frequency flexibility) could not be fetched.

---

## KQ3. Minimum effective dose / maintenance weeks; how should volume and intensity change between a 3-day and a 6-day week?

### Takeaway
The literature is consistent: with weekly volume matched, frequency has little to no independent effect on hypertrophy or strength, so a 3-day week can preserve nearly all of a 6-day week's stimulus if sets are redistributed, up to a per-session ceiling (~6–11 sets per muscle per session depending on counting method). When volume must drop, **intensity (load) is the variable to protect**: maintenance has been shown with as little as 1 session and 1 set per exercise per week (young adults) provided relative load is kept.

### Cited Findings
**Frequency with volume equated**
- Schoenfeld, Grgic & Krieger (2019), 25 studies / 836 participants / 6–30 weeks: "Resistance training frequency does not significantly or meaningfully impact muscle hypertrophy when volume is equated. Conversely, a significant effect favoring higher frequencies [was] observed when volume was not equated" — [PMC table summarising Schoenfeld 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC9302196/table/T1)
- A 2021 Frontiers in Physiology review: latest meta-analyses point to a limited role for frequency at matched volume, but volume-equated studies in trained participants are scarce — [Frontiers 2021](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2021.789403/pdf)
- The 2016 Schoenfeld frequency meta-analysis is often cited for a frequency advantage, but most included studies were not volume-equated — [Biolayne REPS](https://biolayne.com/reps/issue-31/the-king-of-volume-metas/)
- PeerJ 2021 (trained men, volume-matched, 2 vs 4 sessions/week): "no additional benefits of increasing the training frequency from two to four sessions under volume-equated conditions, but it could be favorable to spread the total training volume into several training bouts through the week to avoid potential increases in RPE" — [PeerJ 10781](https://peerj.com/articles/10781)
- Nuckols: <~10 sets/muscle/week → once-weekly frequency is fine; higher frequency mostly matters as a way to get more or better-quality volume in — [SBS research spotlight: frequency](https://www.strongerbyscience.com/research-spotlight-frequency/)

**Per-session volume ceiling (how many sets you can cram into fewer sessions)**
- A meta-regression preprint on per-session volume found hypertrophy gains "level off around ~11 'fractional' sets" per session, with insufficient data at very high per-session volumes; it stresses that "fractional" vs "direct" set counting are not comparable — [SportRxiv preprint](https://sportrxiv.org/index.php/server/preprint/download/537/1148/1071); RP's summary of the same work calls it "the 11-set rule" — [RP Strength](https://rpstrength.com/blogs/podcasts/training-frequency-decoded-the-11-set-rule-every-lifter-should-know)
- The university release on that work reports the strength threshold is much lower: about two direct (hard) sets per exercise per session before diminishing returns — [FAU newsdesk](https://fau.edu/newsdesk/articles/build-muscle-gain-strength-study.php)
- Menno Henselmans, citing an informal Krieger meta-analysis, gives a rule of thumb of no more than ~6 sets per muscle group per session — [Henselmans](https://mennohenselmans.com/this-is-the-max-volume-you-should-do-per-workout/); contrast with the ~11 fractional-set figure above (conflict largely explained by counting method).

**Maintenance / minimum dose**
- Spiering, Mujika, Sharp & Foulis (2021, J Strength Cond Res 35(5):1449–1458): strength and muscle size "(at least in younger populations) can be maintained for up to 32 weeks with as little as 1 session of strength training per week and 1 set per exercise, as long as exercise intensity (relative load) is maintained"; older populations may need up to 2 sessions/week and 2–3 sets per exercise; insufficient data to make recommendations for athletes/military; only included studies with ≥4 weeks of reduced training — [PubMed 33629972](https://pubmed.ncbi.nlm.nih.gov/33629972/)
- Bickel, Cross & Bamman (2011, MSSE 43(7):1177–87): after 16 weeks of 3x/week training, young adults (20–35) maintained size and strength for 32 weeks on 1/3 or 1/9 of the training dose; Examine's hedged summary: "reducing training frequency to 1–2 times per week and performing approximately one-ninth of previous training volume may be sufficient to maintain muscle size and strength." Sources conflict on whether older adults (60–75) maintained size; several summaries say they did not on either reduced dose — [Examine FAQ](https://examine.com/conditions/muscle-size-and-strength/faq/what-happens-if-i-fall-off-the-gainz-train-how-much-exercise-is-needed-to-maintain-what-ive-built); [GetFitCraft detraining summary](https://getfitcraft.com/science/detraining-science)
- A coaching site derives a heuristic of "about a third of building volume" for maintenance in younger athletes, more for older; this is a derived number, not stated in the Spiering abstract — [Coach Athletics](https://coachathletics.com.au/coaching-education/ltad-srbj9)

**Detraining timelines (how long a bad stretch can last before it costs anything)**
- Jeff Nippard: "strength can be detrained for up to three weeks before noticeable decreases begin to occur"; regaining takes roughly half the length of the break — [Nippard blog](https://jeffnippard.com/blogs/news/how-to-get-your-gains-back-after-a-training-break)
- One week off: no measurable size loss; strength dips 3–7%, mostly neural, returning in 1–2 sessions; meaningful detraining after ~3–4 weeks of complete inactivity (citing a 2023 Sports Medicine review) — [SetGraph](https://setgraph.app/articles/does-a-week-off-the-gym-kill-your-gains); a 4-week full layoff cut 1RM ~6–9% in strength-trained men — [BarBend](https://barbend.com/?p=15087)

### Inferences (actionable rules)
- **Set a weekly set target per muscle/lift, not a per-session one.** The designer picks e.g. 12–16 hard sets/muscle/week for a 6-day week. On a 3-day week, redistribute: each session carries ~2x the sets per muscle, capped at ~6 direct sets per muscle per session (conservative, Henselmans) or ~10–11 fractional sets (preprint ceiling). Anything above the cap is dropped, not carried over.
- **If 3 days available:** full-body sessions; each muscle ~2–3 sets x 3 sessions for a floor of 6–9 sets/week; keep top-set loads unchanged. This sits above the maintenance floor (1 session/1 set) by a wide margin and at the ~10 sets/week line Nuckols cites, so it is a "slow-progress" week, not a maintenance week.
- **If 2 days available (emergency):** 1 heavy set per main movement pattern at normal working load + 1–2 back-off sets. Per Spiering this maintains for months; per PeerJ/Schoenfeld you lose little as long as the following weeks restore volume.
- **If 5–6 days available:** spread the same weekly set target thinner (fewer sets/session), which PeerJ suggests lowers per-session RPE and improves set quality; use the surplus sessions to add volume toward the upper end of the target, not to add new intensity.
- **Priority when cutting: keep intensity, cut volume.** Every maintenance source conditions its finding on relative load being kept. A compressed week should therefore keep the top set / heaviest work and drop back-off sets and accessories first.
- **A single bad week (≤7 days off) costs nothing measurable;** the design does not need make-up sessions, only a return to the rotation.

### Gaps
- No study directly tests week-to-week oscillation (3 days one week, 6 the next); all evidence is from steady-state frequency comparisons or sustained reduced-training periods. The applicability of volume-equated findings to oscillating schedules is an inference.
- Full text of Spiering 2021 and Bickel 2011 could not be read; older-adult results in Bickel are reported inconsistently by secondary sources.

---

## KQ4. Autoregulation tools (RPE/RIR, velocity, readiness) and how to use them when a week is compressed

### Takeaway
Barbell Medicine, Juggernaut and the research all treat RPE/RIR (and velocity) as the mechanism for absorbing schedule disruption: on a compressed or fatigued day you hold the prescribed RPE and let load fall, or you cap sets with an RPE stop. BBM coaches explicitly say a single session "has little impact on your trajectory," so the default on a bad day is lighter loads or pushing the session, not grinding.

### Cited Findings
- Barbell Medicine defines autoregulation as "selecting and adjusting training intensity based on your performance during a given training session," via RPE, RIR, or velocity-based training — [BBM: Autoregulation and RPE Part I](https://www.barbellmedicine.com/blog/autoregulation-and-rpe-part-i/)
- In a BBM forum thread where a lifter had to cram four training days into a week and felt unusually fatigued in warm-ups, the coach's reply: "what you do in a single session has little impact on your trajectory. You could've trained as planned using much lighter weights, or you could push the session off if you wanted to" — [BBM forum: Using RPE or adjusting the training schedule](https://forum.barbellmedicine.com/t/using-rpe-or-adjusting-the-training-schedule/19074)
- BBM coaches on overshooting RPE: it "is not a reason for great concern, it just provides you with further experience to help refine your choices in the subsequent week"; if you realise mid-session you overshot, finish the set and adjust load for subsequent sets; but "continuing to blindly add weight to the bar despite it clearly being unsustainable is not a smart way to train" — [BBM forum: How to progress while not exceeding capacity](https://forum.barbellmedicine.com/t/how-to-progress-while-not-exceeding-capacity-or-over-reaching-too-frequently/11314)
- BBM staff say training two days in a row on their 4-day templates is fine; many lifters run Mon/Tue/Thu/Fri — [BBM forum: Scheduling the press template](https://forum.barbellmedicine.com/t/scheduling-the-press-template/1237)
- An NSCA-accepted thesis/study on 12 powerlifters found "volume can be effectively autoregulated using RPE stops as a method to dictate number of sets performed" — [AUT repository: RPE volume autoregulation](https://openrepository.aut.ac.nz/bitstream/10292/12177/2/RPE%20volume%20autoregulation.pdf)
- JuggernautAI adapts via a "Readiness Rating System" pre-session, intra-session, session-to-session, week-to-week and block-to-block; a reviewer reports a high soreness score reduced load "for that workout only (not the entire strength block)" — [JuggernautAI App Store](https://apps.apple.com/app/id1515756471); [Garage Gym Reviews](https://garagegymreviews.com/juggernautai-review)
- Mike Israetel on mid-mesocycle fatigue: offers options ordered by fatigue level from "grind it out" (slightly higher fatigue than planned, or last accumulation week before deload; fix with more sleep/food) up to deload; "when you get really tired, take an easy week of training or no training at all" — [RP: Dr. Mike Israetel Compilation](https://rpstrength.com/blogs/articles/dr-mike-israetel-compilation)
- Nippard's comeback guidance: after a layoff, run compound lifts at RPE ≤5 (≥5 reps in reserve) in the introductory phase and avoid soreness, which "doesn't do anything extra for hypertrophy and just reduces your ability to perform and recover" — [Nippard blog](https://jeffnippard.com/blogs/news/how-to-get-your-gains-back-after-a-training-break)

### Inferences (actionable rules)
- **Prescribe top sets by RPE, not fixed percentage,** so a compressed week self-corrects: "work up to a single @8, then 2–4 back-off sets at −5–8%." When sessions are packed back-to-back, the @8 lands lighter and the week stays sustainable.
- **Use RPE stops for volume:** "do back-off sets until a set hits RPE 9, max N sets." This makes session length and total volume shrink automatically on a compressed/fatigued day and expand on a fresh 6-day week.
- **Readiness gate:** a simple pre-session check (sleep, soreness, warm-up velocity or how the first work-up set feels) → if poor, drop the day's volume by ~1/3 and keep the top set; do not change the plan for the rest of the block (mirrors the JuggernautAI "that workout only" behaviour).
- **After ≥2–3 weeks mostly missed:** treat the return week as a ramp (Nippard: RPE ≤5 compounds), not a continuation.

### Gaps
- No BBM, JTS or RP source found that gives an explicit rule for a *compressed week* (e.g., "4 sessions in 4 consecutive days → reduce back-offs by X"). The BBM forum reply is the closest, and it is a forum answer, not a published guideline.
- Velocity-based specifics (velocity-loss thresholds for a short week) were not found.

---

## KQ5. Rules for what to keep when sessions are cut, how to merge two sessions into one, and how to handle a skipped session mid-rotation

### Takeaway
Practitioner guidance converges on: keep the main compound/strength work, drop accessories and cardio first; merge sessions only when the two are compatible and not as back-to-back heavy days; and for a skipped session in a rotation, do not skip ahead, resume with the missed session next time you train.

### Cited Findings
- Built With Science: default is to continue the schedule; one or two missed workouts make little long-run difference; the alternative is to shift the missed session to the next day and push everything back (sacrificing a rest day) — [Built With Science help](https://help.builtwithscience.com/en/what-happens-if-i-miss-a-workout)
- Freeletics: skipped training days are moved to the next scheduled training day — [Freeletics forum](https://forum.freeletics.com/t/how-to-move-training-days-in-a-week/9058/6)
- Cathe forum consensus: shift the rotation forward so nothing is lost and weeks don't become lopsided; double up only when the sessions are compatible and "not on consecutive days" for the same body part; "I skip cardio workouts if I miss one. I don't skip strength training. I always go back to the body part I missed" — [Cathe forum 225177](https://cathe.com/forum/threads/what-do-you-do-when-missing-days-in-rotation.225177); [Cathe forum 197583](https://cathe.com/forum/threads/rotation-miss-a-day-do-you-do-double-the-next-day.197583); doubling two heavy sessions, especially leg days, is reported as too much — [Cathe forum 236190](https://www.cathe.com/forum/threads/what-do-you-do-when-you-miss-a-workout.236190)
- CTS (endurance coaching, generalisable): one or two missed sessions for ordinary reasons → carry on; longer gaps → ease back with lighter sessions — [TrainRight missed workouts guide](https://trainright.com/missed-workouts-guide-to-adjusting-training/)
- BBM 12-week strength and press templates run 4 days and "include a suggested modification for three days"; the 4-week Time Crunch is a 3-day program with no conditioning; the 6-day Endurance/GPP block "can be condensed by pairing lifting with conditioning sessions" — [BBM Template Overviews](https://forum.barbellmedicine.com/t/barbell-medicine-template-overviews/1534)
- BBM Beginner Prescription offers Standard/Foundational at 3 days, Express at 2 days — [BBM Beginner Prescription](https://www.barbellmedicine.com/the-beginner-prescription/)
- The T-Nation 5/3/1 2-day compression: all four lifts each week, heavy on two and supplemental-only on the other two, swapping the following week — [T-Nation thread](https://t-nation.com/t/leader-anchor-4-day-forever-templates-2-days-a-week/275860)
- Maintenance studies condition everything on keeping relative load (Spiering 2021) — [PubMed 33629972](https://pubmed.ncbi.nlm.nih.gov/33629972/)

### Inferences (actionable rules)
- **Keep order (priority stack) when cutting a session's content:** 1) the main compound top set(s) for the session's primary pattern; 2) the secondary compound (e.g., a press on a squat day) at reduced sets; 3) one pull/hinge balance movement; 4) isolation/accessory work; 5) conditioning. Cut from the bottom.
- **Merge rule:** Merge two consecutive rotation sessions only if their primary lifts don't share the same pattern (e.g., Upper + Lower → one full-body; Push + Pull → one upper). Take each session's top set at full load, halve each session's back-off/accessory sets, and cap the merged session at ~6 direct sets per muscle. Do not merge two heavy lower-body sessions.
- **Skipped mid-rotation:** next time you train, do the session you missed (the rotation never advances without a completed session). If more than ~7 days pass since that muscle group was trained, still do the session, but at the previous week's loads (no progression jump). If more than ~3 weeks pass, drop top sets to RPE ≤5–6 for the first exposure (Nippard).
- **Unbalanced-week guard:** in any week of ≤3 sessions, every session should include a squat/hinge, a press, and a pull, regardless of what the rotation label says (full-body collapse).

### Gaps
- No peer-reviewed or coach-published test of "merged" sessions versus separate sessions was found; the merge rules are synthesised from per-session volume ceilings and forum practice.
- Wendler's and LeFever's own missed-session rules remain unverified (see KQ2 gaps).

---

## KQ6. Keeping progression tracking when a lift's frequency changes between weeks

### Takeaway
The cited programs that tolerate variable frequency all key progression to **completed exposures** (sessions or waves) rather than calendar weeks: 5/3/1 bumps the training max after a completed 3-week wave of content however long it takes; GZCLP progresses load per completed session and changes rep scheme on failure; the r/Fitness BBR adds weight every session with a performance-based deload. RPE-based top sets (BBM) remove the need for a fixed schedule at all.

### Cited Findings
- 5/3/1: cycle length stretches with fewer days (4 weeks at 4 days/week, 5+ weeks at 3 days/week), meaning the percent-wave progression is per lift-exposure, not per calendar week — [Muscle & Strength](https://www.muscleandstrength.com/node/4458); Leader/Anchor blocks are counted in 3-week waves of content, with the 7th Week Protocol as a test/deload between them — [train531.com](https://train531.com/blog/531-forever/)
- GZCLP: load increases each time a tier's sets are completed; failure → rotate rep scheme (not weight reset); only after exhausting rep schemes do you reset/retest — [thefitness.wiki GZCLP](https://thefitness.wiki/routines/gzclp/); [Boostcamp GZCLP](https://boostcamp.app/cody-lefever/gzcl-program-gzclp)
- r/Fitness BBR: +2.5 lb upper / +5 lb lower per session, bigger jumps if the AMRAP exceeds 10 reps, −10% deload if fewer than 15 total reps across the sets — per-session, schedule-agnostic — [thefitness.wiki BBR](https://thefitness.wiki/routines/r-fitness-basic-beginner-routine/)
- BBM: progression is autoregulated by RPE; coaches advise refining load choices "in the subsequent week/training session" based on the last RPE result — [BBM forum 11314](https://forum.barbellmedicine.com/t/how-to-progress-while-not-exceeding-capacity-or-over-reaching-too-frequently/11314)
- JuggernautAI adjusts load for that workout only when readiness is poor; block-level progression continues — [Garage Gym Reviews](https://garagegymreviews.com/juggernautai-review)
- Detraining evidence: ≤1 week off costs ~3–7% strength, neural, recovered in 1–2 sessions; noticeable loss begins after ~3 weeks — [SetGraph](https://setgraph.app/articles/does-a-week-off-the-gym-kill-your-gains); [Nippard blog](https://jeffnippard.com/blogs/news/how-to-get-your-gains-back-after-a-training-break)

### Inferences (actionable rules)
- **Index progression by exposure count, not week number.** Store for each main lift: last load, last top-set reps/RPE, exposure counter. Advance the lift's progression step when its exposure succeeds, regardless of whether that took 4 days or 11.
- **Days-since-last-exposure modifier:** ≤7 days → normal progression; 8–14 days → repeat last load (no increase); 15–21 days → repeat last load with one fewer back-off set; >21 days → reduce 5–10% and ramp over two exposures (consistent with the 3-week detraining line and the 4-week ~6–9% 1RM loss).
- **Use RPE-anchored top sets** to make the above self-correcting: if the planned load comes in ≥1 RPE harder than prescribed after a gap, hold load next exposure; if it comes in easier on a 6-day week, take the next step.
- **Wave/block progression:** count a "wave" as N completed exposures per lift (e.g., 3), not 3 weeks. A 6-day week may finish a wave in one calendar week; a 3-day week in two.

### Gaps
- No source quantifies progression adjustments by days-since-last-exposure; the modifier table is an inference from detraining timelines.

---

## KQ7. Published or community "flexible template" programs (Boostcamp/Lift Vault 3–6-day, Nippard minimalist, BBM variable-day, RP app)

### Takeaway
I found no commercially published program that formally scales 3↔6 days within one plan. What exists: (a) fixed-day-count programs sold in several day-count variants (RP physique templates 3–6 days, BBM 2/3/4/6-day templates); (b) apps that reschedule rather than rescale (Boostcamp); (c) an RP app whose day count is chosen at mesocycle setup and, per a community thread title, cannot be changed mid-mesocycle; (d) a 2-day "minimalist" line from Nippard and RP.

### Cited Findings
- **Boostcamp**: library filters programs by days/week (2–6); programs list a single fixed frequency; the app lets you reschedule sessions if your week doesn't go to plan — [Boostcamp program library](https://www.boostcamp.app/features/program-library)
- **RP templates**: male/female physique templates are offered for 3 to 6 days per week; simplified physique templates for 2 to 4 — [third-party description of RP templates, Scribd](https://www.scribd.com/document/796915322/Rp-Strength-Male-Physique-Template) (low-quality source; verify on rpstrength.com)
- **RP Hypertrophy app**: the help centre has articles titled "How many days per week should I choose to train?" and "How can I change the length of my training cycle?" (content not retrieved) — [RP Help Center: Navigating the App](https://help.rpstrength.com/hc/en-us/sections/30801323964183-Navigating-the-App); r/RPHypertrophy has a popular thread titled "Can't change Workout days once I start a mesocycle?" (replies not retrieved) — [GummySearch r/RPHypertrophy index](https://gummysearch.com/r/RPHypertrophy/); RP announced a "Meso Builder" for full customisation — [RP blog](https://rpstrength.com/blogs/podcasts/major-updates-to-the-rp-diet-hypertrophy-apps-rp-strength)
- **RP minimalist**: a Boostcamp listing titled "Minimalist Training – Renaissance Periodization" exists — [Boostcamp](https://www.boostcamp.app/users/Kru4CY-minimalist-training-renaissance-periodization)
- **Barbell Medicine**: 12-week Strength and Press templates = 4 days with a 3-day modification; Time Crunch = 3 days; Endurance/GPP = 6 days, condensable; Beginner Prescription Standard/Foundational = 3 days, Express = 2 days; BBM now calls templates "training programs," described as adaptable to time availability — [BBM Template Overviews](https://forum.barbellmedicine.com/t/barbell-medicine-template-overviews/1534); [BBM Beginner Prescription](https://www.barbellmedicine.com/the-beginner-prescription/); [BBM training programs](https://www.barbellmedicine.com/product-category/training-templates/)
- **Jeff Nippard**: a Boostcamp "science based minimalist workout" listing describes 2 days/week, ≤45-minute sessions; a separate user-created "Jeff Nippard Minimalist Program" listing shows 4 sessions/week of ~20 minutes (not Nippard's own material); sources conflict and none is authoritative — [Boostcamp listing A](https://www.boostcamp.app/users/AhlMNp-jeff-nippard-science-based-minimalist-workout); [Boostcamp listing B](https://www.boostcamp.app/users/LGgbWn-jeff-nippard-minimalist-program). Nippard's free 4-week Comeback Program is a 4-day upper/lower bridging detraining back to normal training — [Nippard Comeback Program](https://jeffnippard.com/comeback-program/)
- **5/3/1**: official claim of fitting 2, 3 or 4 days; "The Twice A Week" template in Wendler's templates eBook — [jimwendler.com](https://www.jimwendler.com/products/5-3-1-second-edition-ebook); [EliteFTS](https://elitefts.com/products/training-templates-by-jim-wendler-ebook)
- **JuggernautAI**: adapts loads by readiness; no evidence found that it rescales the week when sessions are missed — [JuggernautAI App Store](https://apps.apple.com/app/id1515756471)
- **Weightology** publishes a "2–3 Day Per Week Whole Body Basic Hypertrophy Plan" using ABA/BAB alternation — [Weightology](https://weightology.net/?p=7759)
- **Dan John** "minimalist training" 2-day approach is referenced by forum users as the classic 2-day template — [danjohn.net (link cited in forum)](http://danjohn.net/2011/01/minimalist-training/)

### Inferences
- Because no off-the-shelf plan scales 3↔6, the designer should build one from the components with the strongest support: (1) rotation-ordered sessions; (2) weekly set targets per muscle with per-session caps; (3) RPE-anchored top sets and RPE-stop back-offs; (4) exposure-indexed progression; (5) a full-body collapse rule for ≤3-day weeks.
- The RP app's apparent mid-meso lock on day count is a useful anti-pattern: a flexible plan must choose day count per week (or per session), not per block.

### Gaps
- Could not read the RP help articles or the r/RPHypertrophy thread, so RP's actual rule on changing days is unconfirmed.
- No Lift Vault page describing a "3–6 day" program surfaced; Lift Vault results were limited to 5/3/1 spreadsheets.
- Nippard's official minimalist program page was not retrieved; frequency options are unverified.

---

## Consolidated "if X days available, do Y" rule set (synthesis; each rule's support is cited in the sections above)

| Days this week | Structure | Per-session content | Volume rule | Intensity rule | Support strength |
|---|---|---|---|---|---|
| 2 | Full body x2 (rotation A/B) | 1 squat/hinge, 1 press, 1 pull; top set + 1–2 back-offs each | ~1/3 of normal weekly sets; floor = 1 hard set per pattern | Keep normal top-set load/RPE | Strong (Spiering 2021; Bickel 2011) |
| 3 | Full body x3 (rotation A/B/C) or collapsed U/L | Top set per primary pattern + back-offs; 1–2 accessories | ~60–75% of 6-day weekly sets; cap ~6 direct sets/muscle/session | Keep top-set load; cut back-offs first | Strong (Schoenfeld 2019 volume-equated; per-session ceiling data) |
| 4 | Upper/Lower rotation (U-L-U-L) | Standard | ~85–100% of weekly target | Normal | Strong |
| 5 | PPL rotation continuing (P-P-L-P-P, next week L-P-P-L-P) or U/L + 1 | Standard | 100% of target | Normal | Moderate (practitioner floating split; volume-equated evidence) |
| 6 | PPL x2 or U/L x3 | Fewer sets per session, same weekly total; use surplus for extra accessory volume, not extra heavy top sets | 100% of target, spread thin | Normal; expect lower per-session RPE (PeerJ 2021) | Moderate |
| Skipped session mid-rotation | Resume at missed session | — | — | ≤7 days gap: normal; 8–21 days: hold load; >21 days: −5–10% and RPE ≤5–6 first exposure | Moderate (detraining timelines) |

**Where recommendations conflict:**
- *Per-session set ceiling*: ~6 sets/muscle (Henselmans/Krieger informal) vs ~11 fractional sets (preprint). The preprint is the more systematic analysis but uses fractional counting; for direct hard sets on a compound, 6–8 is the safer planning cap.
- *Frequency per se*: Norwegian Frequency Project (6x > 3x in powerlifters, volume-equated) vs Schoenfeld 2019 and PeerJ 2021 (no effect). The meta-analytic evidence (25 studies) has stronger support; the Norwegian result is a single unpublished-in-full study in a specific population and is best read as "higher frequency can improve set quality at very high volumes."
- *Older adults' maintenance dose*: Spiering says 2 sessions, 2–3 sets; Bickel secondary summaries disagree on whether older adults maintained size at all. Spiering (a review) is the better guide.
- *Missed-session make-up*: app help centres default to "skip and continue the calendar"; rotation practitioners default to "never skip, resume the sequence." For a program built as a rotation, the latter is internally consistent and avoids lopsided weeks (the specific harm the Huberman/Cavaliere summaries flag for U/L splits).
