---
name: mission-task-operation
description: Use for an active mission task when Squad must execute, review, verify, and receipt backend, frontend, or devops work autonomously against mission requirements.
---

# Mission Task Operation

## Goal

Complete one mission task through implementation, review, verification, and
receipts without letting runtime activity masquerade as canonical truth.

The user-facing relief is:

```text
I can trust this delegated task because Squad shows what changed, what was
verified, and what still needs judgment.
```

Implementation is usually the easiest part. The hard requirement is that each
task preserves the mission's ontology, epistemology, requirements, governance,
and proof standard while agents work autonomously.

## Use This Skill When

- A mission is running and the worker needs to operate on a task.
- `<mission_operating_context_tool>` exposes an active task or runnable task.
- The task needs engineering work, verification, review, or receipts.
- Backend, frontend, desktop, or devops claims must be proven on the right rail.

## Do Not Use This Skill When

- The mission is not defined or approved; use `mission-definition-conveyor`.
- The task lacks canonical task state; report a blocker instead of inventing a
  task from transcript text.
- The mission has terminated and the user is reviewing outcomes; use
  `mission-review-loop`.

## Required Inputs

- `<mission_operating_context_tool>` packet.
- Active task ref, task execution run ref, dependencies, blockers, and proof
  obligations.
- Execution grant and exposed tool ids.
- Requirement rows with proof surfaces and forbidden substitutions.
- Relevant ontology and epistemology rules from the context graph: terms,
  ownership, architecture constraints, source authority, assumptions, and
  falsification checks.
- Target receipt path and artifact expectations.
- Human judgment packet, if any.

## Operating Loop

1. Read `<mission_operating_context_tool>`.
2. Confirm the active task and execution grant.
3. Choose the smallest Ticket Swarm composition:
   - `multi-agent-workflow` when independent lanes can run.
   - `layered-verification` for proof selection.
   - review queue skills for P0/P1/P2/P3 defect finding and autofix loops.
   - `abstraction-drift-review` when architecture or abstraction risk is high.
4. Run task discovery before implementation when the task's local requirements,
   architecture constraints, or proof strategy are not yet explicit.
5. Implement only the task scope.
6. Run autonomous review and verification loops until P0/P1/P2/P3/security/
   requirements violations are fixed or explicitly held.
7. Record outputs through `mission.record_runtime_result`.
8. Re-read operating context.
9. Continue, report blocker, or hand off to proof/review.

The task lifecycle is:

```text
discovery -> implementation -> review and verification loop -> receipts
```

## Proof By Task Type

Backend:

- API/contract tests, model/property tests where useful, DB/RLS proof when
  durable data or access policy is claimed, runtime-proof telemetry for command
  and negative paths.
- Endpoint/input-output proof where API behavior is claimed.
- Business requirements checked against the implemented behavior, not only
  against code shape.

Frontend:

- Component/unit tests plus Browser/Electron user-journey proof.
- Media is mandatory for user-flow claims: screenshots and, when interaction or
  timing matters, video/recording receipts.
- Media never replaces durable state or telemetry proof.
- The final artifact must display or link the relevant media so Mission Review
  can inspect the delivered user flow.

Devops:

- Health endpoint proof, deployed commit/hash proof, updater/feed proof, release
  artifact integrity, rollback/failure behavior, and frontend proof when deploy
  changes visible UI.
- If a deploy affects a frontend surface, include the same media proof expected
  from a frontend task.

All task types:

- architecture and abstraction choice must be justified from legible context;
- receipts must show P0/P1/Pn review findings and fixes or explain why review
  scope was not applicable;
- proof must distinguish happy path, negative path, and remaining `HOLD`s.
- requirements violations, security issues, and ontology/epistemology drift are
  review findings, not optional notes.

## Stop Condition

Report a blocker with `mission.report_blocker` when:

- required tool authority is missing;
- task refs or execution run refs are missing;
- dependencies are not satisfied;
- proof tools are unavailable;
- the worker cannot produce concrete output, receipt, or artifact refs;
- repeated no-op model behavior occurs.

## Receipt

Every completed task needs a final task artifact that aggregates:

- requirement rows and statuses;
- implementation summary and file refs;
- autonomous review findings and patches;
- verification commands and outputs;
- media for frontend claims;
- telemetry/canonical proof queries;
- final `mission.record_runtime_result` refs;
- human judgment packet;
- explicit non-claims.

Task completion is not valid without this final artifact, even when smaller
receipts already exist.
