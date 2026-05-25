# May 13 Dogfood Goal Template

Use this template when the goal is first mission loop dogfood readiness.

## Goal Statement

Make the May 13 internal dogfood path capable of real mission creation and the
deepest available execution/review loop without false fixture, provider,
connector, telemetry, or release-readiness claims.

## Loop Moves

1. Identify missing visible seams.
2. Convert each gap into work, implementation contract, rerun gate, deferral, or
   human blocker.
3. Dogfood auth -> provider readiness -> connector/context readiness -> Chat
   request -> mission proposal -> kickoff/admission -> mission detail ->
   task/evidence/proof/review -> support recovery.
4. Capture Browser/Computer/runtime/telemetry/DB proof.
5. Review with subagents.
6. Update the blocker ledger and continue.

## Known Starting Gates

- User auth is covered by `SQD-1172` through `SQD-1176`, `SQD-1308`, and
  `SQD-1294`.
- Provider OAuth UX is not fully covered by existing contracts.
- `SQD-1332` is the real-inference / mission-proposal implementation rail.
- `SQD-1316` and `SQD-1317` rerun only after `SQD-1332` produces product-flow
  proof or a changed product-real blocker.
- `SQD-1315` and `SQD-1033` remain release-tail / human release-decision rails.

## Forbidden Claims

No beta readiness, QA atlas completion, provider readiness, connector
readiness, durable persistence, updater readiness, or real-inference success
without matching Linear, Browser/Computer, runtime, telemetry, DB/RLS where
applicable, and receipt proof.
