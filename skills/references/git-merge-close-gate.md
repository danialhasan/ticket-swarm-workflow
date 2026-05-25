# Git Merge Close Gate

Use this reference when a ticket has cleared human review and is about to close.

## Core rule

`VERIFIED` from the human means:

- the ticket is approved to enter the merge gate
- it is **not** yet eligible for `Done`

The close sequence is:

1. human signoff is captured from the surviving ticket worktree
2. the surviving integration branch is reconciled if needed
3. that ticket branch is merged into local `main`
4. the required proof is rerun from root `main`
5. only after root `main` is green may `issue_tracker` move to `Done`

## Minimum mainline proof

At minimum, rerun tests from root `main`.

Default mainline proof for Squad tickets:

- lint
- typecheck
- test
- build

If the repo or active seam requires a stronger floor, use the stronger floor.

## Failure rule

If the merge lands on `main` but root-main proof fails:

- do **not** move the ticket to `Done`
- record that human signoff is already present but the mainline gate is red
- route the fix back into the ticket loop immediately
- rerun the root-main proof after the patch lands

Never let `Done` mean "human liked it, but main is red."

## Issue Tracker Rule

Human signoff and the `issue_tracker` terminal `Done` state are no longer the
same moment.

Use this split:

- after human `VERIFIED`: record the verdict, but keep the ticket out of `Done`
- after merge to `main` plus green root-main proof: move the ticket to `Done`
- after `PARTIAL` or `UNVERIFIED`: keep the ticket out of `Done` and route findings back into patching

## Batch rule

Even inside a grouped review wave:

- merge-to-main is still per-ticket
- root-main proof is still required before each ticket closes
- do not bulk-close a whole wave on the strength of shared human approval alone
