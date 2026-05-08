# Lane Handoff Receipts

Use these receipt shapes so every ticket leaves behind comparable evidence.

## Canon brief receipt

- ticket id
- controlling canon refs
- obligations preserved
- open questions not resolved here
- done signal

## Worktree matrix receipt

- ticket id
- base checkout path and branch
- integration branch and worktree path
- per-lane branch and worktree path
- lane owner
- lane type: mutating / runtime review / read-only
- owned file surfaces
- reserved ports or env notes
- any serialized overlaps

## Implementation receipt

- files touched
- primary seam implemented
- RED surface that existed before the change
- summary of the GREEN change

## Review findings receipt

- reviewer
- blocking findings
- non-blocking findings
- canon or architecture drift observed

## Patch receipt

- findings addressed
- any findings intentionally deferred
- reviewer signoff regained

## Verification receipt

For each layer:

- layer name
- command or check
- what it protects
- result
- reason if not required

## Worktree reconcile receipt

- surviving integration branch
- surviving integration worktree path
- reconciled lane branches
- unreconciled lane branches
- cleanup posture per lane worktree
- any operator action still required before merge or human verification

## Closeout receipt

- final status: VERIFIED / PARTIAL / UNVERIFIED
- user relief now available
- residual risk
- downstream tickets unblocked
- any follow-on work that should become a new ticket rather than hidden scope
