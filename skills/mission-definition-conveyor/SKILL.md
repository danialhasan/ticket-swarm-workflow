---
name: mission-definition-conveyor
description: Use when Squad has enough discovered context to turn a user outcome into a canonical mission definition, task DAG, route/control posture, governance authority packet, and Approve & Run handoff.
---

# Mission Definition Conveyor

## Goal

Convert discovered context plus elicited user intent into a governed mission
that can be approved and run.

The user-facing relief is:

```text
Squad turned my messy outcome into an executable mission I can approve.
```

Mission definitions are created by mission tools, not by prose. The definition
must be the result of memory/context retrieval, thorough discovery, focused
elicitation, requirements engineering, task decomposition, and governance
selection.

## Use This Skill When

- The user asks to create, define, shape, approve, or start a mission.
- `mission-context-discovery` has produced a context packet, or the missing
  context is small enough to elicit directly.
- The agent must call mission tools rather than return a prose-only plan.
- The mission needs task decomposition, dependencies, proof surfaces, and a
  governance packet before `Approve & Run`.
- The agent detects a mission-shaped flow and needs to automatically compose
  the mission lifecycle skills before asking for approval.

## Do Not Use This Skill When

- The mission is already running; use `mission-task-operation`.
- The user is reviewing a terminated mission; use `mission-review-loop`.
- Source context is still too thin to define requirement claims; return to
  `mission-context-discovery`.

## Required Inputs

- Business/user problem, actor, and scenario.
- Context graph path/hash or explicit context-gap statement.
- Requirement claims split by proof surface. Use requirements engineering as a
  first-class step: business, engineering, security, UX, telemetry, governance,
  verification, and human-judgment requirements must be separated when they
  require different proof.
- Objective, scope boundaries, constraints, acceptance criteria, assumptions,
  known unknowns, required artifacts, required receipts, and review outputs.
- Task seeds with dependencies and proof obligations.
- Governance needs: tool ids, connector slugs, effect type, posture, reason, and
  subagent allowance.
- Workspace, work-intake, mission, session, and correlation refs when available.

## Tool Sequence

Use the runtime code map in `../references/mission-runtime-code-map.md`.

Normal path:

1. Ask focused questions with `ask_user_question` only for missing human
   decisions.
2. Run or refresh `mission-context-discovery` when the ontology, epistemology,
   source authority, or assumptions are not yet visible enough to define work.
3. Use `mission.discover` when no mission/work-intake exists yet or grounding is
   missing.
4. Apply requirements engineering across the discovered context:
   - business outcome and actor;
   - user scenario and success language;
   - engineering constraints and architecture rules;
   - security/governance constraints;
   - telemetry and proof requirements;
   - assumptions and falsification checks.
5. Use `mission.define` when the definition is ready to become canonical.
6. Verify accepted readback with `mission.status` or
   `<mission_operating_context_tool>`.
7. Ensure task decomposition is admitted into canonical task state, or mark the
   task DAG as `HOLD` before approval.
8. Use `mission.select_route_control` from allowed readback refs.
9. Use `mission.propose_authority_packet` with executable capabilities only.
10. Present one user-facing choice: `Approve & Run` or `Request changes`.
11. `Approve & Run` must approve authority, activate grant, prepare kickoff, and
   start the run through canonical command/readback paths.

The task output must be a DAG, not a list. Each task needs dependencies,
proof obligations, expected final artifact, required receipts, and the task type:
backend, frontend, devops, or mixed.

## Governance Rule

Authority packets must contain executable capabilities, not prose tasks.

Governance is policy-driven. Different agents may receive different governance
policies: chat agent, mission orchestrator, task worker, review agent, and
subagents do not automatically share the same tool exposure.

Each forecasted capability must name:

- tool id, such as `<mission_operating_context_tool>`, `repo.search`, or
  `external.execute`;
- target ref when the tool is connector-scoped;
- effect: `read`, `write`, `execute`, or `approve`;
- posture: `allow`, `approval_required`, or `deny`;
- reason tied to a task or proof obligation.

Do not include subagent capability unless the mission definition and authority
packet allow subagents for this mission.

## Output

Leave a mission definition packet with:

- canonical mission refs and readback status;
- requirement rows and proof surfaces;
- task DAG with dependencies and proof obligations;
- route/control posture;
- authority packet ref, digest, and allowed capabilities;
- governance policy mapping by agent role;
- `Approve & Run` readiness or exact blocker;
- human judgment packet focused on scope, risk, and approval.

## Stop Condition

Stop before approval when:

- canonical mission definition is missing or rejected;
- task decomposition is only transcript/UI state;
- discovery and elicitation did not produce enough context to infer intent
  safely;
- route/control refs are guessed rather than read back;
- authority packet is not canonical, stale, or missing digest/readback;
- telemetry cannot distinguish accepted, rejected, and blocked paths.

## Receipt

Receipt must include:

- requirements gate location;
- mission refs and command refs;
- current-state and operating-context readback;
- authority packet ref/digest;
- proof surfaces satisfied and `HOLD`s;
- telemetry/canonical events reused or required.
