# Portability

Last updated: 2026-10-21

How to move this project from one Claude account to another (for example, off a
work account) without losing anything. The rule that makes it possible: **the
GitHub repository is the only source of truth.** The Claude account holds only
settings that can be recreated from this file.

## What lives where

| Item | Lives in | Moves with the repo? | What to do on a move |
| --- | --- | --- | --- |
| Research, guide, templates, tools, `CLAUDE.md` | GitHub repo `tlee-ui/WorkoutTrainer` (personal GitHub account) | Yes | Nothing |
| Training log and track state (`data/`) | GitHub repo | Yes | Nothing |
| Link between Claude and GitHub | Claude account (GitHub connection and Claude GitHub App) | No | Connect GitHub from the new Claude account |
| Cloud environment: network access, Hevy secret | Claude account (environment settings) | No | Recreate from the spec below |
| Hevy API key | Hevy account, plus a copy in the old environment | Key: yes. Copy: no | Regenerate the key, store it in the new environment |
| Session transcripts, artifacts, scheduled tasks, memory | Claude account | No | Nothing to move if the rules below are followed |
| `Claude-Session:` links in commit messages | Claude account | No | None. They stop opening from another account; the commits are unaffected |

## Environment spec

Recreate this in the new account's cloud environment settings (the environment
menu in a session's title bar, then Edit).

| Setting | Value |
| --- | --- |
| Repository | `tlee-ui/WorkoutTrainer` |
| Network access | Allow `api.hevyapp.com`. Research sessions also need web search and fetch. |
| Hevy credential | A network secret for `api.hevyapp.com` that sends the key in the `api-key` header. Alternative: an environment variable named `HEVY_API_KEY`. `tools/hevy_pull.py` works with either. |
| Setup script | None. The tools are Python 3 standard library only. |
| Connectors | None. The project does not use Gmail, Calendar, Drive, or any other connector. |

Never paste the key into a chat, a file in the repo, or a commit.

## Migration checklist

1. Confirm everything is pushed: `git status` is clean and every branch you
   want is on GitHub. Merge working branches into the default branch.
2. In the new Claude account, connect GitHub at `https://claude.ai/connect-github`
   and give the Claude GitHub App access to `tlee-ui/WorkoutTrainer`.
3. In Hevy, generate a new API key at `https://hevy.com/settings?developer`.
4. Create the cloud environment from the spec above and add the new key.
5. Start a session and check the link:
   `python3 tools/hevy_pull.py --inspect` should print one workout.
6. Recreate any scheduled tasks you still want (list them in the old account
   first; their prompts are not stored in the repo).
7. In the old account: delete the environment (removes the old key copy),
   delete scheduled tasks, and disconnect GitHub or remove the repo from the
   Claude GitHub App's access. Revoking the old Hevy key is optional once the
   new one works.

Steps 2 to 5 are the whole move. Expect about 15 minutes.

## Rules that keep it portable

- Anything worth keeping goes in the repo and is pushed. Not in an artifact, a
  chat, memory, or only a scheduled task's prompt.
- If a scheduled task is worth keeping, record its schedule and prompt in
  `PORTABILITY.md` under "Scheduled tasks".
- Credentials come from the environment, never from files in the repo.
- No dependency on work connectors or work systems.
- New setup steps (packages, hosts, secrets) are added to the environment spec
  above in the same commit that needs them.

## Scheduled tasks

None yet.

## Running without Claude

The repo works on any machine with Python 3:

```bash
git clone https://github.com/tlee-ui/WorkoutTrainer.git
cd WorkoutTrainer
HEVY_API_KEY=... python3 tools/hevy_pull.py
python3 tools/analyze_history.py
```
