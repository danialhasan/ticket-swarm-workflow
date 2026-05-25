# First Mission Loop Readiness Template

Use this template when the goal is first mission loop readiness for a Squad-style
product surface.

## Goal Statement

Make the target mission path capable of real mission creation and the deepest
available execution/review loop without false fixture, provider, connector,
telemetry, or release-readiness claims.

## Loop Moves

1. Identify missing visible seams.
2. Convert each gap into work, implementation contract, rerun gate, deferral, or
   human blocker.
3. Auth -> provider readiness -> connector/context readiness -> Chat
   request -> mission proposal -> kickoff/admission -> mission detail ->
   task/evidence/proof/review -> support recovery.
4. Capture `ui_automation_driver`, runtime, telemetry, and `db_runtime` proof.
5. Review with subagents.
6. Update the blocker ledger and continue.

## Known Starting Gates

Ask the reader's agent to fill these from the current `issue_tracker`,
requirements map, and receipts:

- `<AUTH-ISSUE>` covers user auth and session continuity.
- `<PROVIDER-UX-ISSUE>` covers provider connection UX.
- `<MISSION-PROPOSAL-ISSUE>` owns real inference or mission proposal behavior.
- `<MISSION-RERUN-ISSUE>` reruns only after product-flow proof exists or the
  blocker changes.
- `<RELEASE-DECISION-ISSUE>` remains release-tail or human release-decision work.

## Forbidden Claims

No beta readiness, QA completion, provider readiness, connector readiness,
durable persistence, updater readiness, or real-inference success without
matching `issue_tracker`, `ui_automation_driver`, runtime, telemetry,
`db_runtime`, access-policy proof where applicable, and receipt proof.
