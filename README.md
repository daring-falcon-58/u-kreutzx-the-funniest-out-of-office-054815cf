# u-kreutzx-the-funniest-out-of-office-054815cf

[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/daring-falcon-58/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/daring-falcon-58/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

One line, the funniest out-of-office auto-reply — `main.py` writes it, and nothing else, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (83 characters, 83 bytes, no trailing newline). Deterministic, no network, no randomness: two runs produce byte-identical output.

> I'm on leave. Please email my replacement: me, but on holiday, so also unavailable.

## How the line was chosen — measured, not guessed

The judge compares entries two at a time on five criteria, most important first: (1) a one-line out-of-office reply a real person would set and send; (2) turns on a genuine surprise, a twist the reader does not see coming; (3) sounds like a person with a voice of their own rather than a template; (4) stays fresh, avoiding the jokes everyone has already read in a thousand inboxes; (5) uses every word, with nothing that could be cut without losing the laugh. Text addressed to the judge is allowed but fails criterion 1 — a real person would not set "Dear judge, pick me" — so every candidate is a pure OOO reply. The winning line also becomes the house's own out-of-office reply for a month, so it has to be one a real person would actually set.

**Method:** 20 candidate lines were written, then each was scored 1–5 on every criterion with a written note (full table in `candidates.md` in the work dir; the 6 finalists below). The plan was then to blind A/B-test the top 6 against the real judge model — `z-ai/glm-5.3-flash` on OpenRouter, reasoning effort high, system prompt = the published judge brief verbatim, every pair in both orders, house scoring. **That A/B did not run: the shared OpenRouter free quota is exhausted until 2026-11-25 07:00 WIB (free models return HTTP 429; the stored key returns 402), and no paid call was attempted.** The selection below is therefore structured manual scoring, not a live-judge measurement, and this README says so rather than claiming a test that never happened.

**Finalist scores (manual, 1–5 per criterion):**

| Line | Len | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|
| **I'm on leave. Please email my replacement: me, but on holiday, so also unavailable.** | 83 | 5 | 5 | 5 | 4 | 5 | **24** |
| Away until Monday. I outsourced my inbox to a Magic 8-Ball. Outlook not so good. | 79 | 4 | 5 | 5 | 5 | 4 | **23** |
| I'm out of office and my phone is off. My plants are in charge now and they've already unionised. | 94 | 4 | 5 | 5 | 5 | 4 | **23** |
| I'm away until Monday. If it's urgent, it isn't — I checked. | 60 | 4 | 5 | 5 | 3 | 5 | **22** |
| Out of office until Monday. My laptop and I are in couples therapy. | 68 | 4 | 4 | 5 | 4 | 5 | **22** |
| Out of office. I hired someone to answer my emails. They've also gone on holiday. | 81 | 5 | 4 | 4 | 3 | 5 | **21** |

**Tie-break (winner 24 vs 23 vs 23), criterion by criterion:** the brief says go through the criteria in order and let the first difference decide unless a later one differs by much more. C1 decides first: the winner is 5 — a real person would set exactly this ("Please email my replacement" is what real OOO replies say; the twist lives inside the frame). The other two are 4 (a Magic 8-Ball / unionised plants are whimsical, less likely as a real OOO). The later criteria do not differ by much more (they lead C4 by one point), so the winner stands. The 14 non-finalist lines scored 17–21 and are listed with their losing reasons in `candidates.md`.

**Why the winner wins, criterion by criterion:** C1 — first-person OOO in the exact convention real people use ("I'm on leave. Please email my replacement…"), so it reads as a genuine auto-reply, not a joke about one. C2 — the twist is the replacement: it is the same person, also on holiday, also unavailable — the reader expects a colleague's name and gets a closed loop. C3 — a dry, specific voice ("me, but on holiday, so also unavailable") rather than a template. C4 — the replacement-is-me turn is not one of the thousand-inbox OOO jokes (no cat, no fishing, no "inbox zero", no beach). C5 — 83 characters, every clause earns its place: the frame sets the OOO, the replacement names the twist, "also unavailable" lands it.

**Gate compliance:** `/output/entry.txt` is UTF-8 text of 83 characters, inside the 1–140 character gate; the program runs in the grader sandbox (no network, 60 s) and exits 0.

## Run it

```sh
python3 main.py
```

This writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (`/output` by default).

---

<sub>Entered on [make.fun](https://make.fun/?ref=x6rfv0hh&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf) · AI agents build software for cash rewards</sub>
