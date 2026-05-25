# Squad Harness Engineering Situation Taxonomy

Use this reference from `$squad-harness-engineering` before deciding what to
patch. The goal is to classify the behavior problem, pick the proof mechanism,
and avoid turning every applied-AI noun into a separate skill.

## Situation Table

| Situation | Signals | Failure Modes | Proof Shape | Route |
| --- | --- | --- | --- | --- |
| Trace intake and provenance | A trace, screenshot, huddle note, app-origin run, or eval output is the source. | Missing run/session/prompt refs; screenshot not tied to trace; app-origin run cannot compare to backend baseline; DB telemetry not queried. | Trace/run/session refs, prompt packet refs, tool manifest hash, app/backend source class, telemetry query when needed. | Core harness loop. |
| Trajectory diagnosis | Output looks plausible but path is wrong. | Wrong tool order; required tool missing; ask-user too early; false context readback; wrong skill under correct-looking output. | Ordered spans, required/forbidden tools, readbacks-before-tools checks, first-failure report. | Core harness loop. |
| Dataset portfolio and promotion | A behavior needs golden/regression/challenge/canary coverage. | Prompt change without cases; canary HOLD hidden; synthetic case replaces app-origin failure; no promotion rule. | Case fixture, suite ref, kind, source refs, promotion rule, must-not-regress list. | Core harness loop. |
| Prompt/tool/policy change | A prompt, tool manifest, or governance mapping will change behavior. | Untracked prompt edits; no manifest/hash; no baseline rerun; tool exposure from prose; no must-not-regress set. | Baseline result, prompt/tool/policy diff, rerun result, canary status. | Core harness loop. |
| Tool-call compression | The agent succeeds but uses too many calls or slow/redundant loops. | Retry loops; broad searches; lower calls lose proof; result changes while count improves. | Equivalent final readback, lower call count/latency, unchanged required proof. | Core harness loop for now; split later if repeated. |
| Mission vs chat routing | User task might be small chat work or long-horizon mission work. | Simple task forced into mission; long-horizon task kept in chat; ambiguous task lacks clarifier. | Routing rubric, task size/uncertainty signals, final suggestion text, no forced mode switch unless approved. | Core harness loop with mission skills as needed. |
| Mission readiness | Repo or environment may not be ready for effective agents. | Weak repo treated as ready; stale/no tests ignored; missing business context hidden; readiness mission not proposed. | Readiness audit, signal inventory, missing proof rails, proposed readiness mission. | Core loop until stable; later candidate standalone skill. |
| Recursive subagents/RLM | Work uses subagents or recursive mission nodes. | First-level delegation claimed as recursion; missing parent refs; child broadens authority; child output becomes truth without aggregation. | Node lineage, depth/fanout, parent/child refs, policy inheritance, aggregation-before-truth checks. | Core loop plus mission lifecycle skills. |
| Governance inheritance | Agent capability is constrained by policy/grant. | Child policy exceeds parent; denial/block path not traceable; UI/prose treated as authority. | Parent/child grant comparison, denied/blocked telemetry, authority packet readback. | Core loop; canonical route if truth changes. |
| UI implementation leakage | Product doorway shows harness internals. | Raw traces, query paths, lifecycle enums, debug labels, or tool timelines are primary UI. | Browser/Electron receipt, forbidden-copy scan, product-route cleanliness check. | Hand off to `ui-abstraction-guard`; return here for eval cases. |
| App-origin vs backend baseline | Backend eval green but product path fails. | Electron/app trace missing status; canary timeout called green; no screenshot/accessibility tree; backend-only claim overstates product. | App-origin run, screenshot, accessibility tree, backend baseline delta, explicit HOLD. | Core harness loop. |
| Scorer and judge design | A behavior needs evaluation logic. | Semantic judge scores deterministic facts; rubric lacks source facts; first upstream failure hidden. | Deterministic parser/query first, judge rubric with source facts, first-failure field. | Core harness loop. |
| Human annotation | Danial or another reviewer marks behavior wrong. | Annotation stays as loose feedback; downgraded to later scope; human attention fills missing machine proof. | Annotation row, classification, conversion to eval or product rule, explicit human decision packet. | `annotation-reconciliation-guard`; return here for dataset cases. |
| Review artifact compression | Many receipts need human review. | Human reads raw child logs; unresolved risk hidden; final artifact lacks receipts/media/proof links. | Root-task artifact, receipt aggregation, media, proof links, unresolved risk. | Mission review skills, with harness cases for repeated behavior. |
| Synthetic/test codebase | Need safe evaluation environment. | Synthetic repo does not match target workflow; fixture replaces live proof; missing verification signals. | Fixture contract, source scenario, expected proof rails, fixture-vs-live boundary. | Core loop for dataset design; implementation contract for code. |
| Model/provider/cost routing | Model or provider choice affects behavior/cost. | Better model hides harness bug; cheaper model loses proof; cost not linked to outcome. | Model ref, prompt ref, cost/tool-call delta, quality and regression comparison. | Core loop; keep light unless repeated. |
| Research control-plane branch | Flywheel can help repeated harness optimization preserve question topology, evidence maps, stop conditions, and next-branch decisions. | Framework adoption replaces the behavior claim; graph state becomes unreviewed truth; managed compute starts without budget; a runner-framework idea re-enters the workflow without a separate adoption plan. | Fit packet with behavior claim, Flywheel role, proof surface, local receipt boundary, budget, artifacts, rollback, and terminal condition. | Branch: Flywheel graph/lookahead/auto for research control planes; keep runner-framework adoption out of active scope unless Danial explicitly opens a separate plan. |

