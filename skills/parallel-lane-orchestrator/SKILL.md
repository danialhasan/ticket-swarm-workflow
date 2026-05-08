---
name: parallel-lane-orchestrator
description: Use when multiple dependency-ready tickets can advance simultaneously and we need explicit execution waves, lane ownership, and serialized-resource rules before work starts.
---

# Parallel Lane Orchestrator

Use this skill when the question is:

- which tickets can run at the same time
- where are the true parallel lanes in today's DAG
- what resources force serialization
- how do we avoid review chaos later

This skill plans multi-ticket execution waves.
It should compose with `worktree-lane-orchestrator`, not replace it.

## Inputs to gather first

- selected tickets for today
- dependency graph
- known shared blockers
- file-surface overlap if already known
- runtime collisions and serialized resources
- expected review convergence points

Start by reading:

- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/worktree-lane-orchestrator/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/ticket-to-human-review/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/review-batch-orchestrator/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/references/git-merge-close-gate.md`

## Goal

Create one honest lane map for today's tickets:

- truly parallel tickets grouped together
- serialized tickets called out explicitly
- shared blockers and shared resources visible up front
- review convergence planned before execution begins

For DB-proof campaigns, the lane map must also keep frozen phase order stronger than "dependency-free
and looks easy." Do not let broad tagged sets blow up the slice.

## Workflow

### 1. Partition tickets into waves

Group tickets by dependency readiness:

- Wave A: no unresolved blockers
- Wave B: unlocks after Wave A
- later waves only when justified by today's capacity

For DB-proof campaigns:

- wave by frozen phase and bundle first, then by ticket-level blocker edges
- start with the proof-substrate and receipt-truth foundation squads
- then repair Bundle A before flowing into the rest of Phase 1
- only after that should later bundles enter active execution waves

### 2. Partition each wave into lanes

For each wave:

- group tickets that can run independently
- split tickets that would collide on the same critical surface
- mark any runtime-verification lane that must serialize

Typical serialized resources:

- Electron MCP verification
- one shared staging deploy surface
- one integration branch that cannot absorb multiple competing mutations safely
- one shared DB reset / local Supabase state surface when persisted-path proof would otherwise collide

### 3. Emit lane ownership

Every lane should include:

- owned tickets
- owner
- expected finish condition
- serialized resources
- review handoff condition
- merge-to-main handoff condition after human `VERIFIED`

For DB-proof campaigns, default lane families are:

- campaign director / trust-table lane
- proof-substrate lane
- receipt-truth lane
- ticket execution lanes by owning surface

### 4. Prepare review convergence

For each wave, declare:

- whether tickets will go to one grouped review wave
- whether any ticket must be reviewed alone
- which patch loop follows if review findings land

## Close rule

This skill is complete only when:

- today's tickets are grouped into honest parallel waves
- serialized resources are explicit
- lane ownership is explicit
- the execution map is clean enough for `worktree-lane-orchestrator` and `review-batch-orchestrator` to pick up next
- any ticket that will eventually close has an explicit path from review to merge-to-main instead of
  assuming human signoff equals `Done`
