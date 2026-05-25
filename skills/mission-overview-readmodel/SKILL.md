---
name: mission-overview-readmodel
description: Use when rendering, auditing, or summarizing the mission overview surface or generated mission card from canonical mission operating context.
---

# Mission Overview Readmodel

## Goal

Show the user the smallest useful mission overview from canonical readback,
without turning Mission Overview into a transcript browser, proof console, or
control panel.

The user-facing relief is:

```text
I can see what this mission is, what is running, what is blocked, and what
authority it has without reading the whole agent transcript.
```

## Use This Skill When

- The agent needs to render or inspect Mission Overview.
- Chat wants to show a compact mission card through generated UI.
- A user asks for mission status, progress, governance, or task details.
- Mission Control must prove it reads the same product truth as Chat.
- A completed mission exposes a review entrypoint that routes to Mission
  Overview before launching the review chat.

## Do Not Use This Skill When

- The user is defining a mission; use `mission-definition-conveyor`.
- The worker is executing a task; use `mission-task-operation`.
- The mission is complete and the user is making a review decision; use
  `mission-review-loop`.

## Required Inputs

- Mission ref.
- `mission.get_operating_context` readback.
- `mission_current_state`, proof/readiness, review surface, and runtime-proof
  query refs where applicable.
- Governance policy/grant readback.
- Transcript/session refs for read-only display only.

## Surface Contract

Mission Overview should contain only:

- Mission metadata needed to orient the user.
- Mission overview markdown rendered document.
- Task list; each task opens a modal with its task markdown/details.
- Progress log from the mission orchestrator with lifecycle statuses:
  discovery, implementation, review and verification loop, receipts.
- Read-only live transcript window for the mission orchestrator agent.
- Governance section listing policies/grants that apply to the mission agent.
- Context-specific entrypoints such as `Review` when the mission is reviewable.

Everything else should be behind details or omitted. Do not add extra default
sections just because the data is available.

## Truth Rules

- The overview reads from `mission.get_operating_context` and related named
  projections.
- The transcript is context, not control. Users do not send messages to the
  mission agent from this surface.
- Human instructions to the mission must go through the chat agent, which can
  translate feedback into mission tools and context updates.
- Governance display is read-only mission authority readback, not the Settings
  policy editor.
- Generated UI cards are carriers. They must reconcile against canonical
  mission readback before presenting approval, running, proof, or review state.
- A generated mission card may appear in Chat when the agent uses generated UI
  with a mission component and mission id from mission read tools. The card is a
  compact carrier of Mission Overview truth, not a separate product surface.
- Proof/readiness and blockers can be used to decide state and entrypoints, but
  should not expand the default overview beyond the surface contract.

## Output

Return or render:

- overview document;
- task rows with modal-ready detail refs;
- progress lifecycle rows;
- transcript read-only stream ref/status;
- governance policy/grant rows;
- review entrypoint readiness when applicable;
- source freshness and `HOLD`s.

## Stop Condition

Do not claim mission state when:

- `mission.get_operating_context` is missing, stale, or not for the requested
  mission;
- active run, grant, task, proof, or review state is inferred from transcript;
- blockers and waits cannot be distinguished;
- UI media exists without query/readback receipts.

## Receipt

Receipt must include:

- mission ref and operating-context query receipt;
- source freshness;
- UI proof if the surface was rendered;
- proof surfaces satisfied and `HOLD`s;
- telemetry/canonical applicability note for read-only overview actions.
