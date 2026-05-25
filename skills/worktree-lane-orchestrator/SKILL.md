---
name: worktree-lane-orchestrator
description: Use when a ticket will execute with parallel mutating lanes and needs explicit git worktree and branch isolation before multi-agent execution starts.
---

# Worktree Lane Orchestrator

Use this skill after the seam is locked and the lane map exists, but before RED-first implementation
begins.

This skill turns “target worktree/branch alignment” from an implied requirement into one explicit
artifact.

Do not use this skill when:

- the ticket is staying single-lane in one clean checkout
- no mutating parallel lanes are planned
- the work is still broad enough that the lane map is unstable

## Inputs to gather first

- ticket id
- ticket title or short seam slug
- base ref for the ticket start, defaulting to `main`
- lane map with lane names, owners, and file surfaces
- which lanes are mutating, runtime-booting, or read-only
- any reserved ports or env collisions that need lane isolation
- any serialized runtime resources, especially `ui_automation_driver` verification
- receipt destination

Start by reading:

- `references/worktree-conventions.md`
- the lane map produced by the parent workflow

Use the helper only when needed:

- `plugins/ticket-swarm-workflow/scripts/ticket_worktree.py`

## Workflow

### 1. Confirm the base checkout is safe

- confirm the root checkout is on the intended base ref
- confirm the root checkout is clean before spawning mutating lane worktrees
- stop if the ticket is trying to start from a dirty root checkout without an explicit reason

The root checkout stays the operator and integration surface. Do not use it as a mutating lane
workspace once parallel execution starts.

### 2. Create the integration worktree first

Create one integration branch and one integration worktree for the ticket.

Default convention:

- branch: `ticket/<ticket-id>/integration`
- path: `.worktrees/<ticket-id>/integration`

This is the only branch/worktree that should survive the lane fan-out by default.

### 3. Create lane worktrees only where they buy isolation

For each mutating lane, create a dedicated lane branch and lane worktree.

Default convention:

- branch: `ticket/<ticket-id>/<lane-slug>`
- path: `.worktrees/<ticket-id>/<lane-slug>`

Rules:

- mutating lanes always get their own worktree
- a review lane gets its own worktree only if it needs to boot the app, run code, or patch
- canon extraction and closeout lanes stay read-only and do not need dedicated worktrees
- if two lanes want the same file surface, do not create competing worktrees for that overlap;
  serialize the surface instead

### 4. Reserve runtime collisions up front

Record any lane-local runtime constraints in the worktree matrix:

- dev server ports
- debug ports
- output directories
- environment variables that must differ per lane
- exclusive runtime resources such as `ui_automation_driver` verification

If two lanes would collide at runtime, stop and re-scope before implementation starts.

Rules:

- installs, tests, builds, and local runtime commands for a ticket run from that ticket's worktree
- `ui_automation_driver` verification is serialized even when tickets otherwise execute in parallel
- if multiple tickets need `ui_automation_driver` proof, queue those verifier lanes instead of running them together

### 5. Emit the worktree matrix receipt

Produce one receipt that becomes a required input to `multi-agent-workflow`.

The worktree matrix must include:

- root checkout path and current branch
- integration worktree path and branch
- one row per lane with:
  - lane name
  - owner
  - lane type: mutating / runtime review / read-only
  - branch
  - worktree path if any
  - owned file surfaces
  - reserved ports or env notes
  - serialized runtime notes, if any
- unresolved collisions or serialization notes

## Default output

- one integration worktree
- zero or more lane worktrees
- one worktree matrix receipt

## Close rule

This skill is complete only when:

- every mutating lane has a dedicated branch/worktree or an explicit serialization note
- the root checkout is no longer carrying mutating lane work
- the worktree matrix receipt exists
