# Codex Work Evidence Dump

Repo root: `/Users/danialhasan/dev/squad`.

This is a presentation evidence packet for the “types of work I’ve been doing with Codex” section. It separates repo evidence from inference. Where direct Codex involvement is not recorded in the artifact itself, the dump uses: “repo evidence shows the work exists, but Codex involvement is inferred from workflow context.”

## 1. Data Migrations

### Example: Control-plane canonical events + telemetry repair

* Summary:
  A schema repair/backfill migration normalizes `canonical_events` and creates/repairs `telemetry_records` so runtime proof can join durable events with telemetry.

* Files inspected:
  * `supabase/migrations/20260409002000_control_plane_telemetry_repair.sql`
  * `apps/api/test/runtime-proof-telemetry-query.db.test.ts`
  * `apps/api/test/projection-query-realtime-telemetry.db.test.ts`

* Key implementation details:
  * Creates/repairs `public.canonical_events` with `aggregate_type`, `aggregate_id`, `event_type`, `correlation_id`, actor, producer, timestamps, and JSON payload.
  * Handles historical column shapes: `stream_key`, `stream_id`, `actor_id`, `created_at`.
  * Converts old `id uuid` to text when needed.
  * Backfills nullable columns, then sets `NOT NULL`.
  * Drops obsolete columns after migration.
  * Creates `public.telemetry_records` with correlation, causation, trace, request, command, event, projection, result, reason, payload, and schema version fields.
  * Adds indexes for aggregate, event type, correlation, request, command, projection, and telemetry type/timestamp.

* Recursive complexity:
  The migration is not just “add a column.” It has to reason over previous schema states and repair them conditionally, while preserving event history used by later proof queries.

* Risk/failure modes:
  * Losing event history during old-column cleanup.
  * Incorrectly mapping `stream_key`/`stream_id` to aggregate identity.
  * Breaking runtime-proof queries by leaving null correlation or actor fields.
  * Treating telemetry as product truth instead of evidence explaining canonical truth.

* Evidence:
  * SQL checks `information_schema.columns` for old schema variants before mutating.
  * Test expects runtime proof posture: `telemetry_explains_canonical_truth_without_replacing_it`.
  * Runtime proof DB test seeds telemetry plus a canonical `receipt.recorded` event and verifies source counts: `telemetryRecords: 2`, `canonicalEvents: 1`.
  * Repo evidence shows the work exists, but Codex involvement is inferred from workflow context.

* Slide takeaway:
  Data migration work is state preservation under uncertainty: old shapes, new contracts, and proof queries all have to line up.

### Example: Supabase waitlist/email production-history reconciliation

* Summary:
  Production waitlist/email schema was reconstructed into repo migration history without copying production data or secrets.

* Files inspected:
  * `supabase/migrations/20260515200357_remote_prod_waitlist_email_history.sql`
  * Historical commit artifact: `54759c0d Add Supabase waitlist cutover functions and tracking`
  * Historical file from commit: `scripts/sqd-1302-migrate-waitlist.mjs`
  * Historical file from commit: `supabase/scripts/sqd-1302-preflight.sql`
  * Historical file from commit: `supabase/scripts/sqd-1302-postcutover-checks.sql`

* Key implementation details:
  * Migration states it captures the “schema-only waitlist/email surface” from production.
  * Creates `private.waitlist_email_settings`.
  * Creates public waitlist, email message, email event, outreach campaign, outreach recipient, and outreach event tables.
  * Adds status constraints, unique keys, foreign keys, indexes, trigger functions, RLS policies, and grants/revokes.
  * Preserves waitlist position/referral logic with advisory locks.
  * Queues confirmation email through `pg_net` only when settings allow it.
  * Migration script exports from old Supabase, normalizes rows, writes backup JSON, imports with conflict handling, and refuses non-empty targets unless explicitly allowed.

* Recursive complexity:
  This combines schema history, data movement, privacy boundaries, email side effects, referral accounting, outreach state, RLS, and production drift. The migration is also about reconstructing truth from an already-live system.

