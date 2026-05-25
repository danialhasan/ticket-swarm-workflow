# Bitter-Lesson Applied AI / Context Engineering Doctrine

Status: active doctrine for Squad harness engineering and context engineering

## Core Claim

Do not over-handcraft intelligence into Squad. Build the environment where
search, feedback, and selection can discover better behavior.

For Squad, the increasingly smart part should be:

- many bounded candidates;
- strong eval pressure;
- trace feedback;
- failure analysis;
- repair and retry/search;
- receipts;
- promotion and rejection decisions.

It should not be:

- one perfect handcrafted prompt;
- one perfect human-designed workflow;
- one giant prompt stack that manually encodes all behavior;
- the configured product reviewer approving every routine micro-judgment.

The catch is that compute only helps when the feedback signal is real. More
compute means more mutation rate. Progress depends on the fidelity of the
selection environment.

## Squad Search-And-Selection Loop

Use this operating loop for harness work:

```text
persisted context
-> inferred product intent
-> candidate behavior generation
-> frozen eval pressure
-> deterministic scoring
-> semantic quality scoring only where appropriate
-> failure analysis
-> candidate repair
-> bounded promotion
-> receipt / rollback
-> dataset expansion from traces
```

## Role Split

Keep these roles separate:

| Role | Owns | Must not own |
| --- | --- | --- |
| Harness | Evaluation environment, guardrails, frozen cases, scorers, fixtures, mutation boundaries, veto order. | Candidate behavior or product runtime truth. |
| Optimizer / hillclimber | LLM-driven search loop over allowed candidate levers. | Dataset truth, scorer logic, fixture expected labels, canonical truth, or product runtime authority. |
| Candidate | A prompt/context/tool/skill/routing behavior configuration proposed for scoring. | Its own score, labels, promotion gate, or evidence truth. |
| Product runtime | Actual Squad app/control plane, commands, canonical events, DB telemetry, product UI, and user-visible lifecycle state. | Eval-only overlay truth unless explicitly admitted through a runtime/canonical slice. |

The harness defines the hill. The optimizer climbs it.

## Repo Authority And Eval Mirror Boundary

Repo-owned harness artifacts remain the source of truth for dataset cases,
schemas, fixture labels, scorers, validators, promotion gates, receipts, and
non-claims. `eval_mirror` may hold selected projected examples and model I/O
readbacks, but it is a mirror, not an authority layer.

An `eval_mirror` example is valid only when its metadata points back to repo truth:
`authority: "repo"`, `source_pack_ref`, `source_pack_path`, `source_git_sha`,
`source_key`, `source_case_hash`, `schema_version`, `scorer_ref`,
`validator_ref`, `proof_surface`, and `selection_reason`. Manual `eval_mirror` edits
are overwritten by the repo sync unless they are exported as a repo patch
proposal first.

Never treat `eval_mirror` dataset state as canonical events, DB telemetry, fixture
truth, scorer truth, or product-runtime promotion proof. `eval_mirror` can help
review model I/O and compare eval examples; product/runtime claims still need
the separate canonical, DB-backed, app-origin, or human-judgment proof surface
that the claim requires.

## Model Responsibilities

Use LLMs for:

- candidate generation;
- candidate critique;
- failure analysis;
- repair proposals;
- reward-case discovery;
- fixture mutation proposals;
- trace clustering;
- receipt synthesis;
- product-intent inference from persisted context.

Do not use LLMs as the source of deterministic truth.

## Deterministic Truth

Machine facts belong to deterministic sources:

- tool traces;
- runtime events;
- DB telemetry;
- RLM context;
- proof registry;
- app-origin traces;
- mutation-boundary hashes;
- fixture and scorer outputs.

Deterministic scorers own machine facts such as event existence, event order,
tool calls, proof refs, lineage, freshness, policy subset, DAG validity,
app-origin/backend split, lifecycle status, fixture labels, and canonical event
existence.

## Semantic Judge Boundary

Semantic judges may score subjective quality only:

- mission sharpness;
- review usefulness;
- human review burden;
- decomposition quality;
- governance clarity;
- RLM legibility.

Semantic judges must not decide:

- event existence;
- tool order;
- proof ref existence;
- policy subset relation;
- app-origin/backend status;
- lineage parent refs;
- depth/fanout budget;
- fixture labels;
- canonical event existence.

If the scorer/judge boundary is unclear, HOLD.

## Falsification-First Promotion Packets

Every promotion packet for a hillclimb winner must include a product-readable
"why this might be fake" section before recommendation. The section must name
the ways automation could be misleading, the proof needed to remove each risk,
and the current HOLD state.

Minimum falsification risks:

