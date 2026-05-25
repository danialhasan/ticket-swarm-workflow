# Mission Runtime Code Map

Use this reference when a mission lifecycle skill needs to bind behavior to the
current Squad runtime instead of inventing a new workflow surface.

## Agent-Facing Mission Tools

Primary source: `apps/api/src/agent-chat-tool-registry.ts`.

Active mission lifecycle and read tools:

- `mission.propose`: non-canonical draft proposal only.
- `mission.status`: concise canonical status readback.
- `mission.get_operating_context`: API-owned packet for mission, task, blocker,
  proof, review, runtime, worker, subagent, governance, and source freshness.
- `mission.discover`: canonical mission discovery from work intake or grounded
  user problem.
- `mission.define`: canonical mission definition and task-plan admission bridge.
- `mission.select_route_control`: canonical execution route and control posture.
- `mission.propose_authority_packet`: canonical pending authority packet.
- `mission.prepare_kickoff`: canonical kickoff preparation against an execution
  grant.
- `mission.start_run`: canonical mission orchestration run start.
- `mission.record_runtime_result`: runtime output admission for task evidence,
  receipts, artifacts, and verification posture.
- `mission.report_blocker`: canonical mission blocker recording.
- `mission.resolve_blocker`: canonical mission blocker clearing.

Agent and workspace tools that commonly compose with missions:

- `workspace.inspect`, `repo.search`, `file.read`, `git.status`, `git.diff`
- `context.readiness`, `connectors.search`
- `external.search_tools`, `external.get_schemas`, `external.manage_connection`,
  `external.execute`
- `agent.spawn`, `agent.send_input`, `agent.wait`, `agent.close`
- `shell.run`, `exec_command`, `write_stdin`, `apply_patch`, `file.write`,
  `git.mutate`

## Command And Contract Anchors

- Contracts: `packages/contracts/src/missions.ts`,
  `packages/contracts/src/mission-operating-context.ts`,
  `packages/contracts/src/mission-current-state.ts`,
  `packages/contracts/src/governance.ts`.
- Domain schemas: `packages/domain/src/mission.ts`,
  `packages/domain/src/governance.ts`.
- Mission handler/admission logic:
  `packages/control-plane/src/mission-handlers.ts`,
  `packages/control-plane/src/mission-start-events.ts`.
- Persistence and events: `apps/api/src/persistence.ts` records accepted,
  rejected, blocked, canonical event, projection, and telemetry facts.
- Runtime worker context: `apps/api/src/mission-operating-context.ts`.
- Workflow bundle registry: `apps/api/src/workflow-bundle-registry.ts` and
  `workflow-bundles/ticket-swarm-workflow.json`.
- Mission worker prompt/nudge path: `apps/api/src/app.ts`.
- Subagent contract store and governance classification:
  `apps/api/src/agent-chat-subagents.ts`.
- Runtime telemetry and proof: `packages/telemetry/src/runtime-boundary.ts`,
  `packages/telemetry/src/runtime-proof.ts`,
  `packages/telemetry/src/projection-query-realtime.ts`.

## Frontend Mission Surfaces

- Mission overview/control: `apps/desktop/src/renderer/src/pages/MissionControlPage.vue`,
  `apps/desktop/src/renderer/src/pages/MissionPage.vue`,
  `apps/desktop/src/renderer/src/pages/MissionsPage.vue`.
- Mission components:
  `apps/desktop/src/renderer/src/components/squad/mission/`.
- Chat mission cards and generated UI carriers:
  `apps/desktop/src/renderer/src/pages/ChatPage.vue`,
  `apps/desktop/src/renderer/src/lib/agent-chat-ai-sdk.ts`,
  `apps/desktop/src/renderer/src/lib/agent-chat-inline-parts.ts`.

## Authority Boundary

Skills do not own product truth. They instruct the agent how to use the runtime.

Product truth must come from:

- canonical commands and admissions;
- `public.canonical_events`;
- `public.telemetry_records`;
- projections such as `mission_current_state`;
- API read models such as `mission.get_operating_context`;
- proof/review query surfaces.

Do not treat model prose, a transcript, a subagent status, a screenshot, or a
workflow runtime status as mission/task/proof truth unless it has re-entered
through the canonical surfaces above.