* Risk/failure modes:
  * Accidentally leaking production data or secrets.
  * Duplicate emails after import.
  * Sending emails during cutover.
  * Breaking referral counts or waitlist ordering.
  * RLS gaps exposing waitlist/outreach data.
  * Target project not empty causing duplicate/merge behavior.

* Evidence:
  * Migration comment says it contains “no production data” and no Resend/API secrets.
  * Preflight SQL checks duplicate lowercase emails, malformed emails, unsubscribes, bounces, outreach rows, and event totals.
  * Post-cutover SQL checks duplicate emails, RLS enabled state, send guard, and outreach totals.
  * Branch evidence: `origin/codex/sqd-1302-supabase-waitlist-contract`.
  * Commit evidence: `54759c0d Add Supabase waitlist cutover functions and tracking`.

* Slide takeaway:
  Codex-assisted migrations are not just SQL generation. They are operational cutovers with privacy, side effects, verification, and rollback thinking.

### Example: Production context-graph RPC + RLS drift repair

* Summary:
  Production migration history said the system was aligned, but the deployed control-plane mutation RPC did not yet admit context graph fields. A later migration restated the RPC and a separate migration reconciled production-only RLS auto-enable behavior.

* Files inspected:
  * `supabase/migrations/20260524143000_repair_context_graph_mutation_rpc.sql`
  * `supabase/migrations/20260524150000_reconcile_prod_rls_auto_enable.sql`

* Key implementation details:
  * `apply_control_plane_mutation(...)` is restated as a `security definer` RPC.
  * Requires `p_command` and `p_command.correlation_id`.
  * Uses `command_log` correlation IDs for idempotency.
  * Can reset and repopulate command log, canonical events, onboarding projection, telemetry records, context bundles, and context sources.
  * Adds context graph fields to `context_bundles`: artifact ref, hash, schema version, and status.
  * Restricts RPC execution to `service_role`.
  * Adds `rls_auto_enable()` event trigger function so future public tables get RLS enabled automatically.

* Recursive complexity:
  The migration repairs the mutation substrate that other product flows depend on. If context graph fields are missing here, later mission/context proof can appear valid in code but fail at persistence.

* Risk/failure modes:
  * Migration history says “done” while production RPC body is stale.
  * Security-definer function could become too broad.
  * Reset path could destroy state if misused.
  * Missing context graph fields would silently degrade context grounding.
  * RLS auto-enable drift could create different security posture across environments.

* Evidence:
  * SQL comment explicitly says production drift existed even though migration history was aligned.
  * RPC grants execute only to `service_role`.
  * RLS migration comment says production already had `public.rls_auto_enable()` outside repo history.
  * Commit evidence from `git log`: `2072b7c7 Checkpoint harness runtime evaluation work`.

* Slide takeaway:
  The hard part is not writing migrations. It is reconciling repo truth, production truth, and future proof surfaces.

## 2. Product Engineering

### Example: Definition-first mission flow with live E2E proof

* Summary:
  A product flow takes a mission-shaped request through definition, task plan, authority packet, approval, execution grant, run start, current-state readback, runtime-proof telemetry, and Mission Control UI.

* Files inspected:
  * `docs/operations/sessions/2026-05-16/receipts/mission-definition-live-e2e-proof.md`
  * `packages/contracts/src/agent-chat.ts`
  * `packages/contracts/src/mission-authority.ts`
  * `apps/api/test/runtime-proof-telemetry-query.db.test.ts`

* Product goal:
  Let a user move from intent to an approved/running mission with proof that the app is showing canonical state, not just a nice generated card.

* Key implementation details:
  * Live E2E receipt records mission ref, workspace ref, definition ref, task plan proposal ref, task graph revision ref, authority packet ref, execution grant ref, and run ref.
  * Current-state query returns lifecycle `running`, authority status `approved`, task total, execution grant, active run, and projection revision.
  * Canonical event chain includes `mission.discovered`, `mission.definition_created`, task creation, route/control, authority packet, approval, execution grant, run start, task start, and task execution run start.
  * Runtime proof query reports telemetry and canonical event counts.
  * UI proof shows Mission Control reading the mission as `RUNNING`.

