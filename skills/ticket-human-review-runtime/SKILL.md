---
name: ticket-human-review-runtime
description: Use when a Squad ticket is already through automated review and verification and needs a human product-QA runtime. Prepares the surviving worktree, launches the right dev surface, provides the human review checklist, and routes any findings back into the owner ticket loop without using root main as the review workspace.
---

# Ticket Human Review Runtime

Use this skill when a ticket is ready for human product QA and we need a concrete review surface instead of a generic "please inspect this" handoff.

This skill does not replace automated review or machine verification. It starts only after:

- non-author review swarm is closed
- layered verification is closed
- one surviving integration worktree exists for the ticket

Read these only when needed:

- `../worktree-lane-reconcile/SKILL.md` when the surviving review worktree is unclear
- `references/review-modes.md` when choosing between ticket review and bundle review
- `references/review-surface-classification.md` when deciding whether the ticket even deserves human runtime review
- `../references/git-merge-close-gate.md` when the operator needs the exact post-signoff close rule

## Goal

Turn a review-ready ticket into one honest human QA session:

- the right worktree is selected
- dependencies are installed
- the correct runtime is launched
- the human gets a legible checklist
- any finding is routed back to the owning ticket worktree and patch loop
- a `VERIFIED` verdict leaves behind a merge candidate, not an auto-closed ticket

## Inputs

- ticket id and title
- surviving integration worktree path and branch
- closeout packet path
- verification receipt path
- QA guide path if one exists
- runtime surface type:
  - desktop or Electron
  - full-stack desktop plus API
  - API-only or non-UI
- expected user-relief sentence
- known residual risks

## Review Posture

- Human review is product QA, not code review cleanup.
- Default review unit is one ticket in its surviving integration worktree.
- Do not review from root `main`.
- Do not merge in-progress ticket worktrees into root `main` for review.
- If you need cross-ticket coherence review, use a temporary review branch/worktree, not `main`.
- Even in bundle review mode, findings still route back to the owning ticket worktree for patching.

### Human lane rule

The operator should shrink the human task aggressively.

- operator owns runtime boot, route prep, artifact lookup, and checklist construction
- operator should provide screenshots or ASCII maps when the runtime surface is not self-explanatory
- human should focus on "does this feel true and bounded?" rather than rediscovering workflow state
- human verdict should usually be one word: `VERIFIED`, `PARTIAL`, or `UNVERIFIED`

If the human starts asking what to click, what ticket is next, or what this screen is supposed to
prove, the operator handoff is not good enough yet.

## Workflow

### 1. Assert prerequisites

Before launching runtime review, confirm:

- automated review lanes reported zero blocking findings
- verification receipt exists
- touched-scope lint, typecheck, test, and build passed
- the surviving integration worktree is explicit

If any of these are missing, do not start human review yet. Route back into the ticket loop.

### 2. Classify the review surface first

Before booting anything, classify the ticket using `references/review-surface-classification.md`.

Default rule:

- if the ticket is `Operator-Only Probe`, do not ask the human to review it unless a contradiction appears
- if the ticket is `Operator-Led Sanity Veto`, give the human one tiny veto question only
- if the ticket is `Human Runtime Review`, continue with normal runtime prep
- if the ticket is `Bundle Coherence Review`, do not pretend one ticket-local runtime is enough

### 3. Choose review mode

Default to `ticket mode`.

`ticket mode`
- Use the surviving integration worktree for one ticket.
- This is the normal path.
- Use when validating bounded user relief and ticket-local runtime behavior.
- For API-only, contract-only, or backend-spine tickets, the truthful review surface is the API
  packet, live endpoint probes, or contract receipts, not the desktop shell.
- Do not launch the desktop app for those tickets just because it exists in the worktree.

`bundle mode`
- Use only after ticket-level automation is closed and the review question is cross-ticket coherence.
- Create a temporary review branch/worktree.
- Merge ticket integration branches there in dependency order.
- Never treat bundle mode as the owner patch surface.

See `references/review-modes.md` when the correct mode is unclear.

### 4. Bootstrap the review runtime

From the selected review worktree:

1. Run `pnpm install` if dependencies may be stale.
2. Choose the narrowest truthful dev command:
   - `pnpm dev` for full-stack desktop plus API review
   - `pnpm dev:desktop` for desktop-only review
   - `pnpm dev:api` for API-only runtime inspection
3. If the ticket depends on Supabase-backed local runtime, ensure the repo's normal dev entrypoint handles it or start the required local services explicitly.

DB-proof prep rule:

- decide explicitly whether this ticket needs DB-backed proof before you hand anything to the human
- if the seam touches durable canonical truth, prefer the Supabase-backed path over an in-memory
  fallback for the review runtime
- if only hermetic in-memory tests ran so far, treat the ticket as not yet ready for final signoff
- when the ticket uses live Linear review routing, keep the `needs:db-proof` label and `## DB Verification`
  block aligned with the actual runtime proof

Preferred default for user-facing tickets: `pnpm dev` from the review worktree root.

## 5. Build the human checklist

Give the human one small review script, not a prose dump.

The checklist should include:

- what user relief should now be real
- what window, route, or entrypoint to open
- the exact path to click through
- what green state should appear after each meaningful step
- what would count as a blocker
- what known residual risk is intentionally out of scope

For UI or Electron tickets:

- use the Electron verifier lane output from layered verification as the base script
- translate it into a human-readable checklist
- include one screenshot-backed or ASCII-backed orientation block when the UI is still scaffold-like
- keep the checklist concrete enough that a person can follow it without reading code

For API-only tickets:

- do not substitute a scaffold desktop shell for the real review surface
- show the exact request/response or endpoint behavior the ticket changed
- keep the human question at the contract level: "does this fail honestly and succeed cleanly?"
- if durable truth is part of the claim, include the DB-backed query or receipt that proves the
  response is sourcing persisted state instead of only an in-memory adapter

### 6. Run human QA

The human checks:

- does the product surface feel real instead of placeholder-shaped
- does the path match the user-relief claim in the closeout
- does anything confusing, misleading, or fake appear in runtime
- do the receipts match what the runtime actually does

The human is not expected to inspect diffs or reason about architecture here.
Human review does not close the ticket by itself; the merge-to-main gate still happens after this skill.

### 7. Record verdict

Capture one final outcome:

- `VERIFIED`
- `PARTIAL`
- `UNVERIFIED`

If not `VERIFIED`, record:

- exact reproduction steps
- expected behavior
- observed behavior
- screenshot or runtime evidence path when useful
- owning ticket id
- whether the finding is blocking or follow-up

### 8. Route findings back correctly

If the human finds a problem:

- patch in the owning ticket worktree
- rerun automated review and layered verification
- rerun human review in the same owner worktree

If review happened in `bundle mode`, do not patch only in the bundle review worktree. Replay the fix into the owner ticket worktree first, then refresh the bundle review surface if still needed.

## Close Rule

This skill is complete only when:

- one explicit review runtime was chosen
- the runtime was bootstrapped from the correct worktree
- the human had a concrete checklist
- the human verdict was captured
- any new finding was routed back to the correct ticket loop
- a `VERIFIED` outcome is clearly handed off as "ready for merge gate," not "already Done"

## Output

- selected review mode
- selected worktree and branch
- runtime launch command
- human QA checklist
- final human verdict
- follow-up routing note when applicable
