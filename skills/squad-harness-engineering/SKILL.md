---
name: squad-harness-engineering
description: Use when Squad agent behavior, prompts, tool manifests, eval traces, trajectories, datasets, or applied-AI harness changes need to be engineered through source traces, golden/regression/challenge/canary cases, scorers or judges, and regression receipts before product claims or implementation closeout.
---

# Squad Harness Engineering

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected problem is model-mediated behavior, not normal
product implementation.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

For the applied-AI/context-engineering doctrine that governs optimizer work,
candidate generation, feedback signals, compute use, and semantic/deterministic
boundaries, see
[references/bitter-lesson-applied-ai-context-engineering-doctrine.md](references/bitter-lesson-applied-ai-context-engineering-doctrine.md).

For the repo-level map of Squad harness knobs against current runtime surfaces,
use `docs/execution-system/harness-engineering.md` before changing prompt
overlays, tool manifests, middleware, skills, subagent delegation, memory,
runtime traces, or promotion boundaries.

## Goal

Turn applied-AI behavior changes into dataset-backed engineering work:

```text
source trace or annotation
  -> behavior claim
  -> golden/regression/challenge/canary case
  -> deterministic scorer and/or semantic judge
  -> prompt/tool/policy change
  -> rerun and regression receipt
```

The user-facing relief is:

```text
Squad improves agent behavior with evidence, not prompt vibes.
```

## Boundary

Harness engineering is part of applied AI, but this skill is not an
`applied-ai` strategy router. It stays inside Ticket Swarm while the work is
about Squad's product harness, mission behavior, traces, datasets, proof, and
reviewability.

Promote this into a standalone `applied-ai-workflow` plugin only after repeated
non-Squad or client-facing workflows need their own upstream router for
opportunity mapping, pilot slicing, data boundaries, workflow automation, and
consulting proof. Until then, keep the implementation rail here.

Flywheel is the default research control plane for repeated Squad harness
optimization, hillclimbing, scorer/judge iteration, prompt/tool/skill search,
or applied-AI frontier planning. Use this skill to name the harness behavior
claim, proof surface, and promotion boundary; use Flywheel to preserve the
research question, hypothesis tree, comparator, evidence artifacts, budget,
stop condition, interpretation, and next branch.

Framework boundaries:

- Flywheel research control plane: default for hypothesis tracking, graph
  topology, artifact mapping, budgeted frontier planning, explicit stop
  conditions, and lookahead decisions across runs.
- Runner-framework adoption: not an active branch in this workflow. Local
  runners, package scripts, and filesystem receipts remain the execution/proof
  substrate. Any future runner-framework proposal needs a separate explicit
  adoption plan, parity oracle, adapter proof, rollback, and Danial approval
  before it can re-enter the active path.
- New repeated non-Squad pattern: propose a standalone skill/plugin branch with
  actor, workflow, source system, write boundary, and proof surface.

Do not let a framework choice become the product claim. The claim remains the
behavior change and the evidence that proves it. Flywheel nodes summarize and
route research; they do not replace local receipts, scorers, canaries, app-origin
proof, canonical events, DB-backed telemetry, or product-runtime promotion
approval.

Generated DSA docs for this workflow live at
`docs/operations/harness-optimization-dsa/index.html`. When a harness change
alters candidate schemas, scorer outputs, mutation algorithms, promotion gates,
runtime bridge contracts, proof vocabulary, or this skill's operating rail, run
`pnpm docs:harness-dsa`, `pnpm docs:harness-dsa:check`, and
`node --test tests/harness-dsa-docs.test.mjs`. Edit source contracts or
`scripts/build-harness-dsa-docs.mjs`, not generated HTML.

## LangSmith Dataset Mirror

Repo-owned harness datasets may be mirrored into LangSmith only as projected
review/eval examples. The repo remains authoritative for case text, schemas,
scorers, fixture labels, promotion gates, receipts, and non-claims. LangSmith is
not canonical truth and does not emit canonical events for dataset sync.

