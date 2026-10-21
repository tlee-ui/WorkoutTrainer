# Lifting Splits and Named Training Programs, Organized by Days per Week

Research notes for the WorkoutTrainer program designer. Method note: in this environment WebFetch could not resolve any host (thefitness.wiki, stronglifts.com, jimwendler.com, liftosaur.com, liftvault.com, startingstrength.com, strongerbyscience.com, boostcamp.app all returned DNS/proxy errors), so every finding below comes from search-result snippets of the linked pages rather than full page reads. Numbers were only recorded when a snippet stated them; anything I could not confirm is listed under Gaps rather than guessed. Primary-author pages are cited where the search surfaced them; otherwise the best available mirror (Boostcamp, Lift Vault, Liftosaur, Jefit) is cited and labelled as secondary.

---

## Key Question 1: How do the generic splits compare (full body, upper/lower, PPL, PPL+UL hybrids, bro split, Arnold split) on per-muscle frequency and session length?

### Takeaway
Per-muscle frequency is set almost entirely by how many days you train and which split you pick: full body hits everything every session (2-4 days), upper/lower gives ~2x/week on 4 days, PPL gives 1x/week on 3 days and 2x/week on 6 days, the Arnold split gives 2x/week on 6 days, and a classic one-body-part-per-day "bro" split gives 1x/week. The research base (Schoenfeld 2016 and the 2019 volume-equated update, as read by Stronger By Science) favors at least 2x/week per muscle, but the volume-equated advantage of higher frequency is small.

