---
name: calendar-dag-scheduler
description: Use when today's real calendar availability needs to become a concrete ticket execution calendar backed by the issue-tracker dependency graph.
---

# Calendar DAG Scheduler

Use this skill when the question is:

- which ticket goes in which time block today
- how do we turn free windows into real execution blocks
- how do we respect dependencies instead of scheduling fantasy work
- how do we place grouped review and patch blocks into the day

This skill is the calendar-writing planner.
It does not itself decide ticket state transitions in the configured `issue_tracker`.
It hands those tickets to `linear-day-allocator`.

## Inputs to gather first

- local date and timezone
- today's `calendar_provider` events
- today's free windows
- candidate child issues from the active `issue_tracker` project
- parent/child relationship data
- dependency graph or blocker graph
- current issue state counts
- parallelism posture for the day
- any fixed review windows or meetings

Start by reading:

- `../ticket-day-operator/SKILL.md`
- `../parallel-lane-orchestrator/SKILL.md`
- `../review-batch-orchestrator/SKILL.md`

Use the configured `calendar_provider` and `issue_tracker` adapters. Examples include Google
Calendar or Outlook Calendar for `calendar_provider`, and Linear, Jira, GitHub Issues, or
Shortcut for `issue_tracker`.

## Goal

Produce one calendar-backed execution map for the current day:

- real free windows only
- one dependency-ready ticket or one explicit grouped block per window
- independent work scheduled in parallel where possible
- shared review and patch windows scheduled intentionally

## Workflow

### 1. Read calendar truth

- fetch all remaining events for the local day
- compute real free windows
- identify hard blocks versus movable holds

Rules:

- do not plan over existing hard commitments
- do not assume a fake 16-hour day if Calendar says otherwise
- preserve transition time around meetings when the day is fragmented

### 2. Filter the board to schedulable child work

- exclude parent issues
- exclude tickets blocked by unresolved upstream dependencies
- exclude tickets whose remaining work is too discovery-heavy for today's schedule
- include grouped review or patch blocks when the DAG says multiple tickets should converge

For each candidate, capture:

- ticket id
- state
- parent
- blockers
- likely effort
- unlock value
- whether it can run in parallel

### 3. Build execution waves from the DAG

Create one or more waves:

- Wave A: dependency-ready execution tickets
- Wave B: grouped review block for Wave A
- Wave C: patch and re-review tickets only if review is expected to surface findings
- later waves only if calendar capacity remains

Rules:

- do not place a downstream ticket before its blocker-clearing ticket
- parallelize only tickets that do not compete for the same critical file surface or runtime resource
- reserve at least one block for grouped review if multiple tickets are expected to hit review together

### 4. Map waves into calendar blocks

For each free window, assign exactly one of:

- one execution ticket
- one grouped review block
- one grouped patch block
- one replanning block if the day is highly uncertain

Rules:

- calendar titles must be legible and operator-facing
- include ticket ids directly in the block title when one ticket owns the block
- grouped blocks must name the wave and the participating tickets
- update an existing same-day block instead of duplicating it

### 5. Write the calendar plan

Create or update calendar blocks for the day.

Each block should carry:

- ticket id or grouped block label
- planned lane or wave
- intended outcome for the block
- any dependency note if relevant

## Close rule

This skill is complete only when:

- today's free windows were read from Calendar
- only dependency-ready child work was scheduled
- the day has explicit execution and review structure
- Calendar was updated or an auth blocker was surfaced honestly
