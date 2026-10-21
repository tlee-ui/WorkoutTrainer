# Mobile Workout-Tracking Apps for Running a Markdown/GitHub-Maintained Custom Strength Program (as of 2026-10-21)

Research-environment note: `WebFetch` returned DNS errors (`getaddrinfo ENOTFOUND`) for liftosaur.com, www.liftosaur.com, api.hevyapp.com, apps.apple.com, setgraph.app and huggingface.co; only github.com fetches succeeded. `WebSearch` refused `allowed_domains: reddit.com` ("not accessible to our user agent"). Consequently most app-site/App Store facts below come from WebSearch result summaries of those pages (cited by URL) rather than full-page reads, and Reddit sentiment could not be sampled directly. Claims that could not be verified are explicitly flagged "(unverified)".

## Key Question 1: Per-app profile (platforms, price, program builder, import, export, progression automation, any-order/rotation, watch, offline, data ownership)

### Takeaway
Only two candidates offer a programmatic path for an agent to push a program into the app: **Liftosaur** (text-based Liftoscript programs, shareable as text snippets or links; open-source AGPL; has an API behind Premium) and **Hevy** (official REST API with routine/routine-folder create/update endpoints, Pro-only). Everything else requires manual program entry; **Boostcamp** adds a web program builder plus shareable program links, and **Strong**, **Alpha Progression**, **FitNotes** offer CSV export for analysis but no import of custom programs.

### Cited Findings

