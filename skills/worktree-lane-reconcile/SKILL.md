---
name: worktree-lane-reconcile
description: Use after lane review and verification to collapse parallel lane work back onto one surviving integration branch/worktree and record cleanup posture before human verification and the later merge-to-main close gate.
---

# Worktree Lane Reconcile

Use this skill after the implementation, review, patch, and verification lanes have finished for a
ticket that used parallel worktrees.

This skill does not replace human verification and does not silently delete evidence.

## Inputs to gather first

- ticket id
- integration branch and integration worktree path
- worktree matrix receipt
- lane receipts
- current branch status for each lane
- review findings and patch status
- verification verdict per lane where relevant

Start by reading:

- the worktree matrix receipt
- `references/reconcile-checklist.md`
- `../references/git-merge-close-gate.md`

## Workflow

### 1. Inspect surviving lane state

For every lane branch/worktree, determine:

- whether the lane produced code
- whether its findings were accepted
- whether its changes are already integrated
- whether the lane still needs to be preserved for follow-up review

### 2. Choose one surviving integration candidate

The default surviving candidate is the integration branch/worktree created at kickoff.

If the integration candidate changed, record why.

Do not leave human verification with multiple equally valid branch candidates.

### 3. Record reconciliation order

If multiple lane outputs must still be combined, record the exact order:

- merge or cherry-pick target
- branch order
- any file-surface or proof dependencies

If there is unresolved overlap, do not hide it. Mark the ticket `PARTIAL` until reconciled.

### 4. Mark cleanup posture

For each lane worktree, record one state:

- `keep for follow-up`
- `ready for cleanup after merge gate`
- `already reconciled and removable`

Do not delete worktrees automatically inside this skill. The goal is explicit cleanup posture, not
silent mutation.

### 5. Emit the reconciliation receipt

Produce one receipt with:

- surviving integration branch
- surviving integration worktree path
- reconciled lane branches
- unreconciled lane branches
- exact cleanup posture per lane worktree
- any operator action still required before human verification
- any operator action still required before the later merge-to-main close gate

## Close rule

This skill is complete only when:

- there is one clear surviving branch/worktree for the ticket
- all lane worktrees have an explicit cleanup posture
- the reconciliation receipt exists
- the surviving branch is explicit enough to hand to the post-signoff merge gate