* Recursive complexity:
  This crosses chat, mission lifecycle, task graph, governance, canonical events, telemetry, runtime proof, and UI readback. A single screenshot is not enough because the product claim spans multiple proof surfaces.

* Risk/failure modes:
  * Generated UI could look valid before canonical state exists.
  * Authority approval could happen without task/route/control readiness.
  * Mission Control could show stale or fixture state.
  * Telemetry could be mistaken for canonical truth.
  * Backend proof could outrun the user-facing journey.

* Evidence:
  * Receipt status: `VERIFIED` for seeded live proof path.
  * Runtime proof records `Telemetry records: 13` and `Canonical events: 16`.
  * The receipt explicitly notes the caveat that context-load telemetry was seeded rather than produced by an organic model turn.
  * Repo evidence shows the work exists, but Codex involvement is inferred from workflow context, with related Codex branch evidence on mission workflow work.

* Slide takeaway:
  Product engineering with Codex becomes powerful when the UI, state machine, and proof chain are built together.

### Example: Authority packet / “Approve & Run” state machine

* Summary:
  The mission approval surface was hardened so `Approve & Run` and `Request changes` behave like auditable state-machine decisions, not loose UI buttons.

* Files inspected:
  * `docs/operations/sessions/2026-05-17/receipts/goal-loops/mission-definition-organic-chat/pass-05-authority-model-property-telemetry.md`
  * `packages/contracts/src/mission-authority.ts`
  * `apps/desktop/src/renderer/src/components/squad/mission/MissionProposalCard.vue`
  * `apps/desktop/src/renderer/src/pages/ChatPage.mission-autonomy.test.ts`

* Product goal:
  Make approval trustworthy: the user should approve a specific packet, not accidentally approve stale scope or hidden execution.

* Key implementation details:
  * `missionAuthorityPacketStatusSchema` includes `pending_approval`, `approved`, `changes_requested`, `blocked`, and `superseded`.
  * Capability forecast includes tool id, effect, posture, reason, and target ref.
  * Tests cover valid approve/request-changes, stale digest, stale revision, route mismatch, control mismatch, already-approved, and already-changes-requested states.
  * Packet-scoped runtime proof can query by `authorityPacketRef`.
  * UI uses explicit `Approve & Run` and `Request changes` copy.

* Recursive complexity:
  The UI action is a gateway into execution grants and mission runs. It needs frontend copy, API command validation, canonical events, telemetry classification, stale-state rejection, and proof queries.

* Risk/failure modes:
  * Stale packet approval.
  * Repeated decision creating duplicate execution.
  * Request-changes being misclassified as failure.
  * Mission-scoped proof hiding packet-specific gaps.
  * User being asked to reconstruct machine-checkable facts.

* Evidence:
  * Receipt says valid approve creates an execution grant and run, while valid request-changes does not.
  * Receipt lists packet-scoped runtime proof endpoint: `/queries/runtime-proof/telemetry?authorityPacketRef=...`.
  * Desktop test asserts `Approve & Run` copy and prevents weaker “Approve mission” wording.
  * Branch/commit evidence: `codex/internal-dogfood-green`, commit `e9c76b91 Implement mission chat proof surfaces`.

* Slide takeaway:
  Codex helped push a button into a contract: one user decision, explicit authority, auditable consequences.

### Example: Composer-first mission revision and non-canonical generated UI

* Summary:
  After a user requests changes, the product keeps the chat composer visible and treats generated mission proposals as drafts until canonical mission definition exists.

