---
name: ticket-swarm-router
description: Use first when a Ticket Swarm goal, ticket, annotation set, or execution day needs the smallest correct next workflow skill selected without loading the whole plugin.
---

# Ticket Swarm Router

Use this skill as the first stop for Ticket Swarm work unless the user named a
more specific skill and the current state already proves that skill is the next
move.

This is a routing skill, not an execution skill. Its job is to keep the plugin
GPT-5.5-native: outcome first, smallest sufficient context, one selected next
workflow, clear proof, and no ceremony for its own sake.

## Goal

Pick the smallest correct next workflow:

```text
goal / ticket / annotation / day state
  -> current truth
  -> blocker and dependency class
  -> selected next skill
  -> required inputs
  -> stop condition
```

The router is complete when it can name exactly one primary next skill, why that
skill is needed, what must be true before it runs, and what receipt it must
leave behind.

## When To Use

- The user gives a broad `/goal` or mission packet.
- A ticket swarm needs sequencing, parallelism, review, or verification.
- Human annotations need reconciliation before readiness can be claimed.
- A workflow feels too dense and the next move should be selected by condition.
- Multiple Ticket Swarm skills could apply and loading all of them would crowd
  the working context.

## When Not To Use

- The user explicitly asks for one named skill and the required inputs are
  already present.
- The task is a tiny local edit with no workflow ambiguity.
- A downstream skill is already active and has a concrete next command.

## Required Inputs

- User outcome or ticket objective.
- Current state: repo, branch, Linear/topology if relevant, annotations,
  blockers, receipts, and verification status.
- Product proof standard: what counts as done, what claims are forbidden, and
  what evidence must exist.
- Requirements-map standard: when the selected move is discovery or
  elicitation, the output must be a high-fidelity requirements map with data
  exposure, context aggregation, proof surfaces, diagrams, current-state status,
  and human judgment packets. Use
  `../references/high-fidelity-requirements-map.md`.
- External boundaries: credentials, billing, consent, release visibility, or
  third-party actions.

If an input is missing, make the conservative assumption only when it does not
affect credentials, money, destructive actions, external visibility, or a human
product decision. Otherwise stop and ask.

## Routing Table

Choose one primary skill:

| Condition | Primary Skill |
| --- | --- |
| Broad product outcome must loop until green, blocked, or deferred | `$goal-loop-operator` |
| Human UI/product annotations must become hard reconciliation rows | `$annotation-reconciliation-guard` |
| Repeated UI abstraction failure should be caught without more manual annotation | `$ui-abstraction-guard` |
| Approved design/readiness rows need an implementation contract | `$implementation-contract-conveyor` |
| Implementation contract needs human signoff before execution | `$ticket-to-human-review` |
| Multiple dependency-ready tickets can run independently | `$parallel-lane-orchestrator` |
| One ticket needs mutating parallel worktrees | `$worktree-lane-orchestrator` |
| Parallel worktree lanes need collapse and proof reconciliation | `$worktree-lane-reconcile` |
| Implemented tickets need grouped non-author review | `$review-batch-orchestrator` |
| Implemented tickets must be reviewed one by one with human validation | `$sequential-ticket-review-queue` |
| Machine proof is complete and the next gate is human product/runtime review | `$ticket-human-review-runtime` |
| A day plan must be built from board pressure and calendar reality | `$ticket-day-operator` |
| Calendar windows need scheduling into real execution blocks | `$calendar-dag-scheduler` |
| Execution windows need concrete Linear allocation | `$linear-day-allocator` |
| A blocker cleared or slipped and the day plan must be reflowed | `$day-state-updater` |
| Feature ideas need beta thesis, non-goal, parking-lot, or kill-list hygiene | `$feature-decision-ledger` |
| Squad agent behavior, prompt/tool manifests, eval traces, trajectories, datasets, or harness failures need dataset-backed repair | `$squad-harness-engineering` |
| Design review must become approved design contract rows | `$design-contract-conveyor` |
| Human explicitly enters release handoff after development proof | `$beta-release-assist` |
| Mission-shaped intent needs ontology, epistemology, source authority, or context graph discovery before definition | `$mission-context-discovery` |
| User is defining, revising, approving, or starting a mission from Chat or Mission mode | `$mission-definition-conveyor` |
| Active mission task needs autonomous implementation, review, verification, and receipts | `$mission-task-operation` |
| User or UI needs Mission Overview, mission card, progress, transcript, or governance readback | `$mission-overview-readmodel` |
| Completed, blocked, or terminated mission needs human outcome review and feedback capture | `$mission-review-loop` |

If two skills look equally valid, pick the one closest to the current blocker.
Do not load downstream skill files until the router has selected the primary
move.

## Output Shape

Return or write a short routing note:

```text
Outcome:
Current truth:
Primary blocker:
Selected skill:
Why this skill:
Required inputs:
Required requirements-map output:
Stop condition:
Receipt path:
Next action:
```

## Stop Condition

Stop routing and ask Danial only when:

- the next move changes product scope;
- a visible user-facing surface would be deferred;
- credentials, billing, consent, destructive action, or external release is
  required;
- no skill matches the blocker without inventing a new workflow.

Otherwise select the skill and continue.
