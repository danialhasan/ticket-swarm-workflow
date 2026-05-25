# Mission Runtime Code Map Template

Use this reference when a mission lifecycle skill needs to bind behavior to the
host product runtime instead of inventing a new workflow surface.

Ask the reader's agent to fill this map from the reader's own codebase. Squad
uses this shape publicly to show how mission runtime truth should be grounded,
but the concrete paths, tool ids, database objects, and query names belong to
each host product.

## Agent-Facing Mission Tools

Primary tool registry: `<PROJECT_ROOT>/<path-to-agent-tool-registry>`.

Active mission lifecycle and read tools:

- `<mission_propose_tool>`: draft proposal or mission-intent candidate.
- `<mission_status_tool>`: concise status readback.
- `<mission_operating_context_tool>`: packet for mission, task, blocker, proof,
  review, runtime, worker, subagent, governance, and source freshness.
- `<mission_discover_tool>`: mission discovery from work intake or grounded user
  problem.
- `<mission_define_tool>`: mission definition and task-plan admission bridge.
- `<mission_route_control_tool>`: execution route and control posture.
- `<mission_authority_packet_tool>`: pending authority or permission packet.
- `<mission_kickoff_tool>`: kickoff preparation against an execution grant.
- `<mission_start_run_tool>`: mission orchestration run start.
- `<mission_record_result_tool>`: runtime output admission for task evidence,
  receipts, artifacts, and verification posture.
- `<mission_report_blocker_tool>` and `<mission_resolve_blocker_tool>`: blocker
  lifecycle tools.

Common composing tools may include repo search, file read, git status, connector
schemas, external tool execution, subagent control, shell commands, and patch
application. The exact tool names should come from the host runtime.

## Command And Contract Anchors

Ask the reader's agent to fill:

- contracts and shared types: `<PROJECT_ROOT>/<path-to-contracts>`;
- domain schemas: `<PROJECT_ROOT>/<path-to-domain-schemas>`;
- command/admission handlers: `<PROJECT_ROOT>/<path-to-control-plane-handlers>`;
- persistence, events, projections, and telemetry: `<PROJECT_ROOT>/<path-to-persistence>`;
- worker or operating-context assembly: `<PROJECT_ROOT>/<path-to-runtime-context>`;
- workflow bundle registry: `<PROJECT_ROOT>/<path-to-workflow-registry>`;
- subagent or worker governance: `<PROJECT_ROOT>/<path-to-governance-runtime>`;
- runtime telemetry and proof queries: `<PROJECT_ROOT>/<path-to-runtime-proof>`.

## Frontend Mission Surfaces

Ask the reader's agent to fill:

- mission overview/control surface: `<PROJECT_ROOT>/<path-to-mission-overview>`;
- mission detail or task surface: `<PROJECT_ROOT>/<path-to-mission-detail>`;
- mission component directory: `<PROJECT_ROOT>/<path-to-mission-components>`;
- chat or generated UI carriers: `<PROJECT_ROOT>/<path-to-chat-or-generated-ui>`.

## Authority Boundary

Skills do not own product truth. They instruct the agent how to use the runtime.

Product truth must come from the host product's canonical workflow owner:

- canonical commands and admissions;
- canonical event storage;
- `db_runtime` telemetry records;
- current-state projections;
- operating-context read models;
- proof/review query surfaces;
- final receipts and artifacts.

Do not treat model prose, a transcript, a subagent status, a screenshot, or a
workflow runtime status as mission/task/proof truth unless it has re-entered
through the host product's canonical surfaces.