* Files inspected:
  * `docs/operations/sessions/2026-05-17/receipts/goal-loops/mission-definition-organic-chat/pass-06-composer-first-revision-layout.md`
  * `apps/desktop/src/renderer/src/pages/ChatPage.mission-autonomy.test.ts`
  * `apps/desktop/src/renderer/src/components/squad/generated-ui/GeneratedMissionProposalBlock.vue`
  * `apps/desktop/src/renderer/src/components/squad/mission/MissionProposalCard.vue`

* Product goal:
  Keep the user in the revision loop without exposing diagnostic UI or accidentally making generated drafts feel authoritative.

* Key implementation details:
  * `AppShell.vue` gates the progress drawer behind `?progress=1`.
  * `ChatPage.vue` keeps `ProviderGateComposer` visible as a non-shrinking bottom control.
  * Generated mission proposal block labels itself as draft/non-canonical.
  * Generated proposal explicitly says definition is not created, no projection exists, and authority is unavailable before `mission.define`.
  * Tests enforce generated UI telemetry states: mounted, composer-suppressed, skipped, and failed.

* Recursive complexity:
  This is UX work, but it is also product-truth work. The app must distinguish draft model output from canonical mission state while preserving a smooth revision loop.

* Risk/failure modes:
  * Diagnostic progress rail steals space from the active revision surface.
  * Generated card looks like product truth.
  * User thinks approval is available before mission definition.
  * Screenshot-only proof misses DOM layout failure.

* Evidence:
  * Browser proof in receipt records `chat-composer` bounds inside viewport and confirms progress drawer is not mounted on normal `/chat`.
  * Test checks generated proposal contains “Draft mission proposal,” “Non-canonical,” “Definition not created,” and “Authority unavailable before mission.define.”
  * Receipt lists focused desktop tests, lint, typecheck, CSS signal, and DOM geometry checks.
  * Repo evidence shows the work exists, but Codex involvement is inferred from workflow context, with related Codex branch evidence on `codex/internal-dogfood-green`.

* Slide takeaway:
  The product surface teaches the user what is real, what is draft, and what still needs approval.

## 3. Harness Optimization / Applied AI Engineering

### Example: Mission workflow prompt/eval harness

* Summary:
  A mission-definition eval harness was built to score whether Codex/Squad mission behavior follows the intended workflow: discovery, context, requirements, task DAG, route/control, authority, approval readiness, and review.

* Files inspected:
  * `docs/operations/sessions/2026-05-18/receipts/mission-workflow-prompt-evals/mission-workflow-prompt-eval-plan.md`
  * `docs/operations/sessions/2026-05-18/receipts/mission-workflow-prompt-evals/final-green-loop-receipt.md`
  * `apps/api/src/mission-definition-evals.ts`
  * `apps/api/scripts/run-mission-definition-eval-sampling.ts`
  * `apps/api/test/mission-definition-evals.test.ts`
  * `apps/api/test/fixtures/mission-definition-evals/cases.json`

* Harness goal:
  Turn “good mission behavior” into eval cases, deterministic checks, semantic judge dimensions, live trace receipts, and regression guards.

* Artifacts involved:
  * Golden, regression, challenge, and canary datasets.
  * Trace normalization from agent-chat runs.
  * Deterministic checks for tool order, forbidden tools, discovery-before-definition, readbacks, route/control before authority, approval readiness ordering, and human lifecycle boundaries.
  * Semantic judge prompt constrained to subjective quality only.
  * JSON/Markdown live sampling receipts.

* Quality signal:
  * Deterministic: tool order, missing readbacks, forbidden tool use, ordering constraints.
  * Semantic: elicitation quality, requirements/proof-surface quality, context grounding, task decomposition, governance clarity, human judgment packet quality.
  * Trace-linked: eval results point to run refs, prompt packet refs, trace refs, and span refs.
  * Human-reviewed where semantic uncertainty remains.

* Recursive complexity:
  The harness evaluates the agent that creates missions. It is optimizing the system that changes the product system.

* Risk/failure modes:
  * Prompt substring tests masquerading as product proof.
  * LLM judges deciding deterministic facts.
  * Approval-ready language before authority packet readback.
  * Human lifecycle instructions leaking back to the user.
  * Generated elicitation UI not counted as user-facing readback.

