---
name: ui-abstraction-guard
description: Use after the configured product reviewer has annotated a UI failure pattern and future agents should proactively find, classify, and route the same class of product-surface abstraction mistake without requiring repeated manual annotation.
---

# UI Abstraction Guard

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected problem is a repeated UI/product abstraction
failure that should be prevented, scanned, or routed without more manual
annotation.

Use this skill when prior human UI annotations reveal a reusable product rule
and the system should stop asking the configured product reviewer to point at every repeat instance.

This is not an annotation-capture skill. It is an annotation-amortization skill:
turn a few human examples into proactive review, route scanning, contract
routing, and proof requirements.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

## Goal

Reduce repeated human UI annotation work:

```text
few human annotations
  -> reusable product rule
  -> proactive route/component scan
  -> repeated violations grouped by abstraction layer
  -> hotfix / design contract / implementation contract / QA / blocker
```

The skill is complete only when the repeated problem class is named, scanned
for, routed, and no longer depends on the configured product reviewer manually marking every copy.

The skill must also prevent annotation downgrades: once the configured product reviewer marks a visible
surface as wrong, an agent cannot close it by renaming the scope, calling it
outside the golden path, or saying a contract owns it unless the product surface
is fixed, hidden, proven inaccessible, or explicitly deferred by the configured product reviewer.

## Use When

- the configured product reviewer has corrected the same UI problem more than once.
- A visible surface exposes implementation internals, fixtures, debug copy, or
  the wrong product abstraction.
- A component is reused across routes even though each route has a different
  user job.
- Browser annotations show a pattern that should become a reusable review rule.
- The next agent should inspect the app and propose fixes before asking the configured product reviewer
  for more annotation.

Do not use when:

- the issue is one isolated UI bug;
- no reusable rule can be inferred;
- the next step is pure visual polish with no product/workflow implication;
- a designer decision is genuinely missing and cannot be inferred from existing
  annotations, canon, receipts, or product rules.

## Required Inputs

- representative human annotations or receipts;
- route/component surfaces likely to repeat the issue;
- current Browser route when available;
- relevant design packet, canon, glossary, or receipt context;
- active goal loop or ticket scope, if any;
- likely owner rails: existing `SQD-*`, new design contract, implementation
  contract, QA rerun, blocker, or deferral.

## Designer Rubric

Use these questions as the review harness:

1. What is the user trying to decide or understand here?
2. What work has Squad already done for them before they arrive?
3. What is the one primary action or next movement?
4. What should be visible without asking?
5. What should be hidden until Show why, inspect, or review?
6. What would make this feel like a product surface instead of a debug surface?
7. What canonical truth powers this view?
8. What must this screen never pretend to know?

## Abstraction Layers

Classify each repeated issue at the highest layer it touches:

- `journey`: the user's current lifecycle moment is wrong.
- `screen-job`: the screen is doing the wrong job.
- `primary-movement`: the next action is unclear, missing, or buried.
- `information-hierarchy`: default-visible content should be hidden, or hidden
  content should be visible.
- `component-abstraction`: the wrong component/composition is used for the job.
- `copy-abstraction`: internal language appears where product language belongs.
- `truth-state`: the view claims, derives, or hides state incorrectly.
- `diagnostics-proof`: proof/debug details appear in primary UI instead of
  details, receipts, or diagnostics.

When in doubt, classify higher. "Remove this card" is often a screen-job or
information-hierarchy rule, not a local component tweak.

## Product-Specific Rule Pack

Carry these rules forward unless later human review changes them:

- Settings is a control surface, not a diagnostics screen.
- Chat is the mission doorway, not a support-readiness dashboard.
- Provider and connector setup should appear as compact `Connect` /
  `Connected` affordances with test/retry where relevant.
- Raw query paths, timestamps, source counts, blocker enums, fixture labels,
  and named-read explanations do not belong in primary UI.
- Debug/proof details belong behind details, diagnostics, receipts, or review.
- A secondary surface needs a visible way back to the app.
- Scroll/overflow is part of reviewability, not polish.
- After the first user message, Chat should become conversation/workflow, not
  remain in hero/orientation state.
- Review should be artifact-centered: inspect artifact, annotate, request
  fixes, approve, reject, or create follow-up.
