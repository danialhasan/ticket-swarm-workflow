---
name: day-state-updater
description: Use when today's execution day is already in motion and calendar blocks, Linear due-work, and review waves need to be reflowed because a blocker cleared, a lane slipped, or review landed differently than planned.
---

# Day State Updater

Use this skill when the question is:

- what changes now that a lane slipped
- how do we reflow the rest of the day without manual chaos
- which tickets stay in scope and which fall out
- how should Calendar and Linear be updated after reality moved

This skill is the live replanning loop for an active day.

## Inputs to gather first

- current calendar blocks for today
- current selected tickets
- latest ticket states in Linear
- latest blocker graph
- review results if a review wave already happened
- remaining free windows for the day
- any deploy-seam or runtime constraint discovered mid-day

Start by reading:

- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/calendar-dag-scheduler/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/linear-day-allocator/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/review-batch-orchestrator/SKILL.md`

Use Calendar and Linear through Composio.

## Goal

Reflow the active execution day honestly:

- remove stale assumptions
- keep dependency-ready work in motion
- update Calendar blocks
- update Linear due-work and ownership if the day changed materially

## Workflow

### 1. Detect a replanning trigger

Typical triggers:

- a lane misses its expected finish block
- a blocker clears early
- grouped review finds more patch work than expected
- a deploy or runtime seam fails
- calendar capacity shrinks because of new meetings

### 2. Recompute remaining capacity

- read remaining events and free windows
- drop elapsed blocks from the plan
- recompute what can still fit today

### 3. Recompute schedulable work

- promote newly unblocked tickets if they are now dependency-ready
- demote slipped or newly blocked tickets
- preserve work already in motion when it still makes sense

### 4. Rewrite the remaining day

- update existing calendar blocks where possible
- move grouped review or patch blocks if their inputs slipped
- drop fantasy closes that no longer fit

### 5. Reflect material changes in Linear

When the selected set changed materially:

- add due dates or assignments for newly promoted tickets
- remove today ownership only when the operator policy calls for it
- keep a short operational note if the wave changed substantially

## Close rule

This skill is complete only when:

- the trigger was made explicit
- remaining capacity was recomputed from real Calendar state
- the rest of the day was reflowed honestly
- Calendar and Linear were updated or a blocker was surfaced cleanly