* Evidence:
  * Final receipt reports golden deterministic scorers `6 passed, 0 failed`; semantic judges `13 passed`; canary suite `4 passed`.
  * Test fixture counts: 6 golden, 8 regression, 4 challenge, 4 canary.
  * Tests fail `mission.define` before discovery/elicitation and fail authority packets before task/route/control readback.
  * Branch/commit evidence: `codex/mission-workflow-prompt-evals-2026-05-18`, commit `15094baf Add mission workflow eval harness and receipts`.

* Slide takeaway:
  Codex is not just writing code. It is helping build eval pressure around how future Codex runs should behave.

### Example: Goal 2 dataset approval pack and scorer contracts

* Summary:
  A human-approved dataset/rubric pack defines how recursive mission orchestration and harness optimization should be evaluated before hillclimbing.

* Files inspected:
  * `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/README.md`
  * `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/rubrics-and-scorers.md`
  * `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/dataset-cases.json`
  * `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/dataset-schema.json`

* Harness goal:
  Create a governed search-and-selection surface for improving harness behavior without letting optimizer output mutate product runtime truth prematurely.

* Artifacts involved:
  * 41 approved cases: 10 golden, 17 regression, 5 challenge, 9 canary.
  * Dataset schema.
  * Deterministic assertion contracts.
  * Failure-code taxonomy.
  * Positive/negative/noisy/alternate fixtures.
  * Semantic judge boundaries.
  * Promotion decision order.
  * Active harness overlays and promotion history.

* Quality signal:
  * Deterministic scorer sources include normalized tool calls, runtime events, proof registry, app-origin trace, backend baseline trace, review packet, DB telemetry query, UI accessibility tree, browser media receipts, workspace inspection, and connector readiness.
  * Semantic judges are allowed only for subjective workflow quality.
  * Human approval gates decide which cases enter the pack.

* Recursive complexity:
  This is dataset engineering for agent improvement. The work defines what the optimizer is allowed to optimize, what it must not mutate, and which failures veto promotion.

* Risk/failure modes:
  * Optimizing vague prose instead of behavior.
  * Semantic judges deciding machine-checkable facts.
  * Canaries becoming average-score suggestions instead of hard vetoes.
  * Full product-flow claims being made from a narrow pilot.
  * Promotion-bearing hillclimb running without human gate approval.

* Evidence:
  * README says all 41 cases are approved.
  * Rubric says deterministic checks must be implementable against trace, fixture, DB query, read model, app-origin receipt, or normalized tool-call log.
  * Rubric says semantic judges cannot decide file existence, event ordering, tool count, policy subset, proof refs, backend/app-origin status, lineage, source hash, or timestamp.
  * Branch/commit evidence: `bfef1f60 Advance mission workflow eval harness`.

* Slide takeaway:
  The optimizer only gets power after the evaluation surface is frozen, inspectable, and promotion-safe.

### Example: Pilot V2 100-round hillclimb

* Summary:
  A 100-round harness hillclimb scored 880 candidates and promoted an eval-owned overlay while explicitly avoiding product-runtime promotion.

* Files inspected:
  * `docs/operations/sessions/2026-05-21/pilot-v2-hillclimb-100-rounds/receipts/aggregate.md`
  * `docs/operations/sessions/2026-05-21/pilot-v2-hillclimb-100-rounds/reports/final-winner-vs-starting-incumbent.json`
  * `tests/pilotv2-runtime-harness-prompt-scorer.test.mjs`
  * Candidate directory listing under `docs/operations/sessions/2026-05-21/pilot-v2-hillclimb-100-rounds/candidates/`

* Harness goal:
  Improve prompt/harness overlay behavior through candidate generation, scoring, comparison, adversarial review, and promotion controls.