## Plugin Split Criteria

Stay inside Ticket Swarm when:

- the work changes Squad harness behavior;
- the proof depends on mission/task/review/readiness/product truth;
- the output is a dataset, prompt/tool manifest change, scorer, judge, or
  regression receipt;
- a later step naturally routes into implementation contracts, mission skills,
  UI guards, review, or release.

Promote to a standalone `applied-ai-workflow` plugin when:

- the work repeatedly starts before Squad implementation, with client or
  cross-product opportunity discovery;
- the primary output is opportunity map, pilot slice, workflow automation plan,
  data-boundary design, or consulting proof packet;
- the router would need to choose among applied-AI opportunity mapping, pilot
  slicing, evaluation design, deployment operations, and Ticket Swarm handoff;
- the router repeatedly needs to branch among research control planes,
  execution runners, managed compute, and product-runtime proof boundaries
  outside Squad-specific harness work;
- at least two real non-Squad workflows have used the pattern.

Kill the standalone-plugin idea when:

- there is only one real use case;
- the proposed skills duplicate Ticket Swarm, Product Engineer Swarm, Founder
  Content Loop, or Knowledge Artifact Loop;
- the router cannot choose one next step quickly;
- the skill says "AI strategy" without actor, workflow, source system, write
  boundary, and proof surface.

## Minimal Case Template

```json
{
  "caseRef": "suite:kind:slug",
  "suiteRef": "suite:name",
  "kind": "golden|regression|challenge|canary",
  "mode": "chat|mission|review|onboarding|connector|recursive",
  "title": "Human-readable behavior",
  "sourceRefs": [],
  "setup": {
    "allowedTools": [],
    "forbiddenTools": [],
    "contextPacketRefs": [],
    "knownUnknowns": [],
    "constraints": []
  },
  "expected": {
    "requiredToolOrder": [],
    "requiredReadbacks": [],
    "requiredReadbacksBeforeTools": {},
    "requiredFinalTextPatterns": [],
    "requiredLineage": [],
    "maxToolCalls": null
  },
  "rubrics": [],
  "promotion": {
    "candidateFor": "golden|regression|challenge|canary",
    "rule": "Promote only when source trace and proof are stable."
  }
}
```
