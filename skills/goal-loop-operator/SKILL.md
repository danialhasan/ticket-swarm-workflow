---
name: goal-loop-operator
description: Use when Danial gives a /goal-style long-running product outcome that should loop through discovery, implementation-contract materialization, dogfood QA, telemetry review, and blocker re-planning.
---

# Goal Loop Operator

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected next move is a broad product goal loop.

Use this skill when the user gives a durable product goal rather than one
already-scoped ticket.

Examples:

- "Use /goal to make May 13 dogfood actually ready."
- "Loop until first mission creation and execution works."
- "Find missing seams, create implementation contracts, dogfood, review
  telemetry, and repeat."
- "Run this while I go on a walk."

This skill is the outer goal runtime. It does not replace the ticket execution
skills. It decides which Ticket Swarm workflow to invoke next, keeps the goal
ledger honest, and prevents ambiguous residual risk from staying in prose.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

## Goal

Turn a broad outcome into a repeating governed loop:

```text
goal
  -> current truth snapshot
  -> missing seam discovery
  -> implementation contract / deferral / blocker
  -> dogfood product flow
  -> telemetry and proof review
  -> blocker ledger update
  -> next loop
```

The goal loop is complete only when the stated product outcome is proven,
explicitly blocked by a human/input dependency, or decomposed into owned
contracts with no unclassified residual risk.

When the goal depends on human product annotations, those annotations become
hard reconciliation objects. The loop may not shrink the claim boundary around
them after the fact.

## When To Prefer This Over Automation

Use `/goal` / this skill as the primary mechanism when the work needs judgment:

- selecting the next seam
- creating or reopening Linear implementation contracts
- distinguishing fixture proof from product proof
- using Browser/Computer/runtime/DB evidence
- spawning subagents for independent review
- changing status based on receipts
- stopping on human credentials, billing, consent, or release intent

Use a heartbeat automation only as a re-entry timer when the goal loop is
already defined. Automation wakes the thread; it does not own the goal.

## Required Inputs

- goal statement and target date, if any
- current repo path and branch
- active Linear parent/project, when applicable
- known blockers and prior receipts
- allowed writeback surfaces: filesystem, Linear, Slack, GitHub
- proof standard and forbidden claims
- loop count, time budget, or stop condition
- high-fidelity requirements map when the goal is still discovering or
  eliciting a product flow, mission setup path, governance model, generative UI
  surface, orchestration behavior, or eval/applied-AI proof standard

If any input is missing, make a conservative assumption and record it in the
goal ledger unless the missing input changes credentials, money, destructive
actions, or external visibility.

## First Move

Create or update one goal ledger under:

`docs/operations/sessions/<YYYY-MM-DD>/goal-loops/<slug>.md`

The ledger must include:

- goal statement
- target user-visible outcome
- forbidden claims
- active Linear topology
- current known blockers
- loop counter
- receipt directory
- stop conditions
- latest next action
- requirements-map path, or an explicit note that the current loop is execution
  against an already-accepted map

Do not start by creating a large plan in chat only. The ledger is the durable
state the next loop can resume from.

For discovery or elicitation loops, the first durable artifact is the
high-fidelity requirements map described in
`../references/high-fidelity-requirements-map.md`. It must aggregate context,
data exposure, canonical objects, commands, events, tools, UI surfaces, proof
surfaces, current implementation status, and human judgment packets before the
loop routes work into implementation contracts.

If the goal references live product annotations, browser comments, design review
notes, or Danial feedback, create or update an annotation reconciliation ledger
before implementation. Each annotation must have an id, route/surface, expected
product behavior, observed issue, owner rail, required proof, current status,
final disposition, and evidence link.

## Loop Phases

### 1. Rehydrate Truth

Read the goal ledger, current git status, relevant receipts, current code
surfaces, and live Linear state where available.

Classify each known blocker as:

- `work`: can be fixed by implementation or proof in this repo
- `contract`: needs a new or reopened implementation contract
- `rerun`: a QA gate can rerun after dependency proof
- `deferral`: explicitly out of dogfood scope with honest visible copy
- `human`: needs credentials, billing, consent, or release intent
- `unknown`: needs a discovery probe this pass

No blocker may remain as generic "risk."

For annotation-driven goals, no annotation may remain as generic `risk`,
`partial`, `unknown`, `outside golden path`, `broader scope`, or
`owned by contract`. Those are intermediate routing notes, not final
dispositions.