* Artifacts involved:
  * Candidate JSON files by round.
  * Aggregate receipt.
  * Winner-vs-starting-incumbent report.
  * Runtime harness prompt scorer tests.
  * Protected hash drift checks.
  * Promotion/no-promotion fields.

* Quality signal:
  * Scalar score: starting score `22.5`, winner score `80`.
  * Deterministic dimensions and semantic dimensions per case.
  * Hard veto flag.
  * Promotion-blocking canaries.
  * Runtime tests reject prompt ref drift, missing overlay proof, and candidate-only runtime output.

* Recursive complexity:
  The harness improves a prompt/overlay used by future harness runs, so the process must prevent self-dealing: stable refs, no-promotion proof, protected hashes, and baseline comparison.

* Risk/failure modes:
  * Candidate improves scores by mutating scorer environment.
  * Candidate lacks baseline comparison.
  * Prompt references drift.
  * Runtime output is mistaken for canonical truth.
  * Eval overlay promotion gets confused with product runtime promotion.

* Evidence:
  * Aggregate receipt: `rounds_completed: 100`, `candidates_scored: 880`, `winner_score: 80`, `starting_score: 22.5`, `promotion_applied: true`, `runtime_promoted: false`.
  * Winner report marks `canonical_truth_not_admitted: true`.
  * Test rejects runtime output without no-promotion overlay proof.
  * Commit evidence: `2072b7c7 Checkpoint harness runtime evaluation work`.

* Slide takeaway:
  This is feedback descent with rails: generate candidates, score them, reject drift, promote only inside the allowed harness boundary.

### Example: Repo-owned LangSmith dataset mirror

* Summary:
  A LangSmith sync layer mirrors selected repo-owned eval cases into LangSmith while keeping the repo as the source of truth.

* Files inspected:
  * `docs/operations/sessions/2026-05-25/receipts/langsmith-dataset-mirror-implementation.md`
  * `docs/operations/sessions/2026-05-25/receipts/langsmith-dataset-sync-pilotv2-rich-reward-first-batch.md`
  * `scripts/sync-langsmith-dataset.mjs`
  * `tests/langsmith-dataset-sync.test.mjs`

* Harness goal:
  Provide an external eval/review surface without letting LangSmith become canonical truth.

* Artifacts involved:
  * Sync manifest/schema.
  * Stable source hashes.
  * Projection builder.
  * LangSmith example metadata.
  * Check/apply/receipt modes.
  * Fake client tests.
  * Remote drift/stale-example handling.

* Quality signal:
  * Deterministic projection tests.
  * Stable canonical JSON hashing.
  * Remote drift detection.
  * Stale examples archived, not deleted.
  * Local dataset validation and scoring before sync.
  * Human decision remains required for real apply with trusted key.

* Recursive complexity:
  This mirrors evals into an external tool while preserving authority boundaries: repo cases, schema, scorer, and receipts remain authoritative.

* Risk/failure modes:
  * External eval tool becomes accidental source of truth.
  * Fixture details leak unnecessarily.
  * Remote examples drift silently.
  * Stale examples get deleted instead of archived.
  * LangSmith trace IDs are later overclaimed as runtime proof.

* Evidence:
  * Receipt says selected examples: 3 of 8.
  * Sync result: creates 0, updates 0, stale updates 0, no-ops 3.
  * Implementation receipt says LangSmith cannot replace repo cases, scorer truth, canonical events, DB telemetry, app-origin proof, or human promotion judgment.
  * Commit evidence: `851add81 Fix LangSmith dataset workspace sync readback`, `4528ef3b Add repo-owned LangSmith dataset mirror`.

* Slide takeaway:
  External AI tooling is useful as a projection, but the repo-owned harness remains the authority.

## 4. Cross-Cutting Pattern

Data migrations:

* move state correctly

Product engineering:

* change systems correctly

Harness optimization:

* improve the system that changes systems

Software factory:

* organize long-horizon agent work under discipline

The ladder is:

```text
data migrations
→ product engineering
→ harness optimization
→ software factory pattern
```