Use this rail for selected cases:

```text
repo dataset pack
-> validate/score locally
-> project selected manifest rows
-> upsert LangSmith examples
-> write sync receipt
```

Start with
`docs/operations/datasets/langsmith-sync/pilotv2-rich-reward.manifest.json`;
do not mirror the full pack by default. Commands:

```text
pnpm dataset:pilotv2:validate
pnpm dataset:pilotv2:score
pnpm dataset:langsmith:check
pnpm dataset:langsmith:apply
pnpm dataset:langsmith:receipt
```

`dataset:langsmith:check` is the CI-safe command. `dataset:langsmith:apply`
requires `LANGSMITH_API_KEY` and, for org-scoped keys, `LANGSMITH_WORKSPACE_ID`.
Workspace display names such as `Workspace 1` are not accepted by the SDK; use
the workspace UUID. Apply should run only from a trusted manual or scheduled
main-branch sync. Never delete LangSmith examples by default; stale repo-owned
examples must be marked `sync_state: "stale"` or moved to an archived split by
the sync script.

Every LangSmith-backed harness receipt must cite the dataset sync receipt or
state why the mirror was not used. A LangSmith example, trace, or run id is not
promotion proof unless the separate runtime/canonical/DB proof surfaces required
by the claim are also present.

## Bitter-Lesson Applied AI / Context Engineering Doctrine

Squad harness work should optimize the search-and-selection environment, not
pretend one handcrafted prompt can encode all intelligence. Prefer many bounded
candidate attempts, frozen eval pressure, trace-backed failure packets, repair
loops, receipts, and explicit promotion/rejection decisions.

The strict role split is:

- Harness: evaluation environment, guardrails, frozen cases, scorers, fixtures,
  mutation boundaries, and veto order.
- Optimizer / hillclimber: LLM-driven search over allowed candidate levers.
- Candidate: a prompt/context/tool/skill/routing behavior configuration.
- Product runtime: the actual Squad app/control plane, canonical events, DB
  telemetry, and user-visible lifecycle state.

The harness defines the hill. The optimizer climbs it.

Do not overfit the runtime model to Mission mode. Squad starts from the default
chat posture; Plan, Mission, review, subagent, and eval behavior are composed
runtime layers selected by mode, product state, or harness namespace. Current
Pilot V3 cases are Mission-heavy because the active arena is the Mission
workflow packet, not because Mission is the base runtime.

Protect the stable prompt prefix. Harness prompt candidates should default to
append/composition after stable base and mode context so optimization does not
destroy model cache locality by rewriting the base system prompt. Prepend or
replace-style prompt mutations require a separate cache/risk rationale and
must not be treated as product-runtime promotion from an eval-only win.

Use models for candidate generation, critique, failure analysis, repair
proposals, reward-case discovery, fixture mutation proposals, trace clustering,
receipt synthesis, and product-intent inference from persisted context. Do not
use model output as deterministic truth.

Deterministic scorers own machine facts. Semantic judges score subjective
quality only, such as mission sharpness, review usefulness, human review burden,
decomposition quality, governance clarity, and RLM legibility. Semantic judges
must not decide event existence, tool order, proof refs, policy subset,
app-origin/backend status, lineage refs, depth/fanout budgets, fixture labels,
or canonical event existence.

Context is a controlled input surface, not prompt stuffing. Context packets
must be selected, compressed, sourced, freshness-aware, tied to product intent,
tied to proof surfaces, discardable when stale, versioned enough for receipts,
and evaluated against downstream behavior.

Compute increases mutation rate, not progress by itself. Use compute for
parallel candidate generation, critique, failure clustering, fixture mutation
proposals, scorer stress tests, reward ablations, trace comparison, receipt
synthesis, and adversarial search for reward hacking. Do not use compute for
random prompt spam, uncontrolled rewrites, scope expansion without gates,
scoreboard mutation, premature case expansion, or dumping huge traces on Danial.

