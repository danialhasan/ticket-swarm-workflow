# Pressure-Grade Dataset Contract

Use this reference from `$squad-harness-engineering` when a dataset will govern
prompt, tool, policy, routing, recursive-agent, or semantic-judge hillclimbing.

## Intent vs Pressure

Intent means the case says the right behavior.

Pressure means the case can fail a bad trace for the right reason and pass a good
trace without false positives.

Do not freeze a hillclimbing dataset while it is only intent. Hillclimbing will
optimize against whatever the scorer can observe.

## Required Case Shape

Every pressure-grade case needs:

- `case_ref`
- `kind`: `golden`, `regression`, `challenge`, or `canary`
- `case_lifecycle_status`
- `invariant_family`
- `allowed_tools`
- `forbidden_tools`
- `forbidden_behaviors`
- `proof_surfaces`
- `deterministic_assertions`
- `failure_codes`
- `fixtures`
- `semantic_judge_targets`, only when needed
- `semantic_judge_forbidden_claims`
- `promotion_rule`
- `promotion_blocking`

`forbidden_tools` is for invocations only. Conceptual violations such as
`backend_green_masks_app_hold` or `human_attention_as_missing_machine_proof` are
behaviors, not tools.

## Case Lifecycle

Use explicit lifecycle status:

- `idea`: behavior risk identified, not yet case-shaped
- `proposed`: case drafted, not yet schema-valid
- `schema_valid`: case passes schema and review validation
- `fixtures_materialized`: required good/bad fixtures exist
- `scorer_calibrated`: known-good passes, known-bad fails with expected failure code
- `frozen`: eligible for hillclimb selection or promotion gates
- `retired`: inactive

Human approval belongs in case `status`. Machine/process readiness belongs in
`case_lifecycle_status`. Only `scorer_calibrated` or `frozen` cases may
participate in hillclimb scoring. Only `frozen` canaries may block promotion.
Cases with fixture HOLD cannot score or block promotion.

## Deterministic Assertion Shape

Each machine-checkable target must be explicit:

```json
{
  "source": "runtime_events",
  "selector": "$.events[?(@.type=='proof.registration.created')].payload.aggregationRef",
  "operator": "references_event_where",
  "expected": {
    "type": "agent.aggregation.accepted",
    "status": "accepted"
  },
  "failure_code": "PROOF_REGISTERED_WITHOUT_ACCEPTED_AGGREGATION"
}
```

If the source, selector, operator, expected value, or failure code is not known,
the case can remain a proposed idea but must not be frozen.

## Assertion Source And Operator Registry

Assertion `source` must come from the approved source registry. Scoring
operators must come from `scoring_operator_registry`. Review-only operators must
come from `review_only_operator_registry` and cannot score. New sources or
operators require a contract update before case freeze.

Allowed source examples:

- `runtime_events`
- `rlm_context`
- `proof_registry`
- `review_packet`
- `app_origin_trace`
- `backend_baseline_trace`
- `ui_accessibility_tree`
- `browser_media_receipt`
- `db_telemetry_query`
- `workspace_inspection`
- `connector_readiness`
- `normalized_tool_calls`
- `normalized_trajectory`
- `eval_packet`
- `semantic_judge_output`

Scoring operator examples:

- `equals`
- `equals_field`
- `not_equals`
- `exists`
- `not_exists`
- `contains`
- `not_contains`
- `not_contains_any`
- `ordered_before`
- `references_event_where`
- `subset_of`
- `no_event_matching`
- `all_events_match`
- `count_equals`
- `count_lte`
- `count_gte`

Custom scoring operators must have a short operator contract before fixture
generation. The contract must name input shape, pass condition, fail condition,
first-failure behavior, and good/bad fixture sketches.

`operator: "satisfies"` is review-only intent. It belongs only in
`review_only_operator_registry` and is not allowed in scorer-calibrated or
frozen cases.

## Invariant Families

Use these families as the coverage map:

- lineage / recursion
- policy / authority
- aggregation truth
- proof registration
- readiness / completion
- context grounding
- app-origin / read-model truth
- UI review surface
- retry / trace integrity
- simple-task non-recursion
- semantic judge boundaries
- hillclimb mutation boundaries

