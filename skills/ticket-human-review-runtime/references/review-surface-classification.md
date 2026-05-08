# Review Surface Classification

Use this reference before launching any review runtime.

Goal:

- classify the ticket before asking the human to look at anything
- keep operator-only tickets moving without human babysitting
- reserve real human attention for visible product truth

## Classes

### 1. Operator-Only Probe

Use when the ticket only changes:

- handlers
- contracts
- write paths
- event append rules
- projectors
- named queries
- realtime delivery plumbing
- telemetry seams
- smoke fixtures or verification harnesses

Operator behavior:

- run live probes
- compare against receipts and closeout
- record the result
- move the ticket forward unless a contradiction appears

Human interruption rule:

- do not interrupt by default
- escalate only if the probes contradict the claimed seam or reveal scope drift

### 2. Operator-Led Sanity Veto

Use when the ticket is still mostly plumbing but there is a thin product judgment worth preserving.

Examples:

- auth or readiness bridge seams
- source posture surfaces
- kickoff command bridge tickets
- support overlays where wording or state honesty matters

Operator behavior:

- do almost all of the work
- give the human one tiny question
- expect a one-word verdict

Human interruption rule:

- show only the smallest contract packet or visible state needed for a veto

### 3. Human Runtime Review

Use when a human can directly judge the claim in the live app.

Examples:

- onboarding shell
- home orientation
- mission view
- proof and review surfaces
- approval and reroute command UX
- degraded-state honesty and recovery posture

Operator behavior:

- boot the right runtime
- provide a visual map or screenshot
- reduce the review to a short checklist

Human interruption rule:

- this is the normal path for real product-surface tickets

### 4. Bundle Coherence Review

Use when the real question is not one ticket, but whether several visible surfaces line up into one honest product story.

Examples:

- execution bundle coherence
- proof and review coherence
- context and integration coherence
- degraded-state and external-beta hardening coherence

Operator behavior:

- finish ticket-local proof first
- then stage one integrated review surface
- route fixes back to owner worktrees

## Current Default Map

Early default map from the `First Mission Loop External Beta` audit:

- Bundle A flow and control-plane seams: `Operator-Only Probe`
- bridge tickets around auth, shell replacement, readiness, and kickoff: `Operator-Led Sanity Veto`
- visible onboarding, home, mission, proof, review, and degraded-state surfaces: `Human Runtime Review`
- execution/proof/review and degraded-state bundle slices: `Bundle Coherence Review`

## Routing Rule

Classify first. Launch runtime second.

If you have not classified the ticket yet, you are not ready to interrupt the human.