**Liftosaur**
- Open-source weightlifting tracker "for coders"; a PWA with thin iOS/Android wrappers; Liftoscript is a JavaScript-like scripting language for progression/deload logic with `kg`/`lb` number types; built-in programs (5/3/1, GZCLP, Starting Strength) all editable; plates calculator; weight rounding to available plates/bars; rest timers with push notifications (native apps only); graphs, muscle map, exercise substitution, custom exercises, warmup configuration; bodyweight/measurements; web editor for programs; shareable programs via a generated link importable on another phone; works offline (account needed for cloud save); license AGPL-3.0; self-hosting the backend is difficult (tied to liftosaur.com domain, AWS CDK) — [GitHub README](https://github.com/astashov/liftosaur)
- App Store listing: free download, last updated July 8, 2026; "share those programs with others - either as text snippets or as links"; pasted program text can be imported ("You can add this text snippet to the app"); Web Editor for desktop program creation — [AppFollow mirror of App Store listing](https://apps.appfollow.io/ios/liftosaur-scriptable-workouts/1661880849?country=td); [Liftosaur overview blog](https://www.liftosaur.com/blog/posts/liftosaur-overview/)
- Apple Watch: maintainer astashov posted "Apple Watch is done" on Feb 5, 2026 in the Wear/Watch discussion; Health Connect sync shipped earlier (Oct 2024 comment); Wear OS: a user asked Jul 24, 2026 "Any word on Android watch support?" with no maintainer reply; users mention buying a "lifetime pass" and "premium" — [GitHub Discussion #118](https://github.com/astashov/liftosaur/discussions/118)
- Third-party integrator says Liftosaur API access requires Premium and a personal API key is created under Liftosaur settings — [Wellness Project integration page](https://wellnessproject.ai/fr/integrations/liftosaur) (third-party; unverified against Liftosaur docs)
- Liftoscript syntax details: see Key Question 2.

**Hevy**
- Pro pricing cited at $2.99/mo, $23.99/yr, $74.99 lifetime (some sources also mention $3.99/mo); free tier: unlimited workout logging, capped at 4 routines, 7 custom exercises, ~3 months of graph history; regional pricing varies — [SensAI Hevy review 2026](https://www.sensai.fit/blog/hevy-review-2026) (competitor blog); [Boostcamp vs Hevy](https://boostcamp.app/vs/hevy) (competitor); [aitoolsbakery Hevy review 2026](https://aitoolsbakery.com/?p=18424)
- Export: Profile > Settings > Export & Import Data > Export Data (workouts or measurements). Import: CSV only from Strong app format, in English; support can send a sample CSV in the Strong format for other sources — [Hevy help: Import Strong CSV / Export](https://help.hevyapp.com/hc/en-us/articles/38001424401943-How-to-Import-Strong-App-CSV-Files-and-Export-Your-Data-in-Hevy)
- Public API: REST at api.hevyapp.com, per-account UUID key in an `api-key` header; key issued to Pro subscribers at the web app's developer settings page (`https://hevy.com/settings?developer`); docs at `https://api.hevyapp.com/docs/` (fetch failed: DNS) — [apis.io Hevy auth profile](https://apis.io/security/hevy/hevy-authentication/); [hevy-py README](https://github.com/ewright3/hevy-py)
- API operations per unofficial Python SDK: workouts (list/get/create/update/count/events since), routines (list/get/create/update), routine folders (list/get/create), exercise templates (list/get/create custom), webhooks (create/get/delete), exercise history — [hevy-py README](https://github.com/ewright3/hevy-py); Hevy MCP server can read/create/update workouts and routines, requires Pro + API key — [mcpmarket Hevy MCP](https://mcpmarket.com/server/hevy-5); [apis.io Routine Folders API](https://apis.io/apis/hevy/hevy-routinefolders-api/)
- Routines are started by tapping "Start Routine" on the Workout tab; routines grouped in folders (e.g. by split); saved library programs appear as a folder; ad-hoc empty workouts also supported; no weekday-schedule concept appears in the help pages — [Hevy help: Build a Workout Program](https://help.hevyapp.com/hc/en-us/articles/34953606698903-Build-a-Workout-Program-Create-Organize-Routines); [Hevy help: Log a Workout](https://help.hevyapp.com/hc/en-us/articles/35361530647959-How-to-Log-a-Workout-in-the-Hevy-App-Step-by-Step-Guide)
- Integrations: Apple Health sync (writes workouts; outage-period workouts don't backfill), Health Connect, Strava (one-way Hevy->Strava, per-workout "Sync with" toggle) — [Hevy help: Apple Health troubleshooting](https://help.hevyapp.com/hc/en-us/articles/36957445562775-Hevy-Not-Syncing-to-Apple-Health-Step-by-Step-Troubleshooting); [Hevy help: Strava](https://help.hevyapp.com/hc/en-us/articles/38279744541591-Using-Hevy-with-Strava-Setup-Syncing-and-Editing-Workouts); [Hevy Integrations category](https://help.hevyapp.com/hc/en-us/categories/33072994406423-Integrations)
- Data ownership: "your information on Hevy is stored to your profile on our servers, not to your device"; an unsaved active workout is lost if the app is uninstalled — [Hevy help: uninstall/reinstall](https://help.hevyapp.com/hc/en-us/articles/38223672272791-What-will-happen-to-my-information-if-I-uninstall-and-reinstall-the-Hevy-app)
- Same account works across devices/platforms — [Setgraph blog roundup](https://setgraph.app/ai-blog/best-app-to-track-weight-lifting-progress-top-options-2026) (vendor)

**Strong**
- Strong PRO $4.99/mo, $29.99/yr, $99.99 one-time ("Forever"); free version logs unlimited workouts with 3 templates; iPhone, Apple Watch, Android — [SensAI Strong review Oct 2026](https://www.sensai.fit/es/blog/strong-app-review-2026) (competitor); App Store IAP tracker snapshot April 2026 shows $4.99/$29.99/$99.99 — [App Pricing Lab](https://apppricinglab.com/iap/apple/464254577)
- Strong supports CSV export of workout history and RPE logging; custom-routine cap removed on PRO — [Boostcamp vs Strong](https://www.boostcamp.app/vs/strong) (competitor, May 2026); Hevy imports Strong-format CSV, confirming Strong CSV export exists — [Hevy help](https://help.hevyapp.com/hc/en-us/articles/38001424401943-How-to-Import-Strong-App-CSV-Files-and-Export-Your-Data-in-Hevy)
- Sentiment: April 2026 review aggregator reports workouts sometimes not showing up or failing to sync with Apple Watch; aggregator sentiment ~59% positive/29% negative — [justuseapp Strong reviews](https://justuseapp.com/en/app/464254577/strong-workout-tracker-gym-log/reviews); unitQ score 58 ("fair") with 2024 Watch-sync reports — [unitQ scorecard](https://www.unitq.com/unitq-scorecards/strongworkouttracker/)
- No public API or program import found in any source (gap).

**Boostcamp**
- Pro $59.99/yr (7-day trial) or $14.99/mo (one Boostcamp page says $11.99/mo — conflicting); free tier includes workout tracker, RPE/RIR logging, rest timers (auto-start per exercise), PR boards, Weekly Report, custom program builder (limited count); Pro adds 20+ coach programs, Strength Score, muscle-volume heatmap, advanced analytics, unlimited custom programs — [Boostcamp: is it free](https://www.boostcamp.app/is-boostcamp-free); [Boostcamp Pro](https://www.boostcamp.app/pro); [Boostcamp rest timer](https://www.boostcamp.app/features/rest-timer); [Boostcamp RPE/RIR](https://www.boostcamp.app/best/rpe-rir)
- Web program creator: saved programs appear in the app immediately; programs shareable via (private) link that lets the recipient save to their account — [Boostcamp custom program](https://boostcamp.app/custom-program); [Boostcamp features](https://www.boostcamp.app/features)
- Android available — [Boostcamp RPE/RIR page](https://www.boostcamp.app/best/rpe-rir)
- No data export (CSV/API) found anywhere in Boostcamp materials — [Boostcamp vs Strong](https://www.boostcamp.app/alternatives/strong) notes Strong's CSV export without claiming one for Boostcamp (absence of evidence; unverified)
- Fortune 2026 roundup named Boostcamp "best free option" — [Fortune best weightlifting apps](https://www.fortune.com/article/best-weightlifting-apps/)
- Garage Gym Reviews has a Boostcamp review page (content not retrieved) — [GGR Boostcamp review](https://www.garagegymreviews.com/boostcamp-review)

**JEFIT**
- Elite ~$12.99/mo or $69.99/yr, no lifetime; free tier ad-supported; verified Aug 2026 by SensAI; App Store prices tracked Apr 20, 2026 — [SensAI Jefit vs Hevy 2026](https://www.sensai.fit/pt/blog/jefit-vs-hevy-2026) (competitor); [Boostcamp vs JEFIT](https://www.boostcamp.app/vs/jefit); [App Pricing Lab JEFIT](https://www.apppricinglab.com/iap/apple/449810000)
- Tracks volume, PRs, 1RM — [Setgraph roundup](https://setgraph.app/ai-blog/best-app-to-track-weight-lifting-progress-top-options-2026)
- No export/API information found in 2026 sources (gap).

**Alpha Progression**
- Premium $12.99/mo or $79.99/yr (one Alpha Progression page lists $14.99/mo — conflicting); CSV export listed as a free-tier feature; RPE/RIR analysis gated to Premium; automatic periodization of sets/reps/RIR across mesocycles with integrated deloads; plan generator asks days/week, session length, muscle focus; can build plans from scratch and edit every detail — [Alpha Progression guide](https://alphaprogression.com/en/blog/alpha-progression-guide); [Boostcamp RPE/RIR comparison](https://www.boostcamp.app/best/rpe-rir); [Alpha Progression vs Gravl](https://alphaprogression.com/en/blog/alpha-progression-vs-gravl); [Alpha Progression vs Caliber](https://alphaprogression.com/en/blog/alpha-progression-vs-caliber); [hotelgyms how-to guide](https://www.hotelgyms.com/blog/how-to-use-alpha-progression)
- Android available — [Boostcamp RPE/RIR page](https://www.boostcamp.app/best/rpe-rir)
- No program import or API found (gap).

**Setgraph**
- iOS, Android, Apple Watch; 67,000+ lifters, 4.8 average rating, 50M+ sets; compares each set to the previous session (percent change in reps, weight, volume, sets); rest timers auto-start after a set, visible on Lock Screen/Dynamic Island — [setgraph.app/llms.txt](https://setgraph.app/llms.txt) (vendor; fetch failed, summary from search); [App Store listing](https://apps.apple.com/cr/app/setgraph-work-out-rep-counter/id1209781676)
- Pro tier reportedly $4.99/mo — [low-quality roundup via search](https://www.nomorestrangers.org/10-best-workout-apps-of-2026-tested-by-personal-2/) (unverified)
- Export/import/API: not found (gap).

**KeyLifts**
- "KeyLifts - 531 Workout Log" by Strongomatic LLC; iOS; free with IAP; built around Wendler 5/3/1 with auto-calculated cycles; free: warm-ups, rest timer, 150+ templates from the 5/3/1 books, custom templates, assistance and Joker sets; Pro: automatic training-max progression, cloud backup/sync, plate calculator, graphs, Apple Health; 4.8 rating from ~800 ratings — [App Store listing](https://apps.apple.com/us/app/keylifts-531-workout-log/id1437949461); [appshunter reviews](https://appshunter.io/ios/app/keylifts-531-workout-log/id1437949461/reviews)
- No Android, no import/export/API found (gap).

**Gravitus**
- iOS with companion Apple Watch app (auto sync, live heart rate); Gravitus Pro monthly/yearly subscription (amounts not stated) adds unlimited programs, unlimited graph history, real-time analytics; Apple Health integration (charts HealthKit data, optional bodyweight write-back); no CSV export found — [App Store listing](https://apps.apple.com/us/app/gravitus-gym-workout-tracker/id965383840); [marlvel aggregator](https://marlvel.ai/apps/gravitus-gym-workout-tracker) (AI-generated, low weight)

**RepCount**
- By Siper Apps AB; iOS; free with two "RepCount Premium" IAPs $4.99–$29.99; Premium adds supersets and advanced progress statistics; no export/API found — [App Pricing Lab RepCount](https://apppricinglab.com/app/apple/594982044); [App Store listing (es-MX)](https://apps.apple.com/us/app/repcount-%EC%9A%B4%EB%8F%99%EC%9D%BC%EC%A7%80-%EC%9A%B4%EB%8F%99-%EA%B8%B0%EB%A1%9D-%ED%97%AC%EC%8A%A4-%EA%B8%B0%EB%A1%9D/id594982044?l=es-MX)

**FitNotes (Android)**
- Android-only, developer James Gay, no official iPhone release; exports training logs as CSV for spreadsheets; CSV is not a restorable backup — the proprietary backup goes to device storage, Dropbox or Google Drive — [BlueStacks mirror of Play listing](https://www.bluestacks.com/campaign/com.github.jamesgay.fitnotes/en); [ghacks review](https://www.ghacks.net/?p=90924); [Setgraph comparison article](https://setgraph.app/articles/best-workout-tracking-apps); [Wellness Project page](https://wellnessproject.ai/fitnotes-for-iphone) (competitor marketing)

**Progression (Android)**
- No Google Play listing or 2025–2026 source for an Android app named "Progression" was found; the only "Progression Workout Tracker" found is iOS-only (id1090687896) focused on automatic weight/rep adjustment — [App Store](https://apps.apple.com/us/app/-/id1090687896). Treat the Android "Progression" candidate as unresearched (gap).

**Fitbod**
- ~$15.99/mo or $95.99/yr (~$8/mo) per a user review; AI-generated workouts; no official pricing page or export documentation retrieved — [IndieHackers review 2026](https://www.indiehackers.com/post/fitbod-app-review-2026-honest-take-after-real-testing-45d5f07a1b); tracks benchmark lifts/estimated strength — [Setgraph roundup](https://setgraph.app/ai-blog/best-app-to-track-weight-lifting-progress-top-options-2026). Export: not found (gap).

**RP Hypertrophy**
- $299.99/yr per Oct 2026 competitor comparison; web app usable from any browser; 45 pre-built programs that autofill, or custom meso builder from scratch; workouts changeable on the fly — [SensAI JuggernautAI vs RP vs Alpha 2026](https://www.sensai.fit/blog/juggernaut-ai-vs-rp-hypertrophy-vs-alpha-progression-2026) (competitor); [App Store listing](https://apps.apple.com/us/app/rp-hypertrophy/id1555614554). Export: not found (gap).

**JuggernautAI**
- $34.99/mo or $349.99/yr, 2-week trial, no permanent free tier — [Boostcamp vs JuggernautAI](https://www.boostcamp.app/vs/juggernautai); [SensAI comparison](https://www.sensai.fit/blog/juggernaut-ai-vs-rp-hypertrophy-vs-alpha-progression-2026). It is a program generator, not a custom-program runner (inference from both sources). Export: not found (gap).

**Stronger By Science via Boostcamp**: Boostcamp markets "20+ exclusive coach programs" on Pro — [Boostcamp Pro](https://www.boostcamp.app/pro); no source retrieved confirming SBS specifically in 2026 (gap).

**2025–2026 entrants / open-source**
- Liftlog: free, open-source gym tracker with single-tap set logging and rest timers — [AlternativeTo listing](https://alternativeto.net/software/workout-tracker)
- openGym: self-hosted AGPL-3 PWA (React + Docker) with Android APK, weekly plan, 1,324-exercise library, PR detection; activity into Sept 2026; exercise media licensing disputed — [openGym mirror](https://gitea.com/estebanfak/openGym)
- GymRoutines (Android, F-Droid): open-source, on-device data, data export, `adb backup` — [F-Droid listing](https://f-droid.org/es/packages/com.noahjutz.gymroutines/)
- Bolic: open-source hypertrophy tracker "founded 2026" — [startuphub listing](https://www.startuphub.ai/startups/bolic.md) (unverified)
- Gravl: referenced only as a competitor in Alpha Progression's blog with "per-muscle recovery system" generation — [Alpha Progression vs Gravl](https://alphaprogression.com/en/blog/alpha-progression-vs-gravl); no primary source retrieved.
- SensAI, PonteFuerteAI, Wellness Project: new AI-coach apps whose blogs produce most 2026 comparison content; all are competitors and should be weighted accordingly — [SensAI pricing comparison](https://www.sensai.fit/blog/fitness-app-pricing-free-tier-comparison); [PonteFuerteAI Hevy alternatives](https://www.pontefuerteai.com/blog/best-hevy-alternatives-2026)

**Spreadsheet/Notion baseline**
- Notion templates exist for RIR/volume logging with custom programs (paid, $25+) and cheaper split-based trackers ($6+); a free one-click logger supports up to 4 sets per exercise — [Mingus Lilja Notion template](https://minguspingus.gumroad.com/l/eolfw); [setinnotion template](https://setinnotion.gumroad.com/l/nqkqc); [expan.do simple tracker](https://help.expan.do/templates/a-simple-workout-tracker); [Notion template gallery](https://www.notion.com/en-gb/templates/collections/top-10-free-fitness-routine-templates-in-notion)
- Google Sheets results were generic how-to pages (exercise/sets/reps/weight columns, conditional formatting); no lifting-specific template with progression logic surfaced — [generic Sheets template page](https://ocms.walkerart.org/workout-program-template-google-sheets) (low quality)

### Inferences
- Hevy and Liftosaur are the only two candidates with a documented machine-writable input path (API and text DSL respectively); Boostcamp's link-sharing is a human-to-human path, not agent-writable.
- Apps that organize programs as unscheduled "routines/templates" (Hevy, Strong) are naturally any-order; coach/AI apps (RP, JuggernautAI, Alpha Progression generator, Fitbod) are built around their own periodization and are poor fits for an externally maintained program.
- Open-source/self-hosted options (openGym, GymRoutines, Liftlog) give maximal data ownership but lack Watch support and polish; Liftosaur is the only open-source option with a shipped Apple Watch app.

### Gaps
- Liftosaur Premium price (monthly/yearly/lifetime) could not be retrieved (site DNS failure; no search result stated it).
- Hevy API request/response schemas and rate limits (api.hevyapp.com/docs unreachable).
- Whether Alpha Progression's CSV export includes RPE/RIR values.
- Export options for Boostcamp, JEFIT, Setgraph, Gravitus, RepCount, Fitbod, RP, JuggernautAI, KeyLifts — not found; absence is not proof of absence.
- Wear OS support for every app except Liftosaur (no answer) was not confirmed.
- Current App Store privacy-label details for all apps (apps.apple.com unreachable).

## Key Question 2: Which apps have a public/documented API or an import format an agent could generate from markdown/CSV? Format details

### Takeaway
Liftosaur's Liftoscript is a plain-text program format (exercise lines with `sets x reps`, weights/`%`/`@RPE`, and `progress:` rules such as `lp()`, `dp()`, `sum()`, `custom()`) that can be shared as text or link and pasted into the app, making it the most direct markdown->program target; Hevy's Pro-only REST API (`api-key` header) supports creating/updating routines and routine folders programmatically.

### Cited Findings
- Liftoscript: omit weight and the app estimates from RPE tables (no RPE assumes failure at RPE 10; 12 reps ≈ 65% 1RM) — [Liftosaur docs](https://www.liftosaur.com/docs)
- Per-set targets: RPE `@8`, percentage of 1RM `80%`, or absolute `kg`/`lb`; set groups like `1x5 @8, 1x3 @9, 1x1 @10, 5x5 50%`; `+` after RPE logs actual RPE; `?+` asks for the weight after the fact — [Liftoscript doc](https://www.liftosaur.com/doc/liftoscript)
- `progress:` attaches a rule to an exercise, e.g. `progress: lp(5lb)` (linear progression) — [api3.liftosaur.com "How it works"](https://api3.liftosaur.com)
- New program editor: `progress: custom() { ... }` with Liftoscript in `{~ ~}` blocks, built-in variables like `weights` updated directly; warmup percentages are of the first set's weight, not 1RM — [Liftosaur blog: new program editor](https://www.liftosaur.com/blog/posts/new-experimental-program-editor)
- Progression types listed by third parties: `lp`, `dp`, `sum`, `custom`; `dp(weight, minReps, maxReps)` and `sum(totalReps, weight)` signatures appear in a fallback doc embedded in a community MCP server — [agentskills.so Liftosaur program creator skill](https://agentskills.so/skills/pbantolas-liftosaur-program-creator-liftosaur-program-creator); [Hugging Face liftosaur-mcp app.py](https://huggingface.co/spaces/davanstrien/liftosaur-mcp/blob/main/app.py) (signatures unverified against official docs)
- Programs can be shared as text snippets or links and pasted into the app; web editor available — [AppFollow listing](https://apps.appfollow.io/ios/liftosaur-scriptable-workouts/1661880849?country=td); [Liftosaur overview](https://www.liftosaur.com/blog/posts/liftosaur-overview/); link import confirmed in README — [GitHub README](https://github.com/astashov/liftosaur)
- Community tooling already exists for agents: a Liftosaur MCP server that fetches Liftoscript docs (overview, syntax, progressions) — [Hugging Face liftosaur-mcp](https://huggingface.co/spaces/davanstrien/liftosaur-mcp/blob/main/app.py); an agent "skill" for generating Liftosaur programs — [agentskills.so](https://agentskills.so/skills/pbantolas-liftosaur-program-creator-liftosaur-program-creator)
- Hevy API: REST, `api-key` header with per-account UUID; Pro-only; key from `https://hevy.com/settings?developer`; docs `https://api.hevyapp.com/docs/`; OpenAPI spec published (no standard security declaration) — [apis.io](https://apis.io/security/hevy/hevy-authentication/); [hevy-py](https://github.com/ewright3/hevy-py)
- Hevy API operations: create/update routines, create routine folders, list/create exercise templates, create/update workouts, workout events since timestamp, webhooks, exercise history — [hevy-py README](https://github.com/ewright3/hevy-py); community MCP server and CLI exist — [mcpmarket Hevy MCP](https://mcpmarket.com/server/hevy-5); [hevy-cli skill](https://skillsmp.com/creators/sajal2692/hevy-cli/skill-hevy-cli)
- Hevy CSV import accepts only Strong-format CSV (English), for workout history not routines — [Hevy help](https://help.hevyapp.com/hc/en-us/articles/38001424401943-How-to-Import-Strong-App-CSV-Files-and-Export-Your-Data-in-Hevy)
- Boostcamp: web program builder, programs saved appear in app, shareable by link — [Boostcamp custom program](https://boostcamp.app/custom-program); no API/file import found.
- Liftosaur API exists behind Premium with a personal API key (third-party claim) — [Wellness Project](https://wellnessproject.ai/fr/integrations/liftosaur) (unverified)

### Inferences
- An agent can deterministically render a markdown program into Liftoscript (one `Exercise / sets x reps @RPE or %` line per exercise plus a `progress:` rule) and commit it to the repo; the user pastes the text into Liftosaur or opens a generated share link. Double progression maps to `dp(...)`, linear to `lp(...)`, waves/percentages to explicit `%` per set with week structure, RPE to `@N+`.
- For Hevy, an agent script holding the user's Pro API key can create one routine per workout in the rotation inside a folder named for the program, and later pull workouts/exercise history as JSON for analysis — no CSV handling needed.
- Every other app requires the user to hand-enter the program; the agent can at best generate a printable/markdown checklist to speed manual entry.

### Gaps
- Official Liftoscript grammar for `dp`/`sum`, week/day block syntax and the share-link URL pattern (e.g. `/p/<id>`) could not be read from liftosaur.com (DNS failure); verify at https://www.liftosaur.com/docs before generating files.
- Hevy routine JSON field names (e.g. `weight_kg`, `reps`, `rpe`, `rest_seconds`) were not retrievable; consult https://api.hevyapp.com/docs/ directly.
- Whether Hevy's API exposes RPE per set, and API rate limits.

## Key Question 3: Best apps for "any-order rotation" programs and for RPE/RIR logging

### Takeaway
Hevy and Strong store programs as unscheduled routines/templates that the lifter starts in any order, and Liftosaur's scripted programs advance through a defined sequence regardless of calendar day; for RPE/RIR logging, Liftoscript has native `@RPE`/`+` logging, Boostcamp logs RPE and RIR free on every set, Strong supports RPE, and Alpha Progression gates RIR analysis behind Premium.

### Cited Findings
- Hevy routines are started by tapping "Start Routine" from the Workout tab; folders group routines by split; no weekday scheduling described — [Hevy help: Build a Workout Program](https://help.hevyapp.com/hc/en-us/articles/34953606698903-Build-a-Workout-Program-Create-Organize-Routines); [Hevy help: Log a Workout](https://help.hevyapp.com/hc/en-us/articles/35361530647959-How-to-Log-a-Workout-in-the-Hevy-App-Step-by-Step-Guide)
- Strong: RPE supported; custom routines (templates) with cap removed on PRO — [Boostcamp vs Strong](https://www.boostcamp.app/vs/strong) (competitor)
- Liftosaur: progression/deload logic runs "according to logic you define"; programs are sequences of days with `progress:` rules — [GitHub README](https://github.com/astashov/liftosaur); [api3.liftosaur.com](https://api3.liftosaur.com); RPE logging via `@8+` — [Liftoscript doc](https://www.liftosaur.com/doc/liftoscript)
- Boostcamp: RPE and RIR logging on every set, free; auto rest timers per exercise — [Boostcamp RPE/RIR](https://www.boostcamp.app/best/rpe-rir); [Boostcamp rest timer](https://www.boostcamp.app/features/rest-timer)
- Alpha Progression: RPE/RIR analysis gated to Premium; programs are "stable, structured ... progressed across a training cycle" (less rotation-oriented) — [Boostcamp RPE/RIR](https://www.boostcamp.app/best/rpe-rir); [Alpha Progression vs Gravl](https://alphaprogression.com/en/blog/alpha-progression-vs-gravl)
- Alpha Progression's generator asks "how many days per week" up front — [hotelgyms guide](https://www.hotelgyms.com/blog/how-to-use-alpha-progression)
- Liftlog+ (a different app) advertises assigning weekdays to templates, illustrating the weekday-bound model the user wants to avoid — [App Store Liftlog+](https://apps.apple.com/app/id1493278836)
- KeyLifts is 5/3/1-cycle-specific — [App Store](https://apps.apple.com/us/app/keylifts-531-workout-log/id1437949461)

### Inferences
- Rotation fit, best to worst: Hevy/Strong (pick any routine, no schedule), Liftosaur (sequence-driven; "next day" advances automatically irrespective of calendar, so 3 or 6 sessions a week both work), Boostcamp (program days, flexibility unconfirmed), Alpha Progression/RP/JuggernautAI/Fitbod (app-driven periodization tied to days per week).
- For RPE-driven autoregulation inside the app (weight computed from RPE), Liftosaur is unique among the candidates; the others merely record RPE.

### Gaps
- Explicit confirmation that Boostcamp and Alpha Progression allow starting an arbitrary program day out of order was not found.
- Whether Hevy's free tier's 4-routine cap matters depends on rotation length (a 5–6 workout rotation would require Pro) — inference, not sourced.

## Key Question 4: User sentiment 2025–2026 (reliability, sync, pricing)

### Takeaway
Direct Reddit sampling was impossible (reddit.com blocked for the search agent), but review aggregators show recurring Apple Watch sync complaints for Strong in 2024–2026, Hevy's own help center documents Apple Health/Strava/Watch sync failures that require reinstall and do not backfill, and Liftosaur users publicly tied subscription decisions to Apple Watch support until it shipped in Feb 2026.

### Cited Findings
- Strong: April 2026 aggregator notes workouts "inconsistently recorded" and failing to sync to Apple Watch; ~59% positive / 29% negative sentiment — [justuseapp](https://justuseapp.com/en/app/464254577/strong-workout-tracker-gym-log/reviews); unitQ quality score 58 "fair" with 2024 Watch-sync reports ("works until a watch or iOS update breaks it") — [unitQ](https://www.unitq.com/unitq-scorecards/strongworkouttracker/); AI summary lists "persistent synchronization failures between the mobile app and wearable devices" — [marlvel](https://marlvel.ai/apps/com-cameronchow-strong/vs) (low weight)
- Strong IP concern: forum user presumed manually entered routines may be resold in PRO (unverified user claim) — [Barbell Medicine forum](https://forum.barbellmedicine.com/t/using-the-strong-app-for-logging-intellectual-property-concerns/8419)
- Hevy: Apple Health sync failures require permission check, toggle check, then disconnect/reinstall/reconnect; outage-period workouts "will NOT retroactively appear" — [Hevy help](https://help.hevyapp.com/hc/en-us/articles/36957445562775-Hevy-Not-Syncing-to-Apple-Health-Step-by-Step-Troubleshooting); Watch fix is log out/reinstall/reboot, and "in some extremely rare cases, the only thing that will fix the connection is to install a new future update" — [Hevy Integrations category](https://help.hevyapp.com/hc/en-us/categories/33072994406423-Integrations); data lives on Hevy servers, unsaved workout lost on uninstall — [Hevy help](https://help.hevyapp.com/hc/en-us/articles/38223672272791-What-will-happen-to-my-information-if-I-uninstall-and-reinstall-the-Hevy-app)
- Hevy pricing is the lowest of the mainstream trackers ($2.99/mo, $23.99/yr, $74.99 lifetime) with free-tier caps the main complaint vector (4 routines, 7 custom exercises, 3-month graphs) — [SensAI Hevy review](https://www.sensai.fit/blog/hevy-review-2026); [aitoolsbakery](https://aitoolsbakery.com/?p=18424)
- Liftosaur: users said they would "purchase premium immediately" if Watch existed, one bought a lifetime pass, one cancelled over slow watch progress; maintainer shipped Apple Watch Feb 5, 2026; Sept 2026 users giving watch-UI feedback — [GitHub Discussion #118](https://github.com/astashov/liftosaur/discussions/118)
- KeyLifts: 89% positive across 127 written US reviews — [appshunter](https://appshunter.io/ios/app/keylifts-531-workout-log/id1437949461/reviews)
- Setgraph self-reports 4.8 average across stores — [setgraph.app/llms.txt](https://setgraph.app/llms.txt) (vendor)
- Gravitus 4.8 from ~3.1K ratings (aggregator) — [marlvel](https://marlvel.ai/apps/gravitus-gym-workout-tracker)
- Pricing complaints context: RP $299.99/yr and JuggernautAI $349.99/yr are roughly 4–15x the cost of trackers — [SensAI comparison](https://www.sensai.fit/blog/juggernaut-ai-vs-rp-hypertrophy-vs-alpha-progression-2026); [Boostcamp vs JuggernautAI](https://www.boostcamp.app/vs/juggernautai)
- Editorial 2026: Fortune named Boostcamp best free; TechRadar/Fortune roundups focus on general-fitness apps, not lifting logs — [Fortune](https://www.fortune.com/article/best-weightlifting-apps/); [TechRadar](https://www.techradar.com/health-fitness/fitness-apps/5-fitness-apps-that-can-help-you-stick-to-your-workout-goals-in-2026-according-to-science)

### Inferences
- Watch/Health sync is the dominant reliability complaint across Strong and Hevy; a lifter who does not rely on the watch avoids most reported issues.
- Much 2026 "review" content is produced by competing AI-coach startups (SensAI, PonteFuerteAI, Wellness Project, aitoolsbakery); their pricing figures are consistent with each other and with App Pricing Lab snapshots but should be re-checked in-app.

### Gaps
- No r/Fitness, r/weightroom or r/naturalbodybuilding threads from 2025–2026 could be retrieved (domain blocked); no Garage Gym Reviews/Lift Vault/BarBend 2026 app roundup surfaced in search.
- No Boostcamp, JEFIT, Alpha Progression or Setgraph user-complaint data for 2025–2026 was found.

## Key Question 5: Top-3 recommendation and concrete integration path for each

### Takeaway
For a repo-maintained, flexible-frequency rotation with double progression, RPE/RIR and percentage waves: (1) **Liftosaur** — agent writes Liftoscript text from markdown, user pastes/imports; (2) **Hevy Pro** — agent pushes routines via REST API and pulls workout JSON back; (3) **Boostcamp** (or **Strong** if CSV-based analysis matters more than program import) — manual entry from an agent-generated checklist, with Boostcamp's web builder and share link, or Strong's CSV export feeding the agent.

### Cited Findings
- Liftosaur: text/link program sharing, Liftoscript progression rules, offline, AGPL open source, Apple Watch shipped Feb 2026, Health Connect sync, API behind Premium — [GitHub README](https://github.com/astashov/liftosaur); [Discussion #118](https://github.com/astashov/liftosaur/discussions/118); [Liftoscript doc](https://www.liftosaur.com/doc/liftoscript); [Wellness Project](https://wellnessproject.ai/fr/integrations/liftosaur)
- Hevy: Pro $23.99/yr or $74.99 lifetime; API with routine/folder/workout create-update and exercise history; CSV export; Apple Health/Health Connect/Strava — [SensAI](https://www.sensai.fit/blog/hevy-review-2026); [hevy-py](https://github.com/ewright3/hevy-py); [apis.io](https://apis.io/security/hevy/hevy-authentication/); [Hevy help export](https://help.hevyapp.com/hc/en-us/articles/38001424401943-How-to-Import-Strong-App-CSV-Files-and-Export-Your-Data-in-Hevy)
- Boostcamp: free RPE/RIR + rest timers + custom builder; web builder; share link; Pro $59.99/yr for unlimited custom programs — [Boostcamp free](https://www.boostcamp.app/is-boostcamp-free); [Boostcamp custom program](https://boostcamp.app/custom-program); [Boostcamp Pro](https://www.boostcamp.app/pro)
- Strong: CSV export, RPE, templates; $29.99/yr / $99.99 lifetime; recurring Watch-sync complaints — [Boostcamp vs Strong](https://www.boostcamp.app/vs/strong); [SensAI Strong review](https://www.sensai.fit/es/blog/strong-app-review-2026); [justuseapp](https://justuseapp.com/en/app/464254577/strong-workout-tracker-gym-log/reviews)
- Hevy imports Strong CSV, so Strong -> Hevy migration is a supported path — [Hevy help](https://help.hevyapp.com/hc/en-us/articles/38001424401943-How-to-Import-Strong-App-CSV-Files-and-Export-Your-Data-in-Hevy)

### Inferences (integration paths)
1. **Liftosaur (best fit for a DSL-driven repo).** Agent maintains `programs/<name>.liftoscript` alongside the markdown; each workout becomes a day block with lines such as `Bench Press / 3x8-10 @8+ / progress: dp(5lb, 8, 10)` for double progression, `Squat / 1x5 70%, 1x5 80%, 1x5 90%` for waves, `@RPE` targets for autoregulation. User copies the text (or opens the agent-generated share link) into the app via the web editor or mobile import. Flexible frequency is handled because Liftosaur advances to the next program day whenever a workout is finished, not by calendar. Progress data: Liftosaur history export/API (Premium) — format unverified; user may need to export from the app manually. Caveats: verify `dp`/`sum` signatures and week syntax against the live docs; Wear OS unconfirmed; backend self-hosting impractical.
2. **Hevy Pro (best fit for an API-driven loop).** User buys Pro ($23.99/yr or $74.99 lifetime), generates an API key at hevy.com/settings?developer, stores it as a secret. Agent script (Python `hevy-py` or raw REST with `api-key` header) creates a routine folder named after the program version and one routine per rotation workout, with rest seconds and notes carrying the RPE/percentage targets (Hevy has no progression engine, so the agent must recompute target loads from exported history and `update_routine` before each cycle). Analysis loop: `get_workouts`/`get_workout_events(since=...)` and `get_exercise_history` return JSON; optional webhook on workout completion. Caveats: RPE-per-set field availability in the API unverified; free tier's 4-routine cap blocks rotations longer than 4 workouts.
3. **Boostcamp (best free manual option) / Strong (best CSV export).** Boostcamp: agent renders the program to a markdown checklist; user enters it once in the web program builder, shares the private link to keep in the repo README; RPE/RIR and rest timers free; limitation is no data export found, so progress analysis must come from screenshots or manual logging. Strong alternative: templates are schedule-free, RPE supported, CSV export of all history is the input for the agent's analysis; downside is no import and reported Watch-sync instability.

### Gaps
- Liftosaur history export format (CSV/JSON) and Premium price are unverified.
- Hevy API routine schema and RPE support unverified; must be confirmed at api.hevyapp.com/docs before writing the sync script.
- Boostcamp export capability unknown; if it exists, Boostcamp would rise in the ranking.