### Cited Findings
**Full body**
- Full-body training suits 2 to 4 days a week, trains each muscle every session, runs about 45-70 minutes per session, with 2-6 sets per muscle per session — [GetFitCraft](https://getfitcraft.com/guides/full-body-vs-split-workout)
- Beginners often start with full body; upper/lower suits four-day schedules — [Arvo training splits](https://arvo.guru/resources/training-splits)

**Upper/lower (4 days)**
- The usual 4-day upper/lower layout hits each muscle about twice weekly; sessions run about 45-60 minutes — [FindYourEdge U/L](https://www.findyouredge.app/news/upper-lower-split-for-beginners-uk-2026)
- Upper/lower is described as the default four-day choice — [Speediance](https://www.speediance.com/blogs/strength-programming/upper-lower-vs-ppl-4-day)

**Push/pull/legs (3 or 6 days)**
- PPL usually needs 6 days to reach twice-weekly frequency; on 3 days each muscle is trained once a week — [FindYourEdge PPL vs full body](https://www.findyouredge.app/news/push-pull-legs-vs-full-body-beginners-uk-2026)
- PPL fits lifters who can train 5 or 6 days and want more volume per muscle; sessions typically 40-60 minutes — [GetFitCraft](https://getfitcraft.com/guides/full-body-vs-split-workout); another source gives 45-75 minutes — [FindYourEdge U/L](https://www.findyouredge.app/news/upper-lower-split-for-beginners-uk-2026)

**Arnold split (6 days) and bro split**
- With the Arnold split you work out six days per week and train each muscle group twice per week; common layout Mon Chest/Back, Tue Shoulders/Arms, Wed Legs, Thu Chest/Back, Fri Shoulders/Arms, Sat Legs, Sun off; a variant inserts a rest day after legs making an eight-day cycle — [Muscle Evo](https://muscleevo.net/arnold-split/); [Fitbod](https://fitbod.me/blog/arnold-split/); [FitnessVolt Arnold vs PPL](https://fitnessvolt.com/arnold-split-vs-ppl/)
- Sources call it advanced; one says it should only be done by lifters training at least two years; beginners may do each of the three workouts once per week (3 days, each muscle 1x) as a modification — [Muscle Evo](https://muscleevo.net/arnold-split/); [Fitbod](https://fitbod.me/blog/arnold-split/)
- An "Arnold x Upper Lower" 5-day variant exists for late-intermediate/advanced lifters — [FitnessVolt Arnold vs PPL](https://fitnessvolt.com/arnold-split-vs-ppl/)
- Classic Bodybuilding.com body-part programs: Jim Stoppani's Shortcut to Size is listed as 4 workouts/week, 45-60 min per workout, level "beginner" — [Bodybuilding.com 10 most popular](https://bodybuilding.com/fun/our-10-most-popular-workout-programs.html); a third-party review describes it as a 4-day body-part split in three 4-week phases — [Lift Vault Shortcut to Size](https://liftvault.com/programs/bodybuilding/shortcut-to-size-program-spreadsheet/)

**Frequency evidence**
- Stronger By Science reads Schoenfeld's 2016 frequency meta-analysis as favoring training a muscle at least twice a week over once, with too little evidence about higher frequencies — [Stronger By Science, frequency](https://www.strongerbyscience.com/frequency/)
- SBS's own hypertrophy-specific pooled analysis: overall effect trivial (d = 0.113; CI 0.07-0.16); lower-frequency groups grew 0.42%/week vs 0.58%/week for higher-frequency groups — [Stronger By Science, frequency-muscle](https://www.strongerbyscience.com/frequency-muscle/)
- Secondary write-ups of the 2019 Schoenfeld/Grgic/Krieger update: when weekly sets were matched, higher frequency still gave somewhat more growth but the difference was smaller — [Bony to Beastly](https://bonytobeastly.com/how-often-should-you-train-each-muscle-group/); [Bodybuilding.com](https://amp.bodybuilding.com/content/the-science-of-training-frequency.html)
- A 2019 pooled analysis of volume-matched studies found no significant hypertrophy difference between low and high frequencies (secondary source) — [GetFitCraft](https://getfitcraft.com/guides/full-body-vs-split-workout)
- PHUL's and PHAT-style twice-weekly layouts are justified by their authors on the idea that muscle protein synthesis stays elevated up to ~48 hours after training — [Hevy PHUL](https://www.hevyapp.com/phul-power-hypertrophy-upper-lower/); [Liftosaur PHAT](https://www.liftosaur.com/programs/phat)

### Inferences
- Frequency table a designer can use (derived from the cited layouts): Full body 2x/wk = each muscle 2x; Full body 3x = 3x; Upper/Lower 4x = 2x; PPL 3x = 1x; PPL 6x = 2x; PPL + Upper/Lower 5x = ~2x (every muscle hit once in the PPL block and once in the U/L block); Arnold 6x = 2x; one-body-part-per-day bro split 5x = 1x.
- Session length rises as frequency falls for the same weekly volume: full-body days must carry every muscle's sets (so 45-70 min at modest per-session volume), while PPL/U-L days can be shorter per session but need more days. For a time-boxed app, cap full-body sessions by limiting per-muscle sets per session (2-6 per the GetFitCraft figure) rather than by cutting muscles.

### Gaps
- I found no primary-source definition or session-length data for the PPL + Upper/Lower 5-day hybrid; its 2x/week frequency is derived, not cited.
- No source gave a canonical exercise list or set/rep scheme for a generic "bro split"; only the Bodybuilding.com-type programs above are documented.
- The Arnold Blueprint (Bodybuilding.com) did not appear in results; days per week unconfirmed.

---

## Key Question 2: What can I do with 2-3 days per week? (Full-body linear progressions and 3-day strength programs)

### Takeaway
The 3-day slot is dominated by full-body barbell linear progressions (Starting Strength, StrongLifts 5x5, Greyskull LP, GZCLP run 3x) for novices and by the Texas Method / Madcow 5x5 for intermediates; 5/3/1 has official 2-day and 3-day templates, and Reddit PPL and the Arnold split can be run as 3-day/1x-frequency fallbacks.

### Cited Findings
**Starting Strength (Mark Rippetoe; book "Starting Strength: Basic Barbell Training", 3rd ed.) — 3 days, full body, novice strength**
- Two alternating full-body workouts, 3 days a week: squat every session (3x5), pressing alternates bench and overhead press (3x5), deadlift is a single heavy set of 5; add weight every workout — [Barbell Logic Novice LP](https://barbell-logic.com/starting-strength-novice-linear-progression/) / [FitnessVolt Starting Strength](https://fitnessvolt.com/powerlifting/programs/starting-strength/)
- Increments cited: add 5 lb every session to squat, bench and press; 10 lb per session to deadlift while it advances, dropping to 5 lb as progress slows; another guide gives 2.5-5 kg per session for squat and deadlift — [FitnessVolt SS calculator](https://fitnessvolt.com/rpe-training/programs/starting-strength/); [FitnessVolt SS LP](https://fitnessvolt.com/starting-strength-lp/)
- Stall rule as summarized: after failing all reps at the same weight 3 sessions in a row, reset that lift ~10% and build back up — [FitnessVolt SS LP](https://fitnessvolt.com/starting-strength-lp/)
- Phases: one guide describes four phases (foundations/technique; power cleans added; chin-ups added with gradually rising intensity, the longest phase; an advanced-novice stage with a lighter squat session plus heavy squats twice a week); phase boundaries are not standardized across sources — [FitnessVolt SS LP](https://fitnessvolt.com/starting-strength-lp/)
- Book wording quoted on the official forum: after two or three more weeks, chin-ups can be added as "the only really useful assistance exercise"; a forum poster quoting the 3rd edition says Phase 3 adds chin-ups after power cleans on day B — [Starting Strength forum, Phase 2 chin-ups](https://startingstrength.com/resources/forum/general-programming/89979-phase-2-chin-ups-addition.html); Liftosaur's Phase 3 instead alternates deadlift and power clean (5x3) with chin-ups 3x10 — [Liftosaur SS3](https://www.liftosaur.com/programs/ss3) (conflict; the book is primary)
- Duration: one review puts the novice program at about 12-16 weeks, low volume, high intensity — [FitnessVolt SS LP](https://fitnessvolt.com/starting-strength-lp/)
- Status: paid book; official program page exists at [startingstrength.com/get-started/programs](https://startingstrength.com/get-started/programs) (could not be read in this environment).

**StrongLifts 5x5 (Mehdi, stronglifts.com) — 3 days, full body, novice strength**
- Workout A: squat, bench press, barbell row, all 5x5. Workout B: squat 5x5, overhead press 5x5, deadlift 1x5. Alternate A/B across three sessions a week — [FitnessVolt StrongLifts](https://fitnessvolt.com/rpe-training/programs/stronglifts-5x5/); [Boostcamp StrongLifts copy](https://www.boostcamp.app/users/JYFbC3-stronglifts-5x5-assistance-work)
- Progression: +2.5 kg per workout for upper body, +5 kg for deadlift ([LiftStrong app listing](https://apps.apple.com/app/id6761501280)); FitnessVolt gives +5 lb every workout and +10 lb on deadlift ([FitnessVolt StrongLifts](https://fitnessvolt.com/rpe-training/programs/stronglifts-5x5/)). 2.5 kg and 5 lb are the same increment; the deadlift increment (5 kg vs 10 lb) is the real discrepancy.
- Deload: if you fail three workouts in a row at the same weight, reduce that exercise by 10%; only the failed lift is deloaded — [Boostcamp StrongLifts copy](https://www.boostcamp.app/users/JYFbC3-stronglifts-5x5-assistance-work); [Lowyat forum](https://forum.lowyat.net/topic/3240638)
- Status: free program; official app (stronglifts.com) — paid-tier details not retrieved.

**Greyskull LP (John Sheaffer) — 3 days, full body, novice strength/size**
- Mon/Wed/Fri; Press and Squat on Mon and Fri, Bench and Deadlift on Wed; the "1x5+" top set is the trademark (do at least five quality reps); start with a weight you can lift for 8-10 reps; +2.5 lb per session upper, +5 lb lower; Greyskull Reset = 10% reduction next session — [Powerlifting Technique, Greyskull LP](https://powerliftingtechnique.com/greyskull-lp/)
- Phrak's Greyskull variant: 3 non-consecutive days, two alternating A/B workouts — [Liftosaur Phrak's Greyskull](https://www.liftosaur.com/programs/phrakgreyskull)
- Status: book ("The Greyskull LP"); Phrak's variant free on r/Fitness.

**GZCLP (Cody Lefever) — 3 or 4 days, novice strength** (details in KQ3; run on 3 days by rotating the four workouts)
- Boostcamp hosts the Cody-partnered GZCLP — [Boostcamp GZCLP](https://www.boostcamp.app/coaches/cody-lefever/gzcl-program-gzclp)

**Texas Method (Glenn Pendlay / Mark Rippetoe, "Practical Programming") — 3 days, full body, early intermediate strength**
- Three-day weekly template: high-volume 5x5 day, light recovery day, intensity day aiming for a new 5-rep PR; progress is weekly, not per session — [Powerlifting Technique, TM vs Madcow](https://powerliftingtechnique.com/texas-method-vs-madcow-5x5/); [Barbell Logic, TM explained](https://barbell-logic.com/the-texas-method-explained/)
- The intensity day is balanced with a cluster of 5-rep sets on Monday (think 5x5) at about a 10% reduction in load — [Starting Strength, TM intensity day](https://startingstrength.com/article/understanding-the-texas-method-intensity-day)
- Increments: ~5 lb/week on squat; ~5 lb per PR session on bench and press (each every 2 weeks since they alternate) — [Powerlifting Technique](https://powerliftingtechnique.com/texas-method-vs-madcow-5x5/)
- Stall handling: when weekly 5 lb jumps can't be sustained on volume day, change 5x5 to 6x4 or 8x3 — [Barbell Logic](https://barbell-logic.com/the-texas-method-explained/); on intensity day, cycle 2x3, 3x2, 2x2, 5 singles, then return to a new 5RM — [Barbell Logic](https://barbell-logic.com/the-texas-method-explained/) / [Starting Strength article](https://startingstrength.com/article/understanding-the-texas-method-intensity-day); Liftosaur suggests trimming Monday 5x5 to 4x5 or 3x5 before dropping volume-day weight — [Liftosaur Texas Method](https://www.liftosaur.com/programs/texasmethod)
- Status: book (Practical Programming for Strength Training); widely reproduced for free.

**Madcow 5x5 (forum user "Madcow", based on Bill Starr) — 3 days, full body, intermediate strength**
- Ramping sets rather than straight sets; default set interval 12.5% between ramp sets — [StrongLifts Madcow guide](https://stronglifts.com/madcow-5x5/workout-guide); [StrongLifts Madcow interval](https://stronglifts.com/madcow-5x5/interval)
- Monday ramps to a top 5x5; Wednesday is lighter (Squat 4x5 with a deadlift variant 4x5 in the StrongLifts table; another source says only two sets of 5 at 75%); Friday "Workout C" Squat 4x5, 1x3, 1x8 (ramp to a top triple PR plus a back-off 8) — [StrongLifts Madcow guide](https://stronglifts.com/madcow-5x5/workout-guide); [FitnessVolt Madcow](https://fitnessvolt.com/madcow-5x5/)
- Madcow uses more total sets across the week than the Texas Method — [Powerlifting Technique](https://powerliftingtechnique.com/texas-method-vs-madcow-5x5/)
- Top set is scaled from 1RM at ~87.5% (a typical 5RM) in generators — [FitnessVolt Madcow](https://fitnessvolt.com/madcow-5x5/)
- Review warns many online write-ups oversimplify Madcow — [Character Strength review](https://characterstrength.co.uk/?p=4336)
- Status: free (originally a forum post / geocities page).

**5/3/1 on 2 or 3 days (Jim Wendler)**
- Wendler's "Training Templates" eBook contains 14 templates including "3 Days Per Week (The origin of 5/3/1)" and "The Twice A Week" — [EliteFTS, Training Templates by Jim Wendler](https://elitefts.com/products/training-templates-by-jim-wendler-ebook)
- On a 3-day version you rotate the 4 core workouts; a mesocycle lasts 4 weeks at 4 days/week and 5+ weeks at 3 days/week — [Muscle & Strength 5/3/1 guide](https://www.muscleandstrength.com/node/4458)
- A 2-day user layout: bench + squat on one day, press + deadlift on the other — [Starting Strength forum, Wendler 2-day](https://startingstrength.com/resources/forum/general-programming/57773-5-3-1-a.html)
- Boostcamp hosts a 3-day "5/3/1 Full Body 1000% Awesome" template — [Boostcamp 5/3/1 full body](https://www.boostcamp.app/users/h6oNsc-531-full-body-1000percent-awesome)
- Core 5/3/1 numbers are in KQ3.

**Reddit PPL as a 3-day program** — "Can't train 6 days: run it as a 3-day program (Pull, Push, Legs)" — [Liftosaur Metallicadpa PPL](https://www.liftosaur.com/programs/metallicadpappl)

**Sheiko intermediate cycles — 3 days** (details in KQ3/KQ6): community app pages list the intermediate versions at 3 training days per week — [Boostcamp Sheiko intermediate medium load](https://www.boostcamp.app/users/N2vPAO-sheiko-intermediate-medium-load)

### Inferences
- For a 3-day app template, the cleanest novice option is an A/B full-body alternation (SS/SL/Greyskull pattern: 2 workouts, 3 slots/week, so each workout appears 3 times per fortnight); the cleanest intermediate option is a role-per-day week (volume / recovery / intensity, TM pattern) because it ties progression to the calendar week rather than to each session.
- 5/3/1 on 3 days behaves as a 4-workout rotation across a 5+ week cycle; the app must track "workout index" independently of calendar week.

### Gaps
- Official Starting Strength program text (startingstrength.com/get-started/programs) could not be read; phase definitions above are from secondary guides and one forum quote of the book.
- StrongLifts' rule for switching to 3x5 / 3x3 / 1x5 after repeated deloads was not found in any result.
- Madcow's weekly progression percentage (commonly stated as 2.5%/week) was not confirmed by any source surfaced; only the 12.5% ramp interval was.
- The exact Texas Method prescription (e.g., Monday 5x5 at 90% of Friday, Wednesday 2x5 at ~80%) was not stated in snippets beyond the "about a 10% reduction" line from Starting Strength.
- Wendler's exact 2-day template contents (and whether the "I don't have a set schedule" wording is from Beyond 5/3/1 or 5/3/1 Forever) were not found; see KQ7.

---

## Key Question 3: What can I do with 4 days per week? (Upper/lower and 4-day strength programs)

### Takeaway
Four days is the richest slot: 5/3/1 (one main lift per day, including Boring But Big and the Forever leader/anchor system), GZCLP's native 4-workout layout, nSuns 4-day, PHUL, Lyle McDonald's Generic Bulking Routine, Candito's 6-week program, the Juggernaut Method base template, and Nippard's Fundamentals upper/lower track all live here.

### Cited Findings
**5/3/1 core (Jim Wendler; books "5/3/1", "Beyond 5/3/1", "5/3/1 Forever") — 4 days, one main lift per day (squat, bench, deadlift, press), intermediate+ strength**
- Four-week wave from a training max: Week 1 65%/75%/85% x 5/5/5+; Week 2 70%/80%/90% x 3/3/3+; Week 3 75%/85%/95% x 5/3/1+; Week 4 deload 40%/50%/60% x 5, no AMRAP; last set of weeks 1-3 is AMRAP — [Lift Vault 5/3/1 calculator](https://liftvault.com/resources/531-calculator/); [thefitness.wiki 5/3/1 primer](https://thefitness.wiki/5-3-1-primer/); [GymNote 5/3/1 percentages](https://www.gymnoteplus.com/blog/531-workout-program)
- Training max default 90% of true 1RM; most variants use 85% or 90% — [Strength Insider 5/3/1](https://strengthinsider.com/workout-programs/531-program/)
- After each cycle add 5 lb to upper-body training maxes and 10 lb to lower-body — [Hardy app, start 5/3/1](https://hardy.app/guides/start-531-program)
- When you consistently miss prescribed minimum reps, cut the training max 10% and rebuild — [Strength Insider](https://strengthinsider.com/workout-programs/531-program/)
- The deload week is treated as optional by some — [Ironmaster 5/3/1](https://ironmaster.com/blog/2026/03/25/the-5-3-1-program)

**5/3/1 Boring But Big (supplemental template)**
- BBB = 5 sets of 10 reps with a lighter weight after the main lift; on squat day the 5x10 can be deadlift and vice versa ("flip side") — [Jim Wendler, Boring But Big](https://www.jimwendler.com/blogs/jimwendler-com/101077382-boring-but-big)
- BBB 3-Month Challenge: 50% of TM for cycle 1, 60% in month 2, 70% in month 3 — [Jim Wendler, BBB 3 Month Challenge](https://jimwendler.com/blogs/jimwendler-com/boring-but-big-3-month-challenge)
- Other Wendler posts give 50-60% of TM for the 5x10 ("the whole goal is to get 5 sets of 10"), a cycle 1 at 30-50% of TM, and advise beginners to start around 30% of TM — [Jim Wendler, BBB and Really Sore](https://www.jimwendler.com/blogs/jimwendler-com/101082438-boring-but-big-and-really-sore); [Jim Wendler, Boring But Big](https://www.jimwendler.com/blogs/jimwendler-com/101077382-boring-but-big)
- Boring But Strong (BBS) variant exists on Wendler's site — [Jim Wendler, Boring But Strong challenge](https://www.jimwendler.com/2014/07/boring-but-strong-challenge/); [Lift Vault BBS](https://liftvault.com/resources/boring-but-strong/)

**5/3/1 Forever (leader/anchor)**
- Listed at 4 days/week; a leader block typically runs as two three-week waves of higher-volume supplemental work (e.g., BBB), an anchor block is one three-week wave of higher-intensity work (e.g., First Set Last, Widowmaker) — [LiftProof 5/3/1 Forever](https://www.liftproof.app/programs/531-forever/)
- The book contains over 50 templates — [AbeBooks listing, 5/3/1 Forever](https://www.abebooks.com/Title-531-Forever-Simple-Effective-Programming/31945876298/bd)
- A common community pairing: Leader = 5s PRO + BBB, Anchor = 3/5/1 + 5x5 FSL — [Dr Workout 5/3/1 spreadsheets](https://www.drworkout.fitness/531-excel-spreadsheets/)
- Running Forever templates on 2 days: forum advice is to go heavy on 2 lifts and do supplemental work for the other 2, swapping the next week; others ran the 4 lifts over 9 days — [T-Nation, Forever templates 2 days a week](https://t-nation.com/t/leader-anchor-4-day-forever-templates-2-days-a-week/275860)
- Status: books are paid (5/3/1 Forever, Beyond 5/3/1, Training Templates eBook); core percentages are free on jimwendler.com and widely mirrored.

**GZCLP (Cody Lefever) — 4 workouts (A1/A2/B1/B2), run 3 or 4 days, novice strength**
- T1 ladder: 5x3+ → 6x2+ → 10x1+, staying at the same weight between stages; on a miss you don't lower the weight, you move to the next stage; last set AMRAP; minimum reps 15 / 12 / 10 per stage — [Massiv GZCLP progression](https://massiv.app/blog/gzclp-progression/); [GymNote GZCLP](https://www.gymnoteplus.com/blog/gzclp-workout-program); [RepCheck GZCLP guide](https://repcheckapp.com/blog/gzclp-guide)
- After failing 10x1+, sources diverge: test a new 5RM and restart at ~85-90% of it; or take the last clean 5x3 weight + 5-15 lb; or deload 15% and restart 5x3+ — [Massiv](https://massiv.app/blog/gzclp-progression/); [GymNote](https://www.gymnoteplus.com/blog/gzclp-workout-program); [Virtus GZCLP](https://virtusapp.ai/blog/gzclp-program-guide/) (conflict noted)
- T2 ladder: 3x10 → 3x8 → 3x6; after a 3x6 failure reset to 3x10 at a little more than the last 3x10 weight — [Massiv](https://massiv.app/blog/gzclp-progression/)
- T3 volume listed as 45+ total reps in the GZCLP table — [r/gzcl wiki mirror](https://reddit.sudovanilla.org/r/gzcl/wiki/GZCL)
- Official hosted version — [Boostcamp GZCLP (Cody Lefever)](https://www.boostcamp.app/coaches/cody-lefever/gzcl-program-gzclp); Cody's current writing is at [gzcl.substack.com](https://gzcl.substack.com/p/p-zero)
- Status: free.

**nSuns 531 LP 4-day (Reddit user nSuns) — 4 days, upper/lower-ish, late-novice/intermediate strength**
- Variants: 4 days/week (best for those new to nSuns), 5 days/week (after 2-3 months of nSuns), 6-day squat- or deadlift-focus versions; the 4-day version is essentially an upper/lower split; training max ~90% of 1RM — [Boostcamp nSuns guide](https://boostcamp.app/nsuns-531-powerlifting-program)
- The 6-day squat and deadlift versions program that lift 3 times per week instead of 2 — [Lift Vault nSuns spreadsheets](https://liftvault.com/programs/powerlifting/n-suns-lifting-spreadsheets/)
- Progression by reps on the T1 "1+" set: 0-1 reps no increase, up to >5 reps = +10-15 lb to training max — [Muscle Evo nSuns](https://muscleevo.net/nsuns-program/); typical 2-3 reps → +5 lb/week; T2 +5 lb upper / +10 lb lower; if stuck at 1 rep or failing, reduce 1RM 10% and rebuild — [Liftosaur nSuns](https://www.liftosaur.com/programs/nsuns)
- Status: free spreadsheets (Lift Vault) and free on Boostcamp.

**PHUL — Power Hypertrophy Upper Lower (Brandon Campbell, published on Muscle & Strength) — 4 days, upper/lower, intermediate powerbuilding**
- Created by Brandon Campbell — [Hevy PHUL](https://www.hevyapp.com/phul-power-hypertrophy-upper-lower/); original — [Muscle & Strength PHUL](https://www.muscleandstrength.com/workouts/phul-workout)
- Layout: Upper Power, Lower Power, rest, Upper Hypertrophy, Lower Hypertrophy, two rest days (Mon/Tue power, Thu/Fri hypertrophy) — [Hevy](https://www.hevyapp.com/phul-power-hypertrophy-upper-lower/); [Liftosaur PHUL](https://www.liftosaur.com/programs/phul)
- Power days: heavy compounds 3-5 reps; hypertrophy days 8-12 reps ([Liftosaur](https://www.liftosaur.com/programs/phul)) or 8-15 reps with isolation work ([Lift Vault PHUL](https://liftvault.com/programs/bodybuilding/phul-spreadsheet/)); each muscle 2x/week; main lifts squat, bench, deadlift, OHP plus isolation (leg extensions, leg curls, seated calf raises at 8-15) — [Boostcamp PHUL](https://www.boostcamp.app/coaches/brandon-campbell/phul-4-day-split)
- Status: free.

**Lyle McDonald Generic Bulking Routine — 4 days upper/lower, intermediate hypertrophy**
- Mon/Tue/Thu/Fri; intermediate (1-3 years); 6-8 week cycles ending with a 2-week deload; target gain ~0.5-1 lb/week; first weekly session of each half 3-5x5 (strength), second 3x8-12 (hypertrophy); a recovery option uses 2-3x6-8 compounds and 1-2x10-12 secondaries; set counts flexible within range — [Liftosaur Lyle GBR](https://www.liftosaur.com/programs/lylegenericbulking); [Lift Vault Lyle GBR](https://liftvault.com/programs/bodybuilding/lyle-mcdonald-bulking-workout-routine-spreadsheet/)
- Status: free (forum post).

**Candito 6-Week Strength Program (Jonnie Candito) — 4 days nominal, frequency varies by week, intermediate powerlifting**
- Runs 6 weeks, medium-high volume, medium to peak intensity, 4 training days/week; hypertrophy phase → strength phase → peaking — [FitnessVolt Candito 6-week](https://fitnessvolt.com/powerlifting/programs/candito-6-week/)
- Weeks 1-2 "muscular conditioning" with five sessions/week and loads near 80%; weeks 3-4 low volume, high intensity strength emphasis; week 4 heavy acclimatization/explosiveness; week 5 "intense strength" with reduced volume and three sessions; week 6 deload or max test, with a 7th deload week recommended if testing — [Powerlifting To Win Candito review](https://www.powerliftingtowin.com/candito-6-week-strength-program/); [FitnessVolt Candito programs](https://fitnessvolt.com/candito-training-programs/); [BarBend](https://barbend.com/?p=156141)
- Status: free spreadsheet; also on [Boostcamp](https://www.boostcamp.app/jonnie-candito/candito-6-week-strength-program).

**Juggernaut Method base template (Chad Wesley Smith) — 4 days (one main lift per day), intermediate strength**
- 16 weeks in four 4-week waves (10s, 8s, 5s, 3s), each wave = Accumulation, Intensification, Realization, Deload; Realization ends in an all-out AMRAP — [Lift Vault Juggernaut](https://liftvault.com/programs/strength/juggernaut-method-base-template-spreadsheet/); [Coachway Juggernaut](https://coachway.io/articles/chad-wesley-smith-juggernaut-method-for-coaches/)
- Accumulation loads: 10s wave 4x10 + 1x10+ at 60%; 8s wave 4x8 + 1x8+ at 65%; 5s wave 4x5 + 1x5+ at 70%; realization tops out at 75/80/85% respectively; training max ~90% of 1RM — [Lift Vault Juggernaut](https://liftvault.com/programs/strength/juggernaut-method-base-template-spreadsheet/); JTS gives realization back-downs 75/80/85/90% across the four waves — [JTS, Going Heavy on the Juggernaut Method](https://www.jtsstrength.com/going-heavy-on-the-juggernaut-method); 3s wave ~80-92.5% of TM — [Arvo Juggernaut](https://arvo.guru/resources/methods/juggernaut-method)
- Reps beaten on the realization top set bump the training max before the next wave (more reps = larger jump) — [Coachway](https://coachway.io/articles/chad-wesley-smith-juggernaut-method-for-coaches/)
- Status: book (The Juggernaut Method 2.0); base template spreadsheet free on Lift Vault.

**Jeff Nippard Fundamentals Hypertrophy Program — includes a 4-day Upper/Lower track** (see KQ6) — [jeffnippard.com Fundamentals](https://jeffnippard.com/products/fundamentals-hypertrophy-program)

**Jim Stoppani Shortcut to Size — 4-day body-part split** — [Bodybuilding.com](https://bodybuilding.com/fun/our-10-most-popular-workout-programs.html)

### Inferences
- 5/3/1 and Juggernaut share the "one main lift per day, percentage of a training max, AMRAP drives progression" architecture; an app that implements one can implement the other by swapping the percentage tables and the TM-bump rule.
- GZCLP's 4 workouts on 4 days give each T1 lift once weekly and each T2 lift once weekly; on 3 days the same four workouts rotate across the week, which is why GZCLP is listed in both the 3-day and 4-day slots.

### Gaps
- nSuns' exact T1 9-set and T2 8-set percentage tables were not retrievable (the Boostcamp table was garbled in the extract). Verify from the Lift Vault spreadsheet before coding.
- The exact 5/3/1 BBB 3-day vs 4-day layouts and the "BBB not for very new beginners or very advanced lifters" claim came only from low-quality aggregator pages and are not cited.
- PHUL's per-exercise set counts (commonly 3-4) were not stated in any snippet; only rep ranges were.
- Juggernaut's exact TM-increase formula (lb per rep over target) was not given.

---

## Key Question 4: What can I do with 5 days per week? (PHAT, nSuns 5-day, PPL+UL hybrids, body-part splits, Nippard 5-day)

### Takeaway
The 5-day slot is mostly powerbuilding/hypertrophy: PHAT (2 power + 3 hypertrophy days), nSuns 5-day, Nippard's 5-day body-part track, Bodybuilding.com's LiveFit, the "Arnold x Upper Lower" hybrid, and the generic PPL + Upper/Lower hybrid. These are long sessions (PHAT is listed at 90 minutes).

### Cited Findings
**PHAT — Power Hypertrophy Adaptive Training (Layne Norton) — 5 days, powerbuilding, intermediate+**
- Layout: Day 1 Upper Body Power, Day 2 Lower Body Power, Day 3 rest, Day 4 Back & Shoulders Hypertrophy, Day 5 Lower Body Hypertrophy, Day 6 Chest & Arms Hypertrophy, Day 7 rest; meant to be followed for three months = three 4-week cycles — [FitnessVolt PHAT](https://fitnessvolt.com/phat-workout/); [StrengthLog PHAT](https://www.strengthlog.com/phat-workout-routine/)
- Power days: 3 sets of 3-5 reps, starting around 70-80% of 1RM — [Lift Vault PHAT](https://liftvault.com/programs/bodybuilding/phat/)
- Upper Body Power example: Pendlay rows 3x3-5, weighted pull-ups 2x6-10, inverted rows 2x6-10, bench press 3x3-5, overhead press 3x6-10, EZ bar curls 3x6-10, skull crushers 3x6-10 — [FitnessVolt PHAT](https://fitnessvolt.com/phat-workout/)
- Hypertrophy days repeat the movements at lower intensity and higher volume, typically 6-10 reps near failure — [FitnessVolt PHAT](https://fitnessvolt.com/phat-workout/)
- Stop 1-2 reps short of failure when starting; deload every 6-12 weeks — [Lift Vault PHAT](https://liftvault.com/programs/bodybuilding/phat/)
- Suitability: "beginner and intermediate" per FitnessVolt but it recommends 12-18 months of consistent training first because sessions are long and demanding, plus a caloric surplus — [FitnessVolt PHAT](https://fitnessvolt.com/phat-workout/)
- Session length 90 min — [Boostcamp PHAT (Layne Norton)](https://www.boostcamp.app/coaches/layne-norton/phat)
- Origin conflict: originally published on SimplyShredded in 2011 and later updated on Biolayne ([Liftosaur PHAT](https://www.liftosaur.com/programs/phat)) vs. "around since 2008" ([Hevy PHAT](https://www.hevyapp.com/phat-workout/))
- Status: free article; official version on Boostcamp.

**nSuns 531 LP 5-day** — for lifters with 2-3 months of nSuns behind them — [Boostcamp nSuns guide](https://boostcamp.app/nsuns-531-powerlifting-program); user-built Jefit copies estimate ~87 min for a bench/OHP day — [Jefit nSuns 5-day](https://www.jefit.com/routines/51216/nsuns-531-lp-5-day)

**Jeff Nippard Fundamentals — 5-day Bodypart Split track** — "the Bodypart Split will have you in the gym 5 days per week"; program is $39.99; beginner-to-intermediate; three separate 8-week splits — [jeffnippard.com Fundamentals](https://jeffnippard.com/products/fundamentals-hypertrophy-program)
- Nippard's free "Essentials" program is on Boostcamp in 2x, 3x and 5x/week versions — [Boostcamp Essentials 5x](https://www.boostcamp.app/users/oRI0tP-jeff-nippards-essentials-program5x); [Boostcamp Essentials 3x](https://www.boostcamp.app/users/ApMnqS-jeff-nippards-essentials-3xweek); [Boostcamp Essentials 2x](https://www.boostcamp.app/users/logFsy-jeff-nippards-the-essentials-program-2x)

**Jamie Eason LiveFit 12-Week Trainer (Bodybuilding.com classic)** — 12 weeks, 5 workouts/week, intermediate, aimed at fat loss / muscle shaping — [Bodybuilding.com LiveFit](https://bodybuilding.com/workout-plans/about/jamie-easons-livefit-trainer-your-12-week-transformation-plan?page=3); [Bodybuilding.com 10 most popular](https://bodybuilding.com/fun/our-10-most-popular-workout-programs.html)

**Arnold x Upper Lower (5 days)** — late-intermediate/advanced hypertrophy — [FitnessVolt Arnold vs PPL](https://fitnessvolt.com/arnold-split-vs-ppl/)

**Sheiko 4-day variants** — the methodology page says individual programs run 3 to 4 sessions per week — [Boostcamp Sheiko methodology](https://www.boostcamp.app/methodology/sheiko)

### Inferences
- A 5-day week built as PPL + Upper + Lower is the standard way to get ~2x/week frequency without 6 sessions; no primary author "owns" it, so a designer can define it freely (PPL 1x + U/L 1x = every muscle twice).
- PHAT and PHUL share the power/hypertrophy duality; PHAT adds a fifth day by splitting the upper hypertrophy day in two (back/shoulders vs chest/arms), which is the simplest 4→5 day expansion rule for an app.

### Gaps
- No source documented a canonical PPL+Upper/Lower 5-day program with set/rep numbers.
- Kris Gethin 12-Week Trainer days per week not found (listed only as "Advanced, gain weight/build muscle").
- Nippard's Powerbuilding System day count and price were not confirmed from an official page (only an unverified third-party PDF saying 4-6 days).

---

## Key Question 5: What can I do with 6 days per week? (Reddit PPL, Arnold split, nSuns 6-day, RP 6-day)

### Takeaway
Six days is the natural home of PPL run twice (Reddit PPL) and the Arnold split, both giving 2x/week per muscle; nSuns' 6-day variants push one lift to 3x/week. These are for lifters who recover well and can spend 6 sessions; volume per session is lower than on 3-4 day plans.

### Cited Findings
**Reddit PPL (u/Metallicadpa, r/Fitness 2015) — 6 days, PPL x2, novice/early-intermediate strength+size**
- Created by Reddit user /u/metallicadpa, posted to r/Fitness in 2015; Pull/Push/Legs run over six days with two sessions of each; a linear-progression PPL aimed at beginners; fallback: run as 3-day — [Liftosaur Metallicadpa PPL](https://www.liftosaur.com/programs/metallicadpappl)
- Compound lifts: deadlift, bench press, squat, barbell row, overhead press; pull-ups swappable for pulldowns or chin-ups — [Liftosaur Metallicadpa PPL](https://www.liftosaur.com/programs/metallicadpappl)
- Last set of each main compound is AMRAP with at least 5 reps; don't AMRAP bench and OHP on the same day; face pulls 5x15-20; push days superset triceps pushdowns/overhead extensions with lateral raises — [Jefit Reddit PPL copy](https://www.jefit.com/routines/212519/reddit-metallicadpas-beginner-ppl)
- Warm-up: empty bar x10, then 50% x10, 75% x5, 90% x3 of working weight — [Jefit Reddit PPL copy](https://www.jefit.com/routines/212519/reddit-metallicadpas-beginner-ppl)
- Status: free (Reddit post r/Fitness 37ylk5; Boostcamp/Liftosaur mirrors).

**Arnold split — 6 days** — see KQ1 (each muscle 2x/week; Chest/Back, Shoulders/Arms, Legs repeated; advanced) — [Muscle Evo](https://muscleevo.net/arnold-split/); [Fitbod](https://fitbod.me/blog/arnold-split/)

**nSuns 6-day squat / 6-day deadlift** — for lifters who can handle five+ days; the focus lift is programmed 3x/week — [Boostcamp nSuns guide](https://boostcamp.app/nsuns-531-powerlifting-program); [Lift Vault nSuns](https://liftvault.com/programs/powerlifting/n-suns-lifting-spreadsheets/); a user-built 6-day squat copy estimates 135 min per session — [Jefit nSuns 6-day squat](https://www.jefit.com/my-jefit/workouts/36462/nsuns-531-lp-6-day-squat)

**Renaissance Periodization physique templates** — male and female physique templates can be used from 3 to 6 days per week; simplified templates 2-4 days (low-quality source; verify) — [RP template aggregator page](https://chw.dhis2.org/template/rp-training-templates-free.html)

### Inferences
- At 6 days, Reddit PPL and the Arnold split are functionally the same frequency (2x) with different pairings: PPL groups by movement pattern (push/pull/legs), Arnold by antagonist muscle pairs (chest+back, shoulders+arms). For an app, the PPL grouping maps more cleanly onto exercise tags.

### Gaps
- Reddit PPL's exact set/rep scheme per lift (commonly cited as deadlift 1x5+, bench/OHP 5x5 → 1x5+, squat 3x5, rows 4x5/1x5+, accessories 3x8-12) was NOT confirmed by any retrieved snippet; the Jefit copies only confirm the AMRAP rule and the face-pull prescription. Verify against the original Reddit post before copying numbers.
- Reddit PPL progression increments (2.5 kg upper / 5 kg lower per session) and deload rule were not surfaced.

---

## Key Question 6: Multi-frequency frameworks that scale across 1-6 days (GZCL method, Nuckols 28 programs, Sheiko, RP/Israetel, Helms, Nippard)

### Takeaway
Several sources are frameworks rather than fixed day-counts: GZCL's tier rules, Nuckols' 28 programs (1/2/3 days per lift), RP's volume landmarks and 3-6-day templates, Helms' pyramid, and Nippard's 3/4/5-day Fundamentals. These are the best fit for an app that must generate a week from a day count, because their rules are expressed per muscle or per lift rather than per calendar slot.

### Cited Findings
**GZCL Method (Cody Lefever) — framework**
- T1 (primary compound): 85-100% of training max or goal weight, 10-15 total reps per workout, typically 1-3 reps per set — [r/gzcl wiki mirror](https://reddit.sudovanilla.org/r/gzcl/wiki/GZCL); [Boostcamp GZCL methodology](https://www.boostcamp.app/methodology/gzcl)
- T2 (secondary/variation): 65-85%, 20-30 total reps, usually sets of 5-8 — [r/gzcl wiki mirror](https://reddit.sudovanilla.org/r/gzcl/wiki/GZCL); [Bodybuilding.com, Squat Bigger with GZCL](https://bodybuilding.com/fun/squat-bigger-with-the-gzcl-method.html)
- T3 (accessory/isolation): under 65% of a 2-3RM, usually 8+ reps per set, 30+ reps (GZCLP table says 45+) — [FitnessVolt GZCL](https://fitnessvolt.com/gzcl-method/); [r/gzcl wiki mirror](https://reddit.sudovanilla.org/r/gzcl/wiki/GZCL)
- 1:2:3 rule: for every rep in T1, ~2 reps in T2 and ~3 in T3, framed as a weekly balance rather than per session — [Boostcamp GZCL methodology](https://www.boostcamp.app/methodology/gzcl); [FitnessVolt GZCL](https://fitnessvolt.com/gzcl-method/)
- The percentages and rep ranges are "soft" rules; GZCLP is the structured entry program, and the broader method offers more flexible programs (e.g., UHF 5-week, Jacked & Tan 2.0) — [Set For Set GZCLP](https://www.setforset.com/blogs/news/gzclp-beginner-linear-progression-strength-program); [Liftosaur GZCL UHF 5 weeks](https://www.liftosaur.com/programs/gzcl-uhf-5-weeks)
- Status: free (blog/Substack/r/gzcl wiki).

**Greg Nuckols' 28 Free Programs (Stronger By Science)**
- Free in exchange for an email address; covers squat, bench and deadlift with beginner, intermediate and advanced templates at 1, 2 or 3 training days per week per lift; 3 lifts x 3 levels x 3 frequencies = 27, plus a 4th deadlift variation (low/medium/high volume in addition to the standard beginner version) = 28 — [Lift Vault, Nuckols 28 Programs](https://liftvault.com/programs/strength/greg-nuckols-28-programs-spreadsheet/)
- Every program runs on a 4-week cycle with a 1RM test at the end; intermediate/advanced versions add variations (e.g., front squat), beginner versions stick to the big three — [Lift Vault, Nuckols 28 Programs](https://liftvault.com/programs/strength/greg-nuckols-28-programs-spreadsheet/)
- Separate from the newer SBS Program Bundle: six 21-week autoregulated programs, also free with signup — [Lift Vault, Nuckols 28 Programs](https://liftvault.com/programs/strength/greg-nuckols-28-programs-spreadsheet/)

**Sheiko (Boris Sheiko) — 3-4 days, high volume submaximal, intermediate-advanced powerlifting**
- Programs run 3 to 4 sessions per week; most of the cycle at 68-80% of 1RM — [Boostcamp Sheiko methodology](https://www.boostcamp.app/methodology/sheiko)
- #29 = preparation, #30 = highest-volume cycle, #31 = heavier, #32 = peaking; rated intermediate to advanced (1+ years of consistent barbell training) — [Liftosaur Sheiko 29-32](https://www.liftosaur.com/programs/sheiko-29-32); Boostcamp calls #29 and #37 intermediate-friendly starting points — [Boostcamp best Sheiko](https://www.boostcamp.app/best/sheiko)
- Intermediate app versions list 3 days/week and 70-130 minute sessions; a combined #37/#30/#32 "u80" listing says 3 days/week with 180-minute sessions — [Boostcamp Sheiko intermediate medium load](https://www.boostcamp.app/users/N2vPAO-sheiko-intermediate-medium-load); [Boostcamp Sheiko u80](https://www.boostcamp.app/users/sheiko-u80)
- One secondary listing gives 981 working reps across #29 and 1,110 across #37 — [Boostcamp Sheiko intermediate large load](https://www.boostcamp.app/users/1l4raI-sheiko-intermdiate-large-load-2) (single source; approximate)
- Status: original numbered cycles are free (forum/spreadsheets); books and the Sheiko app are paid.

**Renaissance Periodization / Mike Israetel — volume landmarks and templates**
- MEV = lowest weekly set count that still drives growth; MAV = most productive zone; MRV = recoverable ceiling; popularized by Israetel/RP — [Arvo RP training](https://arvo.guru/resources/methods/rp-training)
- Example numbers vary by source: MEV ~4-8, MAV 12-20, MRV 18-30 sets/week for intermediates ([FitnessVolt volume tracker](https://fitnessvolt.com/rpe-training/volume-tracker/)); chest MEV 10, MAV 14-18, MRV 22 ([Arvo volume training](https://arvo.guru/resources/volume-training))
- Weekly frequency per muscle 2-4x, 2-3x typical, per a third-party reference card citing "Scientific Principles of Hypertrophy Training" (unverified against the book) — [skills.cat Israetel reference](https://skills.cat/skills/borisghidaglia/science-based-lifter/israetel-training)
- RP-style mesocycle: start near MEV, add ~1 set per muscle per week over 4-6 weeks, then deload (~1 week at ~50% volume) — [Arvo RP training](https://arvo.guru/resources/methods/rp-training); a forum user describes novice RP templates progressing from 3 RIR to 1 RIR over a 6-week mesocycle followed by a deload — [TexAgs forum](https://texags.com/forums/48/topics/3361390/replies/64326804)
- Physique templates usable 3-6 days/week; simplified templates 2-4 days (low-quality aggregator; verify on rpstrength.com) — [RP template aggregator](https://chw.dhis2.org/template/rp-training-templates-free.html)
- RP recommends reading Helms' Muscle and Strength Pyramids before its own "Scientific Principles of Hypertrophy" book — [Performative Bafflement hypertrophy guide](https://performativebafflement.substack.com/p/a-comprehensive-guide-to-hypertrophy)
- Status: paid (templates, books, RP Hypertrophy app); free content on RP YouTube/blog.

**Eric Helms — The Muscle and Strength Pyramid: Training (3rd ed.)**
- Framework levels: Adherence; Volume, Intensity and Frequency; Progression; Exercise Selection; Rest Periods and Tempo; Warming Up; the first level plans workout frequency with adherence in mind — [RippedBody, how to build training programs (sample chapter)](https://rippedbody.com/how-to-build-training-programs/)
- Status: paid book; sample chapter free at RippedBody.

**Jeff Nippard — Fundamentals Hypertrophy Program**
- $39.99 (sale price listed), beginner-to-intermediate, three separate 8-week splits: Full Body 3 days/week, Upper/Lower 4 days/week, Bodypart 5 days/week; needs a rack, barbell, bench and ideally dumbbells — [jeffnippard.com Fundamentals](https://jeffnippard.com/products/fundamentals-hypertrophy-program)
- Free "Essentials" program on Boostcamp in 2x/3x/5x week versions — [Boostcamp Essentials 3x](https://www.boostcamp.app/users/ApMnqS-jeff-nippards-essentials-3xweek)

### Inferences
- The frameworks converge on the same generator logic: pick weekly sets per muscle (RP landmarks / Helms volume), pick frequency 2-3x (SBS evidence, RP), then divide sets across the available days. GZCL adds the per-session shape (one heavy T1, one moderate T2, high-rep T3s with 1:2:3 rep balance).
- Nuckols' "days per lift" design is the only cited system that explicitly decouples per-lift frequency from the weekly day count (a 3-day week can run squat 1x, bench 3x, deadlift 1x), which is useful for user-chosen priorities.

### Gaps
- Helms' concrete numbers (weekly sets per muscle, rep ranges, frequency) were not stated in any snippet; only the framework's level names were. Do not quote "10-20 sets" to Helms without checking the book/sample chapter.
- RP's official template day-counts and prices were not confirmed from rpstrength.com.
- Israetel's exact per-muscle landmark tables could not be verified; the values above are third-party approximations and differ by site.

---

## Key Question 7: Which programs explicitly support flexible or variable training days?

### Takeaway
Explicit flexibility is rarer than assumed: 5/3/1 has official 2-day and 3-day templates and a rotating 4-workout structure; GZCLP/GZCL and Reddit PPL state 3- or 4-/6-day options; Nuckols' 28 programs offer 1/2/3 days per lift; RP templates span 3-6 days; Nippard sells 3/4/5-day tracks. The specific Wendler phrase "I don't have a set schedule" could not be located in any retrieved source.

### Cited Findings
- 5/3/1: official templates include "3 Days Per Week" and "The Twice A Week" — [EliteFTS Training Templates eBook](https://elitefts.com/products/training-templates-by-jim-wendler-ebook); on 3 days you rotate the 4 core workouts and the cycle stretches to 5+ weeks — [Muscle & Strength 5/3/1](https://www.muscleandstrength.com/node/4458); Wendler has crafted variations for frequencies as low as twice per week — [Lift Vault 5/3/1 spreadsheet](https://liftvault.com/programs/powerlifting/jim-wendlers-531-spreadsheet/); 5/3/1 Forever includes 50+ templates — [AbeBooks 5/3/1 Forever](https://www.abebooks.com/Title-531-Forever-Simple-Effective-Programming/31945876298/bd); community practice of running the 4 lifts over 9 days — [T-Nation thread](https://t-nation.com/t/leader-anchor-4-day-forever-templates-2-days-a-week/275860)
- GZCL: "a framework rather than a fixed program"; percentages/rep ranges are soft rules; GZCLP for beginners, flexible programs for those past that phase — [Set For Set GZCLP](https://www.setforset.com/blogs/news/gzclp-beginner-linear-progression-strength-program); [FitnessVolt GZCL](https://fitnessvolt.com/gzcl-method/)
- Reddit PPL: "Can't train 6 days: run it as a 3-day program" — [Liftosaur Metallicadpa PPL](https://www.liftosaur.com/programs/metallicadpappl)
- Arnold split: beginners do each workout once per week (3 days), experienced lifters twice (6 days) — [Fitbod Arnold split](https://fitbod.me/blog/arnold-split/)
- Nuckols 28: templates at 1, 2 or 3 days per week per lift, mixable across lifts — [Lift Vault Nuckols 28](https://liftvault.com/programs/strength/greg-nuckols-28-programs-spreadsheet/)
- nSuns: 4-, 5- and 6-day variants — [Boostcamp nSuns](https://boostcamp.app/nsuns-531-powerlifting-program)
- Nippard Fundamentals: 3-, 4- and 5-day splits sold as one product — [jeffnippard.com Fundamentals](https://jeffnippard.com/products/fundamentals-hypertrophy-program); Essentials free in 2x/3x/5x — [Boostcamp Essentials 2x](https://www.boostcamp.app/users/logFsy-jeff-nippards-the-essentials-program-2x)
- RP physique templates 3-6 days, simplified 2-4 (weak source) — [RP template aggregator](https://chw.dhis2.org/template/rp-training-templates-free.html)
- Boostcamp has a reschedule feature for when the week doesn't go to plan — [Boostcamp 5/3/1 full body](https://www.boostcamp.app/users/h6oNsc-531-full-body-1000percent-awesome)
- Lyle McDonald GBR: set counts flexible within the prescribed range by feel — [Liftosaur Lyle GBR](https://www.liftosaur.com/programs/lylegenericbulking)
- Candito 6-week varies sessions per week by phase (5 in weeks 1-2, 3 in week 5) — [Powerlifting To Win Candito](https://www.powerliftingtowin.com/candito-6-week-strength-program/); [FitnessVolt Candito programs](https://fitnessvolt.com/candito-training-programs/)

### Inferences
- The programs that tolerate a variable week best are those whose unit is a "workout in a rotation" rather than a "day of the week": 5/3/1 (4 workouts), GZCLP (A1/A2/B1/B2), SS/SL/Greyskull (A/B), Reddit PPL (P/P/L). A designer can make any of these day-count-agnostic by storing a rotation pointer and stretching the cycle length (as Muscle & Strength describes for 5/3/1 on 3 days).
- Programs with fixed weekly roles (Texas Method, Madcow, PHUL, PHAT, Candito) assume specific day spacing (volume → recovery → intensity; power → hypertrophy) and degrade when days are dropped.

### Gaps
- The Wendler "I don't have a set schedule" template (from Beyond 5/3/1 or 5/3/1 Forever) was not found in any search result; the search budget ran out before a targeted follow-up. Its contents (commonly described as rotating the four lifts through whatever days are available) remain unverified here.

---

## Key Question 8: Typical session durations by layout/program

### Takeaway
Cited figures: full body 45-70 min; upper/lower 45-60; PPL 40-75; PHAT 90 min; nSuns ~60-135 min depending on accessory volume; Sheiko 70-180 min; Shortcut to Size 45-60. Most other programs publish no official duration.

### Cited Findings
- Full body 45-70 min; PPL 40-60 min — [GetFitCraft](https://getfitcraft.com/guides/full-body-vs-split-workout)
- Upper/lower 45-60 min; PPL 45-75 min — [FindYourEdge U/L](https://www.findyouredge.app/news/upper-lower-split-for-beginners-uk-2026)
- PHAT: session length 90 min — [Boostcamp PHAT](https://www.boostcamp.app/coaches/layne-norton/phat); PHAT sessions described as long and demanding — [FitnessVolt PHAT](https://fitnessvolt.com/phat-workout/)
- nSuns user-built copies: 87 min (8 exercises, bench/OHP day), 135 min (6-day squat variant), 57-61 min (trimmed versions) — [Jefit nSuns 5-day](https://www.jefit.com/routines/51216/nsuns-531-lp-5-day); [Jefit nSuns 6-day squat](https://www.jefit.com/my-jefit/workouts/36462/nsuns-531-lp-6-day-squat); [Jefit nSuns LP](https://www.jefit.com/routines/36439/nsuns-531-lp)
- Sheiko intermediate app versions 70-130 min; u80 combined listing 180 min — [Boostcamp Sheiko intermediate medium load](https://www.boostcamp.app/users/N2vPAO-sheiko-intermediate-medium-load); [Boostcamp Sheiko u80](https://www.boostcamp.app/users/sheiko-u80)
- Shortcut to Size 45-60 min per workout — [Bodybuilding.com 10 most popular](https://bodybuilding.com/fun/our-10-most-popular-workout-programs.html)

### Inferences
- Duration tracks total sets plus rest: percentage-based strength programs with many heavy sets and long rests (nSuns 9+8 sets of main work, Sheiko) run longest; A/B novice programs with 3 lifts per day should sit at the low end of the 45-70 min full-body band even though no official figure was cited.

### Gaps
- No source gave official durations for 5/3/1 (the "45 minutes" folk figure), GZCLP, Reddit PPL, Starting Strength, StrongLifts, Texas Method, Madcow, PHUL, Juggernaut or Candito.

---

## Key Question 9: Copyright / paywall status summary

### Takeaway
Most community strength programs are free; author-brand programs (Wendler books, Rippetoe books, Helms, RP, Nippard Fundamentals, Juggernaut book, Greyskull book) are paid, usually with the core method freely described online.

### Cited Findings
- Free: GZCLP/GZCL ([Boostcamp GZCLP](https://www.boostcamp.app/coaches/cody-lefever/gzcl-program-gzclp)); nSuns ([Lift Vault](https://liftvault.com/programs/powerlifting/n-suns-lifting-spreadsheets/)); Reddit PPL ([Liftosaur](https://www.liftosaur.com/programs/metallicadpappl)); PHUL ([Muscle & Strength](https://www.muscleandstrength.com/workouts/phul-workout)); PHAT ([Boostcamp](https://www.boostcamp.app/coaches/layne-norton/phat)); Candito 6-week ([Boostcamp](https://www.boostcamp.app/jonnie-candito/candito-6-week-strength-program)); Lyle GBR ([Lift Vault](https://liftvault.com/programs/bodybuilding/lyle-mcdonald-bulking-workout-routine-spreadsheet/)); Nuckols 28 (free for email) and SBS Bundle (free with signup) ([Lift Vault](https://liftvault.com/programs/strength/greg-nuckols-28-programs-spreadsheet/)); Nippard Essentials ([Boostcamp](https://www.boostcamp.app/users/ApMnqS-jeff-nippards-essentials-3xweek)); 5/3/1 core percentages and BBB posts ([jimwendler.com](https://www.jimwendler.com/blogs/jimwendler-com/101077382-boring-but-big)); Juggernaut base template spreadsheet ([Lift Vault](https://liftvault.com/programs/strength/juggernaut-method-base-template-spreadsheet/)).
- Paid: 5/3/1 Forever and Training Templates eBook ([EliteFTS](https://elitefts.com/products/training-templates-by-jim-wendler-ebook); [AbeBooks](https://www.abebooks.com/Title-531-Forever-Simple-Effective-Programming/31945876298/bd)); Nippard Fundamentals $39.99 ([jeffnippard.com](https://jeffnippard.com/products/fundamentals-hypertrophy-program)); Helms' Muscle and Strength Pyramid book, sample chapter free ([RippedBody](https://rippedbody.com/how-to-build-training-programs/)); Starting Strength / Practical Programming books ([Starting Strength programs page](https://startingstrength.com/get-started/programs)); Greyskull LP book ([Powerlifting Technique](https://powerliftingtechnique.com/greyskull-lp/)).

### Inferences
- For an app, the safest sources to reproduce verbatim are the community programs (GZCLP, nSuns, Reddit PPL, PHUL, PHAT, Lyle GBR, Candito, Nuckols 28 with attribution). Book-based programs (5/3/1 templates, SS phases, Juggernaut, Helms, RP) should be implemented as original parameterizations of the published method with attribution rather than copied tables.

### Gaps
- RP template and RP Hypertrophy app prices were not confirmed from an official page.
- StrongLifts app free-vs-paid tier split was not retrieved (stronglifts.com unreachable).

---

## Quick index: days per week → documented options

- **2 days:** 5/3/1 "Twice A Week" template (paid eBook); Nippard Essentials 2x (free); RP simplified templates 2-4 days (weak source); Nuckols 28 at 1-2 days per lift (free).
- **3 days:** Starting Strength (book); StrongLifts 5x5 (free); Greyskull LP / Phrak's (book / free); GZCLP 3-day rotation (free); 5/3/1 3-day rotation (free core); Texas Method (book, widely mirrored); Madcow 5x5 (free); Reddit PPL 3-day fallback (free); Arnold split 1x (free); Sheiko intermediate 3-day (free numbered cycles); Nippard Fundamentals full-body / Essentials 3x (paid / free); Nuckols 28 at 3 days per lift (free).
- **4 days:** 5/3/1 standard, BBB, Forever leader/anchor (free core / paid books); GZCLP native (free); nSuns 4-day (free); PHUL (free); Lyle McDonald GBR (free); Candito 6-week (free); Juggernaut Method base (book / free spreadsheet); Nippard Fundamentals U/L (paid); Shortcut to Size (Bodybuilding.com, free); Sheiko 4-day (free cycles).
- **5 days:** PHAT (free); nSuns 5-day (free); Nippard Fundamentals bodypart / Essentials 5x (paid / free); LiveFit (free); Arnold x Upper Lower (free description); generic PPL + U/L hybrid (no canonical source).
- **6 days:** Reddit PPL (free); Arnold split (free description); nSuns 6-day squat / deadlift (free); RP physique templates up to 6 days (paid).