- "Should not exist" is a route/surface rule, not a copy critique. It requires
  removal, redirect, inaccessibility proof, or explicit reviewer-approved deferral.

## Workflow

### 1. Extract The Rule

Start from representative annotations and compress them into one or more product
rules.

Each rule must answer:

- what repeated mistake should the agent catch next time?
- what user-facing principle does it protect?
- what examples proved the rule?
- what should replace the bad pattern?

Do not preserve every annotation as a task. Preserve the rule that makes future
annotations unnecessary.

### 2. Scan For Repeats

Proactively inspect likely route and component surfaces.

Use:

- `rg` over route/page/component code for repeated copy, components, test ids,
  raw query strings, fixture labels, status enums, and debug phrases;
- Browser for visible route proof when the surface is local and runnable;
- code ownership and existing receipts to find likely `SQD-*` rails.

Look for repeated instances of the rule, not just exact text matches.

### 3. Separate Same Problem From New Question

For each finding, classify:

- `same-problem`: already covered by the learned rule;
- `nearby-problem`: likely same family, but needs a small human/design check;
- `new-design-question`: cannot be inferred safely;
- `not-a-problem`: acceptable because it is in diagnostics, proof, receipt, or
  explicit dev-only mode.

Ask the configured product reviewer only for `new-design-question` or high-impact `nearby-problem`
cases. Do not ask him to re-approve every `same-problem`.

No finding may be downgraded from a human annotation into `not-a-problem` merely
because the current mission can pass without visiting that route. For visible
product surfaces, "outside current happy path" is only acceptable with proof the
readiness user cannot encounter it or with the configured product reviewer's explicit deferral.

### 4. Choose Disposition

Every cluster receives one disposition:

- `hotfix`: tiny local patch needed to keep review/annotation moving.
- `design-contract`: product composition or interaction needs explicit human
  approval.
- `implementation-contract`: approved rule needs owned development scope and
  proof gates.
- `qa-rerun`: existing gate should rerun after the fix.
- `blocker`: prevents readiness/product flow until fixed or made truthful.
- `deferral`: out of current scope with honest visible behavior.

No cluster may remain `misc`, `cleanup`, or `risk`.

If a cluster contains a "should not exist" route or surface, `deferral` is valid
only when the configured product reviewer explicitly approves it. Otherwise the disposition must be
`hotfix`, `implementation-contract`, or `blocker`.

### 5. Hotfix Gate

Apply a hotfix only when all are true:

- the patch is small and local;
- it unblocks annotation, navigation, or basic reviewability;
- it does not settle a larger product abstraction;
- it has an obvious Browser verification path;
- it is recorded as a hotfix, not completion.

Examples:

- add missing overflow so the reviewer can inspect a panel;
- add a back-to-app escape hatch;
- fix a clipped control.

Do not use hotfixes to quietly redesign a surface.

### 6. Route To Ticket Swarm

Choose the next workflow:

- `$design-contract-conveyor` when the product composition, hierarchy, or flow
  still needs human design approval.
- `$implementation-contract-conveyor` when the rule is approved enough to
  become a seam-locked implementation child.
- `$feature-decision-ledger` when the rule changes scope, parking lot,
  kill-list, or non-goal posture.
- `$goal-loop-operator` when the rule changes the current readiness goal ledger,
  blocker ledger, or next loop.
- direct ticket execution only when a signed implementation contract already
  owns the seam.

If a cluster maps to multiple independently shippable seams, split before
implementation.

## Output

Return:

- learned product rule(s);
- example annotations or receipts used;
- proactive scan scope;
- repeated findings grouped by abstraction layer;
- disposition table;
- hotfixes applied, if any;
- new human questions, only where unavoidable;
- next Ticket Swarm skill(s) to invoke.

## Close Rule

This skill is complete when:

- the human annotation pattern became a reusable rule;
- likely repeats were proactively scanned;
- each repeat has an abstraction layer and disposition;
- hotfixes, if any, are verified and recorded as hotfixes only;
- downstream Ticket Swarm routing is explicit;
- the configured product reviewer is not asked to annotate the same class of issue again unless a genuinely
  new design question appears.

It is not complete if a known human annotation is still reachable in primary UI
and the only status is `owned by contract`, `outside golden path`,
`broader scope`, `partial`, or `risk`.