Every optimization artifact must attach to refs: `candidate_ref`, `case_ref`,
`assertion_ref`, `fixture_ref`, `failure_code`, or `receipt_ref`. No unattached
prose blobs.

## Use This Skill When

- A prompt, tool manifest, governance policy, or skill injection change is meant
  to change agent behavior.
- A trace shows wrong tool order, missing proof, too many tool calls, bad
  delegation, false readiness, or mode confusion.
- A mission/chat behavior needs a golden trajectory or regression case.
- App-origin behavior disagrees with backend baseline behavior.
- Recursive subagent or RLM behavior needs lineage, aggregation, depth, or
  policy-inheritance proof.
- A human annotation reveals repeated agent behavior that should become an eval
  case instead of another one-off correction.
- A semantic judge or deterministic scorer needs to be designed, revised, or
  attached to a suite.

## Do Not Use This Skill When

- The work is ordinary code implementation with clear deterministic tests; use
  `implementation-contract-conveyor` or the execution lane skills.
- The problem is purely visible UI abstraction leakage; use
  `ui-abstraction-guard`, then return here only if a harness dataset must catch
  the repeated behavior.
- The problem is raw feature scope or product decision hygiene; use
  `feature-decision-ledger`.
- The problem is mission context, definition, execution, overview, or review
  using already-approved behavior; use the mission lifecycle skills.
- The request is a client/applied-AI opportunity map with no Squad harness
  behavior to change. That is a future standalone plugin concern.

## Required Inputs

- Source trace, app-origin receipt, transcript excerpt, human annotation, eval
  failure, or explicit statement that the source is missing.
- Product outcome or harness behavior claim.
- Invariant family and failure-code taxonomy entry for the behavior.
- Mode: chat, mission definition, mission execution, review, onboarding,
  connector/tool use, or recursive subagent/RLM.
- Current baseline suite and must-not-regress cases.
- Existing prompt refs, prompt packet refs, tool manifest hash, skill refs, and
  model/provider refs when available.
- Allowed tools, forbidden tools, forbidden behaviors, required readbacks, and
  governance posture.
- Dataset target: golden, regression, challenge, canary, trajectory, or
  app-origin baseline.
- LangSmith mirror posture when selected examples are used: manifest path,
  dataset name, sync receipt ref, and whether the check/apply readback was
  local-only or remote-checked.
- Required proof surface: deterministic scorer, semantic judge, product UI
  receipt, DB-backed telemetry query, canonical readback, or human judgment.
- Promotion-packet falsification risks when a run could influence product or
  runtime promotion: why the winner might be fake, overfit, shallow, unable to
  affect runtime, or still missing product proof.
- Fixture refs or explicit fixture HOLD for canaries and key regressions. Cases
  with fixture HOLD cannot participate in hillclimb scoring or promotion
  blocking.
- Custom scorer operator contracts before generating fixtures for any operator
  that is not a primitive equality/count/order/containment check.
- Hillclimb mutation scope when the dataset will select or promote candidates.
- Persisted product context refs when a harness decision needs product judgment.
- Flywheel research root or explicit local-only reason for any repeated
  optimization, multi-run comparison, or frontier-planning pass.
- Flywheel experiment brief: research question, hypothesis, comparator, unit of
  work, primary observable, artifact plan, budget cap, stop condition,
  interpretation rule, and next branch if inconclusive.
- Flywheel graph topology plan: parent insight node, empirical run node,
  optional checkpoint/winner nodes, artifact refs, and raw-trace redaction
  policy.
- Receipt destination.

## Situation Map

Before writing or patching cases, classify the situation with
[references/situation-taxonomy.md](references/situation-taxonomy.md).

When the output is a hillclimbing dataset, apply
[references/pressure-grade-dataset-contract.md](references/pressure-grade-dataset-contract.md)
before any freeze recommendation.

When the output is an optimizer, hillclimb, context-composition pass, candidate
generation pass, semantic judge pass, or no-promotion/promotion plan, apply
[references/bitter-lesson-applied-ai-context-engineering-doctrine.md](references/bitter-lesson-applied-ai-context-engineering-doctrine.md)
before changing behavior or recommending promotion.