Every family does not need every suite type, but core safety families should
have promotion-blocking canaries.

## Fixtures

For canaries and key regressions, include both:

- a good trace that should pass
- a bad trace that should fail with the named `expected_failure_code`

A regression without a bad trace may be useful design intent, but it has not yet
proved scorer pressure.

Regression/canary cases without negative fixtures cannot participate in
hillclimb scoring. Canary cases without positive and negative fixtures cannot
block promotion.

## Scorer Calibration

A case is not pressure-grade until the scorer proves:

- the good fixture passes
- the bad fixture fails
- emitted failure code equals `expected_failure_code`
- failure output includes the relevant `assertion_ref`
- semantic judges did not decide deterministic facts
- false-positive and false-negative results were reviewed

Before freeze, two independent scorer implementations or review lanes should
interpret `source`, `selector`, `operator`, `expected`, and `failure_code` the
same way.

## Semantic Judge Boundary

Semantic judges may score subjective workflow quality. They may not decide:

- file existence
- event ordering
- tool invocation count
- policy subset relation
- proof ref existence
- backend/app-origin status
- lineage parent refs
- depth/fanout budget
- source hash or timestamp
- connector readiness
- canonical event existence

Machine facts belong to parsers, queries, trace scorers, or app-origin receipts.

## Hillclimb Mutation Scope

Define allowed and forbidden mutation surfaces before starting a hillclimb.

Allowed examples:

- prompt variants
- prompt assembly
- routing policy copy/weights
- decomposition policy text
- review packet copy
- semantic judge prompt variants

Forbidden examples:

- scorer logic
- dataset cases
- canonical truth labels
- fixture expected labels
- runtime event schema
- product runtime code
- tool authority policy semantics

The optimizer must not be allowed to make the scoreboard easier.

## Promotion Decision Order

Evaluate promotion in this order:

1. Any dataset validation failure blocks review/freeze.
2. Any freeze-validation failure blocks hillclimbing.
3. Any frozen canary failure rejects the candidate.
4. Any policy/authority or other promotion-blocking deterministic failure
   rejects the candidate.
5. Any app-origin-required HOLD/fail rejects the candidate unless scoped out
   before approval.
6. Any scorer infrastructure error is HOLD, not PASS.
7. Semantic judge failure can reduce score, but cannot override deterministic
   pass/fail.

## Canonical Truth / Telemetry Boundary

Dataset docs and synthetic fixtures do not admit canonical product truth. Only
runtime/control-plane events, DB-backed telemetry, or approved mission lifecycle
transitions can admit product truth. If a harness change admits mission, task,
proof, review, readiness, or authority truth, route it through the relevant
canonical command/event/read model.

## HOLD Conditions

Stop and mark HOLD if:

- source trace, annotation, or receipt is missing and cannot be honestly marked
  `source_missing`
- invariant family is unknown
- failure code does not exist and no taxonomy update is proposed
- deterministic assertion cannot name source, selector, operator, expected, and
  failure code
- canary or key regression lacks fixture refs or explicit fixture HOLD
- semantic judge is asked to decide machine-checkable facts
- hillclimb mutation scope is absent for a dataset that will select/promote
  candidates
- app-origin-required case lacks split backend/app-origin status
- scorer/judge tests have not been run for fixtures
- Goal 1 fresh all-green is required but absent

## Freeze Checklist

Do not freeze until:

- every deterministic assertion has source, selector, operator, expected value,
  and failure code
- every failure code exists in the taxonomy
- tools and behaviors are separate
- every canary is promotion-blocking
- every canary and key regression has good/bad fixture slots
- known-bad fixtures fail with the expected failure code
- known-good fixtures pass
- scorer output includes assertion refs
- two independent scorer/review lanes interpret assertion fields the same way
- semantic judges cannot decide machine facts
- app-origin and backend status remain separate
- hillclimb mutation scope is explicit
- Goal 1 has a fresh all-green closeout when Goal 2 execution is about to begin
