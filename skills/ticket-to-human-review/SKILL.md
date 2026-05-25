---
name: ticket-to-human-review
description: Use when an implementation contract needs human signoff before development/testing begins. This verifies the contract, not the implementation.
---

# Ticket To Human Review

Use this skill when a compiled implementation contract is ready for human
signoff.

This skill does not develop, test, merge, deploy, or release the work. It
answers one question: is this implementation contract clear, bounded, and
approved enough for the direct dev/testing composition to start?

## Goal

Turn an implementation contract into one explicit human decision:

```text
implementation contract
  -> human contract review
  -> SIGNED_OFF / CHANGES_REQUESTED / HOLD
  -> direct iterative dev/testing composition, if signed off
```

`SIGNED_OFF` means ready for development and testing. It does not mean the work
is implemented, verified, merged, deployed, or released.

## Inputs To Gather First

- implementation contract issue or packet
- active Implementation Contract parent
- source Design Contract refs
- source readiness/prep row, when one exists
- browser receipts, screenshots, annotations, or review evidence
- user-relief sentence and done signal
- primary implementation seam
- explicit non-goals
- SDLC composition map
- proof matrix and DB/Electron proof requirements
- governance grant, when mission autonomy or external actions are involved
- dependencies, blockers, and linked backend/design gaps

Start by reading:

- the implementation contract packet
- `../implementation-contract-conveyor/SKILL.md`
- `../design-contract-conveyor/SKILL.md`
- `.codex/skills/multi-agent-workflow/SKILL.md`
- `.codex/skills/layered-verification/SKILL.md`

## Review Posture

The human is reviewing the contract, not code.

The operator should make the human decision narrow:

- what design truth was approved
- what one seam will be built
- what the contract explicitly excludes
- what dev/testing composition will run after signoff
- what proof is required before the work can later be called verified
- what governance grant the agent needs before an autonomous run

Do not ask the human to inspect code, run tests, choose worktrees, or debug
implementation details at this gate.

## Workflow

### 1. Assert contract readiness

Do not start human signoff unless the contract includes:

- source Design Contract refs
- implementation parent and proposed child identity
- one primary implementation seam
- explicit non-goals
- source-of-truth and local-state boundary
- SDLC composition map
- proof matrix
- review and patch-loop expectations
- deployment/release boundary

If any of those are missing, return `HOLD` with the missing contract sections.

### 2. Check the design-to-implementation trace

Confirm the contract traces cleanly from approved design truth:

- approved design rules are present
- rejected, cut, or parked ideas did not sneak back into scope
- screenshots or browser receipts are referenced where useful
- implementation scope does not exceed the approved design cluster

If the contract expands beyond approved design truth, return
`CHANGES_REQUESTED`.

### 3. Check the dev/testing composition map

Confirm the contract names the iterative execution loops that will run after
signoff:

- lane fan-out through `$multi-agent-workflow`
- non-author review swarm
- patch and re-review loop until zero blocking findings
- `$layered-verification` loop until green or true blocker
- UI/Electron verifier lane when required
- Computer Use focus preflight for UI/Electron proof: exact Electron app path, raised/focused window, and real renderer HTML content in the accessibility tree before clicks or visual judgment
- persisted/DB-backed proof row when required
- receipt destinations

This is intentionally not a linear checklist. The contract should make it clear
where the system will spend more tokens/compute to raise quality.

### 4. Check human attention and governance

Confirm the contract says what the human is approving:

- what work may start
- what capabilities/data/actions the agent will need
- which approval boundaries apply
- what remains outside this implementation contract
- whether deployment/release is excluded and handled separately

If the agent grant is too vague for an autonomous run, return
`CHANGES_REQUESTED`.

### 5. Record the verdict

Allowed outcomes:

- `SIGNED_OFF`: contract may enter direct dev/testing composition.
- `CHANGES_REQUESTED`: contract needs edits before development/testing starts.
- `HOLD`: contract cannot be judged because required context is missing or
  upstream approval is unresolved.

For every outcome, record:

- reviewer
- timestamp
- implementation contract id or packet path
- verdict
- reason
- required edits, if any
- next workflow step

## Output

Return:

- implementation contract reviewed
- verdict: `SIGNED_OFF`, `CHANGES_REQUESTED`, or `HOLD`
- concise reason
- required contract edits, if any
- approved direct dev/testing composition, if signed off
- reminder that deployment/release is separate

## Close Rule

This skill is complete when:

- the implementation contract was reviewed against approved design truth
- the dev/testing composition map was checked
- the governance and human-attention boundary was checked
- one explicit verdict was recorded
- no implementation, test, merge, deploy, or release work was performed inside
  this skill