The migration work shows Codex can help reason about state under drift: old schemas, production history, RLS, secrets, side effects, and verification.

The product engineering work shows Codex can help build a user-facing system where UI, contracts, canonical events, telemetry, and receipts are tied together.

The harness optimization work shows Codex can help improve the process that produces future engineering work: evals, datasets, prompt packets, scorers, failure codes, traces, and promotion gates.

The software-factory pattern is the meta-layer: agents do not just perform tasks; they work through contracts, produce receipts, get reviewed, and improve through trace-linked feedback.

## 5. Best Slide Material

* 5 strongest examples
  * Waitlist/email production migration: privacy, cutover, RLS, email side effects, pre/post checks.
  * Mission Definition live E2E proof: intent to definition to task graph to authority to run to Mission Control.
  * Authority packet / `Approve & Run`: user decision becomes auditable execution authority.
  * Mission workflow eval harness: golden/canary/regression/challenge cases around Codex mission behavior.
  * Pilot V2 100-round hillclimb: 880 candidates, score improved from 22.5 to 80, no product runtime promotion.

* 5 strongest one-liners
  * Data migrations move state correctly; product engineering changes systems correctly; harness optimization improves the system that changes systems.
  * The button is not the product. The authority packet behind the button is the product.
  * A generated card is not truth until canonical state, telemetry, and readback agree.
  * The optimizer only gets power after the eval surface is frozen.
  * The future is not more agents doing more tasks; it is disciplined systems for organizing agent work.

* 3 possible early-slide layouts
  * Ladder slide: three stacked bands: `Data migrations → Product engineering → Harness optimization`, with one concrete repo example under each.
  * Evidence grid: three columns, each with “artifact,” “risk,” and “proof” rows.
  * Codex work loop: `inspect repo → change contract/code → run proof → write receipt → feed harness`.

* 1 recommended narrative sequence for this part of the talk
  * Start with Codex as product-engineering partner, not abstract agent theory.
  * Show the mission-flow UI as the visible product artifact.
  * Then reveal the hidden work under it: migrations keep state reliable, product contracts keep user action reliable, evals keep Codex behavior reliable.
  * Use the hillclimb as the escalation: once the workflow is observable, Codex can help improve the workflow itself.
  * Close the section by naming the software-factory pattern: disciplined agent work under contracts, receipts, review, and feedback.

## 6. Files Inspected

