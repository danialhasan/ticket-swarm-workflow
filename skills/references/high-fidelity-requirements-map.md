# High-Fidelity Requirements Map

Use this reference when requirements discovery or elicitation produces enough
context to shape product work, mission work, model-mediated behavior, or a
human-review packet.

The output is not a checklist. It is the compiled product-truth artifact that
lets another agent implement, verify, or review without replaying the full
conversation.

## Required Shape

Every high-fidelity requirements map must include:

- **Outcome frame**: business/user problem, actor, scenario, adjacent scenarios,
  and the user's relief sentence.
- **Requirement ledger**: distinct requirement claims split by proof surface.
- **Context aggregation**: admitted sources, source authority, stale or missing
  context, assumptions, contradictions, and decisions already made.
- **Data exposure map**: what the user sees, what is behind details, what is
  queryable by agents, what is telemetry-only, and what must never be exposed.
- **System surface map**: commands, tools, events, projections, DB tables,
  runtime adapters, UI components, and external systems touched by the flow.
- **State map**: current known implementation status for every major claim:
  `implemented`, `partial`, `missing`, `hold`, or `unknown`.
- **Proof matrix**: required machine proof, forbidden substitutions,
  autonomous verification plan, and the exact human judgment packet.
- **Diagram packet**: ASCII or Mermaid diagrams detailed enough to show
  lifecycle order, data movement, authority boundaries, and review handoff.
- **Receipt target**: where the map, proof, and follow-up contract should live.

## Diagram Standard

Use high-fidelity diagrams when the work crosses mission setup, governance,
runtime orchestration, generative UI, model/tool behavior, proof/review, or
durable state. A useful diagram should show:

- lifecycle stages in order;
- canonical truth owner for each stage;
- provisional UI state versus durable state;
- command/query/event boundaries;
- data exposed in the UI versus data retained for proof/evals;
- blockers, approval gates, and human judgment moments;
- what is implemented today and what is missing.

Avoid vague boxes like `AI does work`. Replace them with the actual boundary:
model call, tool call, command admission, projection update, task execution,
proof assembly, review decision, or eval trace.

## Close Rule

The requirements pass is not complete until the map can answer:

- What user problem are we solving?
- Who acts, who judges, and who benefits?
- What exact flow will the user experience?
- What data appears where?
- Which claims are currently true in the codebase?
- Which claims are unproven or missing?
- What proof would satisfy each claim?
- What decision still genuinely requires Danial?

If those answers are not visible, do not route to implementation yet.