When the pass is repeated, comparative, multi-run, or intended to guide future
agents, continue or create the Flywheel research root before execution. Keep
local receipts as the proof source and record the Flywheel node refs in the
receipt.

Use the taxonomy to decide whether this pass is:

- core harness loop inside this skill;
- handoff to an existing Ticket Swarm skill;
- a reference-only design task;
- a Flywheel-controlled research branch with runner-framework adoption held out
  of active scope;
- or a candidate for a future standalone applied-AI plugin.

## Product Intent Inference Protocol

When harness engineering needs product judgment, first infer the decision from
persisted product context before asking Danial. Cite source context, assign
confidence, and proceed only when confidence is high and the action stays inside
eval-only/no-promotion harness work.

Routine product decisions should not be escalated when they are already implied
by persisted context such as product walkthroughs, Goal reports, workstream split
notes, pilot profiles, approval packets, requirements gates, source maps, and
prior Danial approvals in receipts.

Ask Danial, or stop at HOLD, when:

- context is missing or contradictory;
- the decision changes promotion-bearing scope;
- the decision accepts or waives a HOLD;
- the decision admits product runtime or canonical truth;
- the decision expands into product UI/UX execution;
- confidence is low;
- candidate promotion is requested.

Each inferred decision must be recorded in the receipt:

```yaml
product_intent_inference:
  decision: "<decision inferred from persisted context>"
  source_refs:
    - "<path or receipt ref>"
  reasoning_summary: "<why the sources imply the decision>"
  confidence: "high | medium | low"
  action_taken: "<proceeded | drafted proposal | held | asked Danial>"
  human_approval_required: true | false
  non_claims:
    - "<what this decision does not prove or authorize>"
```

For Goal 2, apply the detailed protocol in
`docs/operations/sessions/2026-05-20/goal-2-dataset-approval-pack/product-intent-inference-protocol.md`.

## Workflow

### 0. Open The Research Control Plane

For repeated harness research, hillclimbing, scorer/judge iteration, or
frontier planning, establish the Flywheel control-plane node before execution:

- root or parent insight node;
- empirical run node or planned child branch;
- experiment brief;
- artifact plan and redaction/non-upload rules;
- budget cap and stop condition;
- next branch if inconclusive.

Use local receipts for proof and Flywheel for topology. If Flywheel cannot be
used, record `FLYWHEEL_HELD` with the reason before continuing local-only.

### 1. State The Behavior Claim

Write the behavior change in one sentence:

```text
When <context>, the agent should <behavior>, proven by <proof>.
```

Examples:

- "When a user asks for a vague mission, the agent should discover and ask
  focused questions before `mission.define`, proven by tool order and final
  text."
- "When Linear lookup succeeds with excessive calls, the agent should preserve
  the same readback with fewer calls, proven by result equivalence and tool
  count reduction."
- "When a child subagent finds evidence, parent mission truth should not change
  until aggregation accepts the child output, proven by lineage and canonical
  event order."

### 2. Prove Source Provenance

Record:

- trace ref, run ref, session ref, mission ref, task ref, or app-origin case ref;
- prompt packet ref and tool manifest hash when available;
- screenshot/video/accessibility tree refs for product UI behavior;
- canonical state/read model refs for mission/task/review claims;
- whether the trace is backend synthetic, app-origin, or human annotated.

If provenance is missing, stop unless the output is explicitly a proposed case
spec awaiting a source trace.

### 3. Choose The Proof Mechanism

Prefer deterministic checks for:

- tool order;
- required or forbidden tools;
- required readbacks before authority;
- prompt/tool manifest reproducibility;
- node lineage, depth, fanout, and parent refs;
- policy inheritance;
- proof registration before completion;
- app-origin versus backend baseline status;
- latency, tool count, and retry ceilings.

