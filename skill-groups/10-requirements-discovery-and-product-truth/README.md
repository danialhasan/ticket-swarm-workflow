# 10 Requirements Discovery And Product Truth

Use these skills before contracts or implementation when the work still depends
on discovery, human annotations, product-surface truth, assumption
falsification, or proof-surface selection.

Skills:

- `feature-decision-ledger`: durable beta thesis, non-goals, parking-lot,
  kill-list, and undecided feature hygiene.
- `annotation-reconciliation-guard`: turns live product annotations or reviewer notes into hard
  reconciliation rows before readiness can be claimed.
- `ui-abstraction-guard`: catches repeated UI/product abstraction failures so
  they become proactive rules, scans, contracts, or checks.
- `squad-harness-engineering`: turns Squad agent behavior, prompt/tool
  manifests, traces, trajectories, and eval datasets into source-backed harness
  repair loops.

This is the anti-handwave layer. It should not stop at a checklist. It should
compile discovery and elicitation into a high-fidelity requirements map that a
later agent, reviewer, or implementation contract can use without reconstructing
the conversation.

For applied-AI and harness work, use the shared doctrine at
[`../../skills/squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md`](../../skills/squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md).
The practical rule is: do not handcraft intelligence into a giant prompt when a
governed search-and-selection environment can find better behavior. Context is a
controlled input surface, not prompt stuffing; it must be selected, compressed,
sourced, freshness-aware, tied to product intent, tied to proof surfaces, and
evaluated against downstream behavior.

The map must name:

- business/user problem
- actor or stakeholder
- scenario and adjacent scenarios
- distinct requirement claims
- requirement type
- fit criterion
- source authority
- assumptions to falsify
- required proof surface
- forbidden proof substitutions
- autonomous verification plan
- human judgment packet
- trace or receipt target

It must also include high-fidelity context aggregation:

- data exposed to the user, data hidden behind details, and data never exposed
- canonical objects, projections, events, commands, tools, and UI surfaces
- status for each surfaced claim: `implemented`, `partial`, `missing`, `hold`,
  or `unknown`
- low/medium/high-fidelity diagrams as needed, with high-fidelity diagrams for
  any mission, governance, runtime, or review flow that will become a contract
- exact current-state evidence and file/doc/source refs
- open decisions separated from machine-verifiable proof

When a discovery pass concerns mission setup, elicitation, orchestration,
generative UI, evals, traces, trajectories, or other model-mediated behavior,
the required output is a high-fidelity map first and a ticket/contract second.
Do not promote the work to implementation until the map makes the data flow,
proof surfaces, dataset/eval obligation, and human judgment packet explicit.

If the work includes optimizer or hillclimb pressure, every artifact should
attach to concrete refs such as `candidate_ref`, `case_ref`, `assertion_ref`,
`fixture_ref`, `failure_code`, or `receipt_ref`. Unattached prose is not a
selection signal.
