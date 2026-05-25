---
name: sequential-ticket-review-queue
description: Use when a bounded ticket set is already implemented and verified enough to enter one-by-one human signoff. Selects the review order, opens each surviving worktree in sequence, runs the human QA loop, captures verdict, merges verified work into main, reruns mainline proof, updates `issue_tracker`, and only then advances to the next ticket.
---

# Sequential Ticket Review Queue

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected next move is one-at-a-time human review and
closeout of already implemented, already verified ticket work.

Use this skill when the correct human-review posture is:

- one ticket at a time
- one surviving owner worktree at a time
- run it and validate it humanly
- sign off or bounce it back
- mark it done before moving to the next ticket

This is the lowest-level review operator for a tight delivery push.

Do not use this skill when:

- the real question is cross-ticket coherence across several slices at once
- multiple tickets still need to converge into one grouped human-review wave
- automated review or layered verification is still open on the current ticket

Read these only when needed:

- `../ticket-human-review-runtime/SKILL.md` when preparing the concrete runtime review surface
- `../ticket-to-human-review/SKILL.md` when contract signoff state is unclear
- `../review-batch-orchestrator/SKILL.md` only when deciding between sequential and grouped review
- `../ticket-human-review-runtime/references/review-surface-classification.md` when the human review mode is unclear
- `../references/git-merge-close-gate.md` when the exact post-signoff close rule matters
- `../references/outcome-first-skill-contract.md` for the compact plugin skill contract

## Goal

Turn a review-ready set into one explicit conveyor belt:

- pick the order
- review one ticket from its surviving worktree
- capture verdict
- route fixes if needed
- move `issue_tracker` only after human signoff, merge to `main`, and green root-main proof
- never advance to the next ticket while the current one is unresolved

## Ownership Split

Default operator split:

- the system owns queue state, worktree selection, runtime boot, artifact lookup, checklist prep,
  `issue_tracker` movement, and next-ticket advancement
- the human owns only product-truth judgment for the active ticket
- the human should answer only `VERIFIED`, `PARTIAL`, or `UNVERIFIED` unless a deeper note is
  actually needed
- when a ticket class is already known to be operator-only sanity veto, the system should keep
  moving proactively and interrupt the human only when a contradiction, ambiguity, or product-risk
  actually appears

Do not make the human drive:

- which ticket is next
- which commands to run
- which receipt to read first
- whether deploy belongs to this ticket
- when to move the queue forward

Default progression rule:

- do not wait for extra prompting between verified tickets
- after a ticket closes, the operator should immediately preflight the next ticket in queue
- if the next ticket is operator-only sanity veto, run the probes and prepare the disposition
- interrupt the human only for a real veto moment, not for routine queue movement

The point of this skill is to keep the human in a narrow review lane while the operator carries the
workflow burden.

## Inputs

- ordered candidate ticket set
- surviving worktree path and branch for each ticket
- closeout packet path for each ticket
- verification receipt path for each ticket
- runtime launch command for each ticket
- current `issue_tracker` state for each ticket
- desired terminal state after merge gate, default `Done`

## Review Order Rules

Default order:

1. review foundation tickets before tickets that mainly validate or consume their outputs
2. review write-path and canonical-truth tickets before telemetry, UI polish, or harness tickets that depend on them
3. review verification-fixture or acceptance-harness tickets last inside a bounded slice
4. if two tickets are independent, prefer the one that unlocks more downstream tickets first

For a public example bundle, the default review order is:

1. `ISSUE-101` `FLOW-H01` live API and shared contract spine unification
2. `ISSUE-102` `FLOW-A01` admission normalization scaffold
3. `ISSUE-103` `FLOW-E01` event append scaffold and ordering rules
4. `ISSUE-104` `FLOW-T01` telemetry emission scaffold and correlation conventions
5. `ISSUE-105` `FLOW-V01` shared flow verification fixtures and acceptance scaffolds

Only change that order if current dependency truth or runtime reality proves a different order is safer.

## Workflow

### 1. Freeze the queue

- choose the exact ticket list
- record the review order
- record each surviving worktree path
- record the runtime command for each ticket
- classify each ticket as `Operator-Only Probe`, `Operator-Led Sanity Veto`, `Human Runtime Review`, or `Bundle Coherence Review`

Do not begin review if any ticket lacks:

- a surviving worktree
- a closeout packet
- a verification receipt

### 2. Review one ticket only

For the active ticket:

1. open the surviving worktree
2. launch the truthful runtime from that worktree
3. choose the human interruption level from the classification
4. prepare the smallest useful review packet from `$ticket-human-review-runtime`
5. only if needed, give the human a tiny checklist, expected outcome, and ASCII or screenshot-backed visual map
6. capture one verdict when human review is actually required