* `.codex/skills/knowledge-artifact-loop/SKILL.md` - used lightly to keep this as a durable, evidence-backed artifact.
* `supabase/migrations/20260409002000_control_plane_telemetry_repair.sql` - canonical event and telemetry schema repair/backfill.
* `supabase/migrations/20260515200357_remote_prod_waitlist_email_history.sql` - production waitlist/email schema-history reconciliation.
* `supabase/migrations/20260524143000_repair_context_graph_mutation_rpc.sql` - context graph RPC production drift repair.
* `supabase/migrations/20260524150000_reconcile_prod_rls_auto_enable.sql` - production-only RLS auto-enable reconciliation.
* `scripts/sqd-1302-migrate-waitlist.mjs` from commit `54759c0d` - historical waitlist export/import/cutover script.
* `supabase/scripts/sqd-1302-preflight.sql` from commit `54759c0d` - historical waitlist preflight checks.
* `supabase/scripts/sqd-1302-postcutover-checks.sql` from commit `54759c0d` - historical post-cutover checks.
* `apps/api/test/runtime-proof-telemetry-query.db.test.ts` - DB-backed runtime proof query over telemetry and canonical events.
* `apps/api/test/projection-query-realtime-telemetry.db.test.ts` - projection/query/realtime telemetry proof.
* `packages/contracts/src/agent-chat.ts` - agent chat modes, tool governance, manifests, run/session contracts.
* `packages/contracts/src/mission-authority.ts` - authority packet and capability schema.
* `apps/desktop/src/renderer/src/pages/ChatPage.mission-autonomy.test.ts` - product guardrails for mission chat, approval, generated UI, workspace drawer, and Mission Control.
* `apps/desktop/src/renderer/src/components/squad/generated-ui/GeneratedMissionProposalBlock.vue` - generated draft proposal UI and non-canonical labeling.
* `apps/desktop/src/renderer/src/components/squad/mission/MissionProposalCard.vue` - mission proposal card with `Approve & Run`.
* `docs/operations/sessions/2026-05-16/receipts/mission-definition-live-e2e-proof.md` - live E2E mission definition proof.
* `docs/operations/sessions/2026-05-16/reports/atlas-implementation-contract-requirements-gap-retrospective.md` - requirements/proof-surface gap analysis.
* `docs/operations/sessions/2026-05-17/receipts/goal-loops/mission-definition-organic-chat/pass-05-authority-model-property-telemetry.md` - authority state-machine and telemetry proof.
* `docs/operations/sessions/2026-05-17/receipts/goal-loops/mission-definition-organic-chat/pass-06-composer-first-revision-layout.md` - composer-first revision layout receipt.
* `docs/operations/sessions/2026-05-18/receipts/mission-workflow-prompt-evals/mission-workflow-prompt-eval-plan.md` - mission workflow eval plan.
* `docs/operations/sessions/2026-05-18/receipts/mission-workflow-prompt-evals/final-green-loop-receipt.md` - final green-loop receipt for mission definition evals.
* `apps/api/src/mission-definition-evals.ts` - trace normalization and deterministic mission eval scoring.
* `apps/api/scripts/run-mission-definition-eval-sampling.ts` - live mission eval runner and receipt writer.
* `apps/api/test/mission-definition-evals.test.ts` - deterministic and semantic judge tests for mission evals.
* `apps/api/test/fixtures/mission-definition-evals/cases.json` - mission eval case pack.
* `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/README.md` - Goal 2 dataset approval and harness boundary.
* `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/rubrics-and-scorers.md` - deterministic and semantic scorer contract.
* `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/dataset-cases.json` - Goal 2 approved case data.
* `docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/dataset-schema.json` - Goal 2 dataset schema.
* `docs/operations/sessions/2026-05-21/pilot-v2-hillclimb-100-rounds/receipts/aggregate.md` - 100-round hillclimb aggregate.
* `docs/operations/sessions/2026-05-21/pilot-v2-hillclimb-100-rounds/reports/final-winner-vs-starting-incumbent.json` - winner vs baseline scoring details.
* `tests/pilotv2-runtime-harness-prompt-scorer.test.mjs` - runtime prompt scoring guardrails.
* `docs/operations/sessions/2026-05-25/receipts/langsmith-dataset-mirror-implementation.md` - LangSmith mirror implementation receipt.
* `docs/operations/sessions/2026-05-25/receipts/langsmith-dataset-sync-pilotv2-rich-reward-first-batch.md` - LangSmith sync receipt.
* `scripts/sync-langsmith-dataset.mjs` - repo-owned LangSmith projection/sync script.
* `tests/langsmith-dataset-sync.test.mjs` - LangSmith sync projection and drift tests.
* Git commits/branches inspected: `54759c0d`, `15094baf`, `bfef1f60`, `e9c76b91`, `2072b7c7`, `4528ef3b`, `851add81`, `origin/codex/sqd-1302-supabase-waitlist-contract`, `codex/internal-dogfood-green`, `codex/mission-workflow-prompt-evals-2026-05-18`, `codex/sqd-1377-*`.

## 7. Applicability Note

* Canonical events added: none.
* DB telemetry added: none.
* Applicability: not applicable. This is a static presentation evidence packet, not product runtime admission, mission lifecycle mutation, approval state mutation, evidence trust mutation, or user-visible app state change.
* Proof query/test used for this artifact: file inspection and git history only.
* Remaining HOLD: direct Codex involvement is strongly indicated by branch/workflow context for some examples, but not every artifact records Codex as the actor. Use the inference wording where needed.
