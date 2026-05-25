---
name: mission-context-discovery
description: Use when a user enters a mission-shaped flow and Squad must make legible context visible before mission definition by building or refreshing an ontology/epistemology context graph from code, connectors, transcripts, memory, and elicitation.
---

# Mission Context Discovery

## Goal

Turn vague mission intent into an auditable context packet and context graph that
the mission definition agent can rely on without pretending the graph is truth by
itself.

The user-facing relief is:

```text
Squad knows what world it is operating in before it asks me to approve work.
```

This is the first step of mission creation. Missions must not be defined before
Squad has made the relevant operating environment legible or has exposed the
exact context gap blocking definition.

For the shared applied-AI/context-engineering doctrine, especially the rule that
context is a controlled input surface rather than prompt stuffing, see
[`../squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md`](../squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md).

## Use This Skill When

- The user enters Mission mode with a broad outcome.
- Mission definition depends on codebase context, connector context, tribal
  knowledge, memory, or prior agent transcripts.
- The agent needs to map ontology: entities, workflows, tools, surfaces,
  owners, dependencies, policies, terms, and artifacts.
- The agent needs to map epistemology: sources, authority, freshness, proof
  rules, assumptions, contradictions, and falsification checks.
- Existing context graphs may be stale or incomplete.
- The mission may depend on non-code context: tribal knowledge, connector
  knowledge, or prior agent conversations from Codex, Claude, and other agents.

## Do Not Use This Skill When

- A canonical mission definition already exists and the task is active runtime
  execution; use `mission-task-operation`.
- The user only asks for a read-only status of an existing mission; use
  `mission-overview-readmodel`.
- The missing item is a single focused clarification that can be handled inside
  `mission-definition-conveyor`.

## Required Inputs

- User outcome or problem statement.
- Workspace, repo, and current mission/session refs when available.
- Allowed sources: codebase, docs, memory, transcripts, connectors, browser
  receipts, `issue_tracker`, `team_chat`, Drive, Gmail, Calendar, or other connected systems.
- Governance posture for source access and connector use.
- Existing context graph path or statement that no graph exists.
- Required receipt target.

## Skill Composition

Use only the minimum composition needed:

- `requirements-proof-map` for proof-surface splitting.
- `multi-agent-workflow` for independent context lanes when the context surface
  is broad. Use separate lanes for codebase, connector, transcript, memory, and
  elicitation work when those sources can be inspected independently.
- `repo.search`, `file.read`, and connector search tools for evidence.
- `ask_user_question` only for missing decisions, not for machine-verifiable
  source reads.

If connector data is needed, use the governed Squad connector or the configured connector adapter rail.
Do not copy external-tool results into mission truth until a later canonical
command admits the derived claim.

Discovery is also the input to Squad's memory system. When the environment has
stable legible sources, recommend background automation that refreshes context
graphs on a schedule and records staleness, source drift, and changed claims
without silently changing mission truth.

## Context Graph Contract

Persist or update a JSON context graph with this minimum shape:

```json
{
  "schemaVersion": "squad-context-graph.v1",
  "generatedAt": "ISO-8601",
  "focus": "mission outcome or environment",
  "coverage": {
    "codebase": "covered|partial|missing",
    "connectors": "covered|partial|missing",
    "transcripts": "covered|partial|missing",
    "memory": "covered|partial|missing"
  },
  "ontology": {
    "entities": [],
    "workflows": [],
    "tools": [],
    "agents": [],
    "policies": [],
    "surfaces": [],
    "connectors": [],
    "transcripts": [],
    "terms": []
  },
  "epistemology": {
    "sources": [],
    "claims": [],
    "assumptions": [],
    "contradictions": [],
    "stalenessRules": [],
    "falsificationChecks": []
  },
  "missionReadiness": {
    "readyToDefine": false,
    "missingInputs": [],
    "humanJudgmentNeeded": []
  }
}
```

Each claim in the graph must carry source refs, authority, freshness, confidence
posture, and what would falsify it.

Context packets must be selected, compressed, sourced, freshness-aware, tied to
product intent, tied to proof surfaces, discardable when stale, versioned enough
for receipts, and evaluated against downstream behavior. Do not treat a large
retrieval bundle as better context by default. Context that cannot guide a
later proof surface should be omitted, parked, or marked as background.

The context graph should let the next agent answer:

- what exists in this environment;
- how each important thing relates to other things;
- who or what has authority for each claim;
- which claims are fresh, stale, assumed, contradicted, or falsified;
- what proof standard applies before the claim can guide a mission.

## Output

Leave a discovery packet that includes:

- Context graph path and hash.
- Source inventory and source authority.
- Codebase, connector, transcript, tribal-knowledge, and memory coverage.
- Missing or stale context.
- Assumptions to falsify before approval.
- Requirement claims split by proof surface.
- Human judgment packet.
- Background refresh or automation recommendation when the source graph should
  stay current between missions.
- Recommended next skill: usually `mission-definition-conveyor`, or `HOLD` if
  context authority is insufficient.

## Stop Condition

Stop before mission definition when:

- required source access needs consent, credentials, billing, or destructive
  action;
- source authority conflicts and the conflict changes the mission;
- the context graph cannot name proof surfaces for the likely mission claims;
- the user must decide scope before discovery can stay bounded.

## Receipt

Receipt must include:

- `issue_tracker` issue when available.
- `Internal ticket id` when available.
- Context graph path and hash.
- Sources read and sources skipped.
- Requirements-proof map location.
- Telemetry/canonical applicability note: discovery files and connector reads
  are not canonical mission events by default.