Each deterministic check must name source, selector, operator, expected value,
and failure code. Prose-only deterministic targets are design intent, not a
freeze-ready contract.

Use semantic judges only for:

- elicitation quality;
- delegation quality;
- aggregation quality;
- context partitioning quality;
- human review burden reduction;
- governance clarity;
- whether a compressed artifact is useful to a human.

Do not use a semantic judge to assert deterministic facts that a parser or query
can check.

### 4. Write Or Select Dataset Cases

Every case must include:

- case ref and suite ref;
- mode;
- case lifecycle status;
- invariant family;
- user turn or source trigger;
- setup constraints and allowed tools;
- forbidden tools for invocations only;
- forbidden behaviors for trace/state violations;
- proof surfaces for proof/query/receipt mechanisms that are not tools;
- expected required tools, readbacks, or final text patterns;
- deterministic assertions with source, selector, operator, expected, and
  failure code;
- assertion source/operator values from the approved source, scoring-operator,
  and review-only operator registries;
- failure codes from the shared taxonomy;
- fixture slots for canaries and key regressions;
- semantic rubrics only where needed;
- semantic judge forbidden claims;
- source refs;
- promotion rule;
- hillclimb mutation boundary when applicable;
- must-not-regress cases.

Keep suites small until the contract layer is useful. Do not scale to a broad
benchmark until known-bad traces fail for the expected reason.

Run `pnpm dataset:goal2:validate` for review-mode dataset changes. Run
`pnpm dataset:goal2:validate -- --mode freeze` before any freeze claim; expected
freeze failures must stay explicit HOLDs.

When fixture refs are materialized for a Goal 2 first-batch case, run
`pnpm dataset:goal2:score` and keep the case at `fixtures_materialized` until
false-positive/false-negative review is recorded. Passing fixture scoring alone
is not case freeze.

### 5. Run Baseline Before Patching

Run or identify the narrowest baseline signal:

- focused eval test;
- sampling runner;
- app-origin harness run;
- trace scorer;
- runtime-proof query;
- product UI receipt.

Record the pre-change status. If the current baseline is already HOLD, do not
hide it behind a new recursive or broader suite.

### 6. Patch The Harness

Patch only the smallest owned behavior surface:

- prompt text;
- prompt assembly;
- tool manifest;
- skill routing;
- governance policy mapping;
- context packet composition;
- tool manifest presentation/order;
- decomposition policy text;
- proof obligation templates;
- review packet copy;
- semantic judge prompt variants;
- scorer/judge;
- dataset fixture;
- trace normalization.

Do not patch product code to make a bad harness trace look good unless the
actual product behavior is wrong.

Prefer candidate overlays before worktree patches and no-promotion runs before
promotion-bearing runs.

Do not let hillclimbing mutate scorer logic, dataset cases, fixture labels,
failure-code taxonomy, canonical truth labels, runtime event schema, product
runtime code, UI labels that relabel HOLD/fail as success, or tool authority
policy semantics.

HOLD when reward deltas are not meaningful, when the candidate lever cannot
affect the scorer source it targets, or when the scorer/judge boundary is
unclear.

### 7. Rerun And Compare

Report:

- previous status and new status;
- first failure before and after;
- prompt/tool manifest diff;
- tool-call count, latency, and retry delta when relevant;
- app-origin versus backend-baseline delta;
- canary and must-not-regress status;
- "why this might be fake" falsification risks and the guardrail required to
  remove each risk before promotion;
- new HOLDs and non-claims.

### 8. Route The Result

Route based on what changed:

- Product UI leakage: `ui-abstraction-guard`.
- Human annotation conversion: `annotation-reconciliation-guard`.
- Mission context/definition/runtime/review behavior: mission lifecycle skills.
- Code implementation needed: `implementation-contract-conveyor`.
- Parallel mutating work: `multi-agent-workflow` or worktree lane skills.
- Human product/runtime decision: `ticket-human-review-runtime`.
- Flywheel-backed harness research: update the research node with result,
  artifact refs, HOLDs, interpretation, non-claims, and next branch. Do not
  route to a runner-framework adapter from this workflow; record such ideas as
  out-of-scope unless Danial explicitly opens a separate adoption plan.
