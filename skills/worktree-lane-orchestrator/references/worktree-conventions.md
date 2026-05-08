# Worktree Conventions

Use one consistent worktree layout for parallel ticket execution.

## Base assumptions

- `main` is the clean default base ref unless the operator explicitly chooses another merged base
- the root checkout remains the operator surface
- mutating lanes do not code in the root checkout

## Naming

- ticket root: `.worktrees/<ticket-id>/`
- integration worktree path: `.worktrees/<ticket-id>/integration`
- integration branch: `ticket/<ticket-id>/integration`
- lane worktree path: `.worktrees/<ticket-id>/<lane-slug>`
- lane branch: `ticket/<ticket-id>/<lane-slug>`

Examples:

- `ticket/SQD-884/integration`
- `ticket/SQD-884/implementation`
- `ticket/SQD-884/review-runtime`

## Ownership rules

- only mutating lanes get dedicated worktrees by default
- read-only lanes may stay in the root checkout or integration worktree
- if a review lane needs to boot the runtime or patch findings, treat it as a runtime or mutating
  lane and allocate a worktree
- installs, tests, builds, and local runtime commands run from the owning ticket worktree
- do not let two mutating lanes own the same file surface

## Runtime collision rules

Record these in the worktree matrix when relevant:

- renderer/api ports
- debug ports
- output directories
- shared temp paths
- env overrides
- Electron MCP verifier slot ownership

If collisions cannot be isolated cleanly, serialize that lane instead of forcing fake parallelism.

Electron MCP verification is one serialized resource across active ticket worktrees:

- only one verifier lane holds the Electron slot at a time
- other tickets may continue non-Electron work in parallel
- queue Electron verifier lanes instead of inventing parallel access

## Reconciliation rules

- lane worktrees feed back into the integration worktree
- the integration branch is the only default candidate for human verification and merge
- stale lane worktrees should not be deleted until their receipts are captured and the surviving
  branch is known