Do not open the next ticket's review runtime yet.

DB-proof rule:

- before treating the active ticket as review-ready, decide whether it requires DB-backed proof
- if the ticket carries `needs:db-proof` or the seam clearly depends on durable canonical truth, the
  review packet must include the DB-backed verification receipt and completed `## DB Verification`
  checklist
- do not advance a ticket into final signoff on the strength of hermetic in-memory tests alone

Truthful-runtime rule:

- if the ticket is API-only or contract-only, do not route human review through scaffold desktop UI
- if the ticket is UI-facing, provide the smallest legible visual surface possible
- never make the human infer ticket truth from unrelated placeholder surfaces

Operator-only rule:

- when project or bundle audit already classifies the ticket as operator-only sanity veto, default to
  operator-led progression
- leave behind the runtime packet and receipts
- escalate to the human only if the live probes contradict the claimed seam, expose confusing product
  truth, or imply scope drift
- if the ticket is plain `Operator-Only Probe` and no contradiction appears, clear the same merge and proof gate operator-side, then advance the queue without waiting for a human verdict

### 3. Apply the gate

If verdict is `VERIFIED`:

- record the signoff note
- update the ticket's final human-review artifact
- merge the surviving ticket branch into local `main`
- rerun the required proof from root `main`
- only after root `main` is green, move the `issue_tracker` issue into its terminal done state
- record deploy separately later if and when release actually happens
- then advance to the next ticket

If verdict is `PARTIAL` or `UNVERIFIED`:

- stop the queue
- route findings back into the owner ticket worktree
- rerun automated review and verification as needed
- rerun human review on the same ticket
- do not advance to the next ticket until the current ticket is fully resolved or explicitly deferred

### 4. `issue_tracker` movement rule

`issue_tracker` state changes are part of the signoff and merge gate, not an afterthought.

Default rule:

- before signoff: ticket stays in its current active review-ready state
- after human `VERIFIED`: record the verdict, but keep the ticket out of `Done` until the merge gate clears
- after merge to `main` plus green root-main proof: move the ticket to `Done`
- after release: add a deploy comment, release receipt, or release label if needed, but do not
  reopen the ticket just to record deploy truth
- after `PARTIAL` or `UNVERIFIED`: keep it out of `Done` and record the blocker or follow-up truth

DB-backed close gate:

- if the ticket requires DB proof, do not move it to `Done` until the DB-backed receipt exists and
  the `## DB Verification` checklist is fully checked off
- if the code is otherwise ready but DB proof is still missing, keep the ticket in an active review
  state and record that the blocker is proof, not implementation
- if the human approved the ticket but root-main proof is still red after merge, keep the ticket
  out of `Done` and record that the blocker is mainline verification, not product QA

Do not bulk-close the whole review set at the end. Close each ticket immediately after its merge gate clears.
Do not treat human signoff alone as closure. Each ticket still owes a merge-to-main and green root-main gate.

### 5. Advance the queue

Only after the current ticket is signed off, merged to `main`, root-main proof is green, and `issue_tracker` is moved correctly:

- shut down or release its runtime if needed
- mark the queue pointer forward
- begin the next ticket from step 2

If the external tool write is temporarily blocked by auth or connector health:

- record the verified verdict locally
- keep the queue truth explicit
- retry the `issue_tracker` move as operator work
- do not force the human to babysit connector recovery

If the local review set is exhausted:

- return to the configured global execution queue, such as
  `<WORKSPACE_RECEIPT_ROOT>/execution-order.md`
- use live `issue_tracker` dependency truth to choose the next ready ticket in that order
- do not jump ahead to overlays or support artifacts just because they look locally free
- carry the same one-ticket-at-a-time signoff loop into that next ticket

For an early-slice queue, the global rule is:

- finish and sign off the active `<BUNDLE-A>` or equivalent foundation queue
- then continue to the next ready ticket in the configured `issue_tracker` queue
- do not jump later bundles with overlay or support work unless the queue source itself changes

## Close Rule

This skill is complete only when:

- the review order is explicit
- each reviewed ticket was opened from its own surviving worktree
- each ticket received a concrete human verdict
- each verified ticket was merged into `main`
- each verified ticket reran the required proof from root `main`
- each verified ticket that required DB proof had that proof completed before moving to `Done`
- each verified ticket was moved to `Done` before advancing
- no unresolved ticket was silently skipped

## Output

- one explicit review queue
- one signoff record per ticket
- one merge-to-main and root-main proof note per verified ticket
- one `issue_tracker` transition per verified ticket
- one stop point when a ticket fails review
- one explicit next-ticket handoff when the queue rolls back into the global `issue_tracker` order