- Applied-AI opportunity outside Squad harness: do not force it here; propose a
  standalone applied-AI plugin or a one-off packet.

## Kill Criteria

Kill or hold the loop when:

- there is no source trace, annotation, or explicit proposed case spec;
- invariant family is unknown;
- failure code is missing and no taxonomy update is proposed;
- a prompt edit is proposed without a regression case;
- deterministic assertion cannot name source, selector, operator, expected, and
  failure code;
- deterministic targets remain prose-only but the case is being proposed for
  freeze;
- `forbidden_tools` mixes real tools with conceptual behavior violations;
- canaries or key regressions lack good/bad fixture slots;
- hillclimbing mutation scope is absent for a candidate-selection dataset;
- app-origin-required case lacks split backend/app-origin status;
- scorer/judge tests have not been run for fixtures;
- Goal 1 fresh all-green is required but absent;
- a canary or app-origin HOLD is being renamed as green;
- two prompt/tool patches in a row fail without changing strategy;
- the scorer cannot identify the first upstream failure;
- a semantic judge is being used for deterministic facts;
- a promotion packet or closeout recommendation omits "why this might be fake"
  falsification risks before asking for product/runtime approval;
- fewer tool calls remove required proof or readback;
- a child subagent changes mission truth without parent aggregation;
- a child policy is broader than the parent policy;
- the default product UI requires humans to inspect raw traces;
- repeated or multi-run harness research lacks a Flywheel root/run node and no
  explicit local-only exception exists;
- Flywheel graph state contradicts local receipts;
- Flywheel artifact sync fails for proof-bearing summaries;
- Flywheel summaries claim product runtime, app-origin, canonical, or DB truth
  that local proof has not established;
- Flywheel budget or compute approval is missing for managed compute work;
- raw trace externalization is unsafe or not approved;
- the request is really opportunity mapping or consulting strategy, not Squad
  harness behavior.

## Output

Return a harness-engineering packet with:

- behavior claim;
- situation classification;
- source refs and provenance status;
- dataset cases added or selected;
- deterministic checks and semantic judges;
- baseline status;
- prompt/tool/policy/scorer changes;
- rerun status and regression delta;
- product impact and non-claims;
- falsification risks: why the winning candidate might be fake, overfit,
  shallow, unable to affect runtime, or still missing product proof;
- Flywheel node refs, sync status, artifact refs, interpretation, and next
  branch when Flywheel applies;
- product intent inference records when product judgment was needed;
- next skill or HOLD;
- receipt path.

## Receipt

Receipt must include:

- source trace, case, run, prompt, and tool manifest refs;
- dataset diff or proposed case spec;
- commands/queries run and pass/fail;
- app-origin or backend-baseline status;
- canary and must-not-regress status;
- Flywheel research root/run refs or explicit local-only reason;
- Flywheel sync status, artifact refs, preserved HOLDs, and next branch;
- promotion-packet falsification risks and required guardrails;
- human annotation refs when used;
- product intent inference records when routine product judgment was inferred;
- telemetry/canonical applicability note.

Flywheel-backed harness receipts must expose the research sync fields by name:

```yaml
flywheelRoot:
  node_id: "<root node id>"
  slug_name: "<root slug>"
flywheelNodeRefs:
  - node_id: "<node id>"
    slug_name: "<node slug>"
artifactIndex:
  path: "<local artifact index path>"
  artifact_ids:
    - "<optional Flywheel artifact id>"
syncStatus: "synced | held | not_applicable"
holdBoundary:
  - "<claim or proof surface still HOLD>"
nextBranch: "<next Flywheel branch or explicit none>"
```

Canonical events are not emitted for harness eval activity by default. If a
change admits mission, task, proof, review, readiness, authority, or other
product truth, route that fact through the relevant canonical command/event/read
model instead of treating the trace as truth.
