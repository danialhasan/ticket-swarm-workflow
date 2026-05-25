# 15 Mission Lifecycle

Use these skills when a Squad-style product is operating a mission or work-program
lifecycle: context discovery, mission definition, task operation, overview
readback, and post-mission review.

Skills:

- `mission-context-discovery`
- `mission-definition-conveyor`
- `mission-task-operation`
- `mission-overview-readmodel`
- `mission-review-loop`

This group sits between product-truth discovery and implementation contracts.
It is where broad mission intent becomes a governed mission object and where a
running mission keeps re-entering canonical task, proof, review, and telemetry
surfaces.

The operating model is:

- discovery makes the deployed environment legible through ontology,
  epistemology, source authority, and context graph refresh;
- definition converts that context plus elicitation into requirements, a task
  DAG, governance policy mapping, and `Approve & Run`;
- task operation executes autonomous work through discovery, implementation,
  review/verification, and final artifacts;
- overview shows only the minimal mission read model and read-only worker
  transcript;
- review starts from mission surfaces, returns through Mission Overview, and
  then happens as a mission-scoped Chat collaboration.

## Operating Rule

Mission skills are behavior programs for agents. They do not own Squad product
truth.

Truth must come from the host product's canonical workflow owner:

- mission lifecycle tools;
- canonical commands and events;
- current-state read models;
- operating-context queries;
- task/proof/review read models;
- `db_runtime` telemetry and `<proof_query>` surfaces;
- final receipts and artifacts.

In Squad, those concepts may map to names such as `mission_current_state` and
`mission.get_operating_context`, but public users should ask their agent to fill
the equivalent names from their own codebase.

## Flow Map

```text
mission-context-discovery
  -> mission-definition-conveyor
  -> mission-task-operation
  -> mission-overview-readmodel
  -> mission-review-loop
```

The flow can loop:

- missing context sends definition back to context discovery;
- request changes sends approval back to definition;
- task blocker sends operation back to overview/readback;
- failed review sends the user into chat collaboration or a new mission.
- stale environment knowledge sends any mission back to context discovery.

## Proof Discipline

Split proof by claim. A mission is not complete because the worker finished a
runtime loop. A task is not complete because a subagent said done. A UI flow is
not proven by an API test. A proof package is not proven by a screenshot.
