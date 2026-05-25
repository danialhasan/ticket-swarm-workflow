# Skill Groups

These folders describe the high-level function of the Ticket Swarm Workflow
skills. The entries inside each group are links back to the active flat runtime
skills under `../skills/`.

## Lifecycle Map

| Group | Function | Use Before |
| --- | --- | --- |
| `00-routing-and-loop-control` | Select the smallest correct workflow and operate broad loops. | Everything else |
| `10-requirements-discovery-and-product-truth` | Preserve user/business truth, reconcile annotations, falsify assumptions, and prevent proof-surface substitution. | Contracts |
| `15-mission-lifecycle` | Drive Squad mission discovery, definition, task operation, overview readback, and review. | Mission runtime and review |
| `20-design-and-implementation-contracts` | Turn approved product/design/readiness rows into implementation contracts and human signoff. | Execution |
| `30-day-planning-and-allocation` | Convert board pressure, calendar reality, and dependencies into an execution day. | Lane work |
| `40-execution-orchestration` | Split approved work into parallel or isolated execution lanes. | Review |
| `50-review-reconciliation-and-human-qa` | Collapse lanes, batch or sequence review, and run human product QA. | Release |
| `60-release-and-delivery` | Verify post-merge delivery posture and prepare release handoff. | External delivery |
| `90-plugin-infra-and-references` | Shared references, setup notes, and non-runtime support material. | Any skill that cites them |

## Operating Rule

Requirements discovery and product-truth skills must run before contract,
execution, or release skills whenever the problem, actor, scenario, proof
surface, or decision owner is unclear.

If the router is unavailable in the active runtime cache, manually apply this
taxonomy and record the cache/source drift in the closeout.