### 2. Discover Missing Seams

Use Browser as the local product truth rail. Use Computer only for native auth,
provider account chooser, protocol callback, installed app identity, updater,
relaunch, focus/window, or packaged behavior.

Look for:

- visible no-ops
- fixture/live blending
- missing route truth
- support-surface copy that does not come from the real read/command path
- missing telemetry
- missing durable readback
- missing DB/RLS proof class
- stale Linear status
- QA tickets marked Done while semantic receipt says PARTIAL/BLOCKED
- contracts that own readiness but not user repair

Also look for annotation downgrades:

- a visible product route classified as outside the golden path without proof
  the dogfood user cannot encounter it
- a human "should not exist" annotation treated as copy cleanup instead of
  removal, redirect, inaccessibility proof, or explicit Danial-approved deferral
- a visible seam closed as contract-owned while the user can still hit the
  unresolved surface
- a scope label that moves a Danial annotation out of the goal without a cited
  product decision

### 3. Choose The Next Workflow

Pick exactly one primary move for the loop:

- `$implementation-contract-conveyor` when a missing seam needs an owned child
  contract.
- `$ticket-to-human-review` when an existing implementation contract needs
  signoff before development.
- Direct `$multi-agent-workflow` plus `$layered-verification` when an existing
  signed contract is ready to execute.
- `$review-batch-orchestrator` when implementation exists and needs
  non-author review before proof.
- `$ticket-human-review-runtime` when machine proof is complete and the next
  gate is human product/runtime review.
- `$beta-release-assist` only after the human explicitly enters release work.
- `$feature-decision-ledger` when the discovered item is scope drift,
  non-goal, parking lot, or kill-list hygiene.

Do not run multiple primary moves in one loop unless one is purely read-only
supporting evidence for the other.

If an annotation ledger exists, choose the next workflow from the highest-risk
unreconciled visible row first. Do not prefer an easier golden-path proof while
known visible annotations remain unreconciled.

### 4. Execute Or Materialize

For the selected move:

- update Linear only after live readback
- keep file ownership clear
- write receipts before claiming progress
- run proof appropriate to the surface
- preserve secret hygiene
- record exact rerun gates unlocked or still blocked

### 5. Review Telemetry And Proof

For dogfood/product-flow loops, capture:

- Browser route/DOM/console proof
- Computer proof where native behavior is involved
- runtime command/query responses
- telemetry readback
- mission/session ids
- provider invocation ids
- DB/RLS proof class or explicit non-claim

Use subagents for independent lenses when the pass spans more than one seam:

- product visible-seam reviewer
- runtime/API/DB/telemetry reviewer
- contract/topology reviewer

Subagents return findings first, with file paths and blocker class.

### 6. Synthesize And Continue

Update the goal ledger with:

- pass number
- evidence paths
- blockers retired
- blockers discovered
- contracts created/reopened/proposed
- QA gates rerun or now eligible
- next action
- stop/continue decision

Then either continue the next loop or stop with one of:

- `goal-proven`
- `blocked-human`
- `blocked-external`
- `blocked-technical`
- `decomposed-to-contracts`
- `paused-by-user`

## Receipt Requirements

Each loop pass writes:

`docs/operations/sessions/<YYYY-MM-DD>/receipts/goal-loops/<slug>/pass-XX.md`

The receipt must include:

- pass number and timestamp
- current branch/worktree
- primary move selected and why
- Linear state read
- Browser/Computer/runtime/DB proof
- subagent review summaries
- blocker classification changes
- contracts created/reopened/proposed
- QA rerun gates changed
- next pass objective
- final status

For annotation-driven goals, each receipt must also include:

- annotation rows touched this pass
- rows retired with evidence
- rows still visible and unreconciled
- any Danial approval required before deferral
- proof that no row was closed as only `owned by contract`, `outside golden path`,
  `broader scope`, `partial`, `unknown`, or `risk`

## Close Rule

Do not claim the goal is done unless the ledger has no unclassified blockers
and the product-visible outcome has proof.

Do not claim `goal-proven`, `dogfood-ready`, or equivalent readiness while any
annotation row remains visible and unresolved, merely contract-owned, silently
scoped out, or classified as `outside golden path` without route proof and
Danial-approved deferral.

Do not let an automation, subagent, or status counter override the goal ledger.
The ledger is the source of truth for the loop.
