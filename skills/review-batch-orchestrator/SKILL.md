---
name: review-batch-orchestrator
description: Use when multiple tickets are expected to converge into one shared human-review wave, followed by patch and re-review loops that should stay synchronized instead of ad hoc.
---

# Review Batch Orchestrator

Use this skill when the question is:

- how do we review multiple tickets in one wave
- when do grouped review and grouped patch blocks happen
- how do we keep patch and re-review from becoming random ticket-by-ticket churn

This skill is the review-wave planner for a multi-ticket day.

If the correct review posture is not a grouped wave but a strict one-by-one signoff conveyor belt,
route to `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/sequential-ticket-review-queue/SKILL.md`
instead.

## Inputs to gather first

- current execution waves
- tickets expected to reach review today
- ticket owners
- human-review availability
- known serialized review surfaces
- patch expectations or likely risk areas

Start by reading:

- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/ticket-human-review-runtime/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/ticket-to-human-review/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/parallel-lane-orchestrator/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/references/git-merge-close-gate.md`

## Goal

Produce one streamlined review wave:

- grouped review when multiple tickets are ready together
- explicit patch wave when findings land
- explicit re-review wave when patches settle
- explicit post-signoff merge gate per verified ticket

For DB-proof campaigns, grouped machine review is the default, but human review should stay
isolated to only the tickets whose classified surface genuinely needs a human verdict.

## Workflow

### 1. Build the review set

Collect tickets that are likely to hit review in the same day window.

Rules:

- do not group tickets that depend on unresolved upstream work
- do not mix unrelated review contexts if that would confuse the human reviewer
- for DB-proof campaigns, keep receipt-truth corrections grouped with their matching proof wave so
  the trust story cannot drift ahead of the substrate

### 2. Decide grouped versus isolated review

Use grouped review when:

- several tickets belong to the same execution wave
- the same human can review them in one pass
- the risk is coherence and convergence, not just single-ticket correctness

Use grouped machine review plus isolated human review when:

- many tickets share the same proof substrate or receipt repair wave
- only a subset actually exposes a human runtime surface
- the human should not babysit operator-only or API-only tickets

Use isolated review when:

- one ticket is much riskier
- one ticket owns a separate runtime surface
- one ticket is not ready with the rest of the wave

Use sequential signoff queue when:

- the human wants to finish one ticket fully before touching the next
- each ticket has its own surviving worktree and should be validated there
- merge-to-main and Linear `Done` should happen ticket by ticket instead of after one shared wave
- the main risk is operator focus and honest closure, not cross-ticket coherence

### 3. Plan the patch loop

For grouped review findings:

- route each finding back to the owning ticket lane
- batch patch time into one explicit patch wave
- avoid scattering micro-patches throughout the rest of the day
- if a DB-backed proof lane fails, patch the substrate or receipt truth once, then fan the rerun
  back across the affected ticket set instead of treating each ticket as a bespoke failure

### 4. Plan re-review

After the patch wave:

- schedule a grouped re-review if multiple tickets changed
- schedule isolated re-review only when one ticket remains unstable
- after a ticket clears human review, keep its merge-to-main and root-main proof gate explicit
- do not treat a grouped human wave as permission to bulk-close tickets before main is green

## Close rule

This skill is complete only when:

- the review set is explicit
- grouped versus isolated review is justified
- patch follow-through is scheduled intentionally
- the re-review path is explicit rather than implied
- the post-signoff merge gate is explicit instead of being hand-waved into `Done`