- fixture overfit: the candidate learned generated JSON, labels, or
  scorer-visible structure instead of behavior;
- lever mismatch: the candidate names a lever that does not affect the runtime
  target or observable;
- semantic judge overreach: a semantic score is deciding a machine fact;
- headless/runtime gap: the harness path omits frontend, read-model, app-origin,
  canonical, or DB state required for the product claim;
- packet polish: the recommendation is readable while the evidence is still
  missing;
- shallow convergence: repeated candidates converge on generic proof/HOLD
  language without reducing user risk or review burden.

If a promotion packet asks for product/runtime approval without these risks and
guardrails, HOLD.

## Context Engineering

Context is a controlled input surface, not prompt stuffing.

Treat context as:

- selected;
- compressed;
- sourced;
- freshness-aware;
- tied to product intent;
- tied to proof surfaces;
- discardable when stale;
- versioned enough for receipts;
- evaluated against downstream behavior.

Candidate behavior must be tied to scorer-visible sources. A context packet that
cannot affect the scorer source it targets is not a useful optimizer lever; HOLD
or redesign the lever-source mapping.

For prompt and context overlays, preserve cache locality by keeping the stable
base prompt prefix stable. Default new harness candidates to append/composition
after the base and active mode context. A candidate that rewrites, prepends to,
or replaces the base prompt is cache-hostile and needs a separate rationale,
trace proof, and promotion review before it can leave eval-only space.

## Product Intent Inference

When product judgment is needed, infer from persisted context first. Cite the
source context, assign confidence, and proceed only when confidence is high and
the action does not cross a protected boundary.

Ask the configured product reviewer only when:

- context is missing or contradictory;
- confidence is low;
- the decision changes promotion-bearing scope;
- the decision accepts or waives a HOLD;
- the decision admits product runtime or canonical truth;
- the decision expands into product UI/UX execution;
- candidate promotion is requested.

Every inferred product decision must record:

- decision;
- source refs;
- reasoning summary;
- confidence;
- action taken;
- whether human approval was required;
- non-claims.

## Optimizer Levers

Allowed optimizer levers, when the active pack permits them:

- prompt assembly overlays;
- review packet copy overlays;
- context packet composition;
- skill routing;
- tool manifest presentation/order;
- governance policy mapping copy/selection;
- decomposition policy text;
- proof obligation templates;
- semantic judge prompt variants.

Forbidden optimizer surfaces:

- dataset cases;
- scorer logic;
- fixture expected labels;
- failure-code taxonomy;
- canonical truth labels;
- runtime event schema;
- product runtime code;
- tool authority policy semantics;
- UI relabeling of HOLD/fail as success;
- recursive aggregation, parent synthesis, or proof-claim generation unless the
  relevant regression is in the pilot or explicitly accepted as HOLD.

## Compute Policy

Use abundant compute for:

- parallel candidate generation;
- candidate critique;
- failure clustering;
- fixture mutation proposals;
- scorer stress tests;
- reward ablations;
- trace comparison;
- receipt synthesis;
- adversarial search for reward hacking.

Do not use compute for:

- random prompt spam;
- uncontrolled broad rewrites;
- expanding scope without gates;
- mutating the scoreboard;
- generating more cases before the selection signal is trustworthy;
- dumping huge traces on the configured product reviewer.

Every optimization artifact must attach to refs:

- `candidate_ref`;
- `case_ref`;
- `assertion_ref`;
- `fixture_ref`;
- `failure_code`;
- `receipt_ref`.

No unattached prose blobs.

## Operational Rules

- Prefer many bounded candidate attempts over one giant prompt edit.
- Prefer frozen eval pressure over informal judgment.
- Prefer trace-backed failure packets over prose complaints.
- Prefer candidate overlays before worktree patches.
- Prefer no-promotion runs before promotion-bearing runs.
- Reject candidates that improve reward while violating canaries/regressions.
- HOLD if reward deltas are not meaningful.
- HOLD if the candidate lever cannot affect the scorer source it targets.
- HOLD if the scorer/judge boundary is unclear.
- HOLD if a hillclimb promotion packet omits falsification risks before asking
  for product/runtime approval.
- Expand datasets from traces after failure analysis, not as a substitute for a
  trustworthy selection signal.
- Keep human approval gates for promotion, runtime, canonical, HOLD-waiver, and
  product-UX boundaries.

## Non-Claims

This doctrine does not start hillclimbing, enable promotion, mutate runtime
prompts, change tool authority, admit canonical truth, emit DB telemetry, or
change dataset/scorer/fixture truth. It is an operating doctrine for how future
Squad harness and context-engineering work should be framed and reviewed.
