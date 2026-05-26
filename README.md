# Ticket Swarm Workflow

Ticket Swarm Workflow is a repo-local Codex plugin that turns messy product and
engineering work into a sequence agents can safely execute, humans can review,
and teams can trust.

It exists because agentic engineering fails in a very predictable way: agents
move too quickly from "I understand the request" to "I changed the code." The
missing layer is requirements engineering: what problem are we solving, who has
authority, what scenario must work, what would count as fit, what evidence is
valid, and what still needs human judgment?

This plugin is that discipline encoded as workflow.

## Why It Is Structured This Way

The structure comes from the requirements-engineering memo:

[`docs/mastering-requirements-agentic-engineering-and-squad.md`](docs/mastering-requirements-agentic-engineering-and-squad.md)

The Build Future Codex demo deck is available at
[`docs/build-future-codex-demo-slides/index.html`](docs/build-future-codex-demo-slides/index.html).

The core idea from that memo is simple:

> Requirements engineering becomes powerful again because agents can carry its
> discipline without human ceremony fatigue.

For human teams, heavyweight requirements practice often turned into meetings,
templates, and stale documents. For agents, the same practices become leverage:

- stakeholder maps become source-authority maps
- use cases become scenarios
- fit criteria become evals
- non-functional requirements become trust constraints
- traceability becomes review compression
- requirements repositories become context and proof infrastructure

So the plugin is not organized around "write code faster." It is organized
around moving from ambiguity to trustworthy delegation.

```text
messy request / product pressure
  -> requirements and product truth
  -> contracts
  -> planned execution
  -> isolated agent lanes
  -> review and reconciliation
  -> release handoff
```

That order matters. If agents skip the early steps, they can produce impressive
work that proves the wrong claim.

## Bitter-Lesson Applied AI / Context Engineering Doctrine

For model-mediated work, Ticket Swarm follows the doctrine in
[`skills/squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md`](skills/squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md).

The short version:

- prefer search-and-selection over one perfect handcrafted prompt;
- compute only helps when the feedback signal is real;
- the harness defines the hill and the optimizer climbs it;
- LLMs propose, critique, repair, cluster, and synthesize receipts;
- deterministic scorers own machine facts;
- semantic judges score subjective quality only;
- routine product intent should be inferred from persisted context when
  confidence is high;
- human approval gates are reserved for promotion, runtime, canonical,
  HOLD-waiver, and product-UX boundaries;
- context engineering is a controlled input surface, not prompt stuffing;
- candidate behavior must attach to scorer-visible sources and refs.

More compute means more mutation rate, not automatic progress. Selection
fidelity determines whether the extra attempts are learning or noise.

## The Product Value

The user-facing value is not "we have a workflow plugin."

The value is:

> Squad turns messy work into missions your agents can execute and you can
> actually trust.

In a good run, an engineering lead should be able to say:

> I can see what had to be true, what the agents proved, and what still needs my
> judgment.

That is the point of the structure. It lets the team accept or reject delegated
work without rereading the whole agent transcript, every log, and every diff.

## Repository Layout

The plugin has two layers:

- [`skills/`](skills/README.md) is the flat runtime layout consumed by Codex
  plugin discovery.
- [`skill-groups/`](skill-groups/README.md) is the human/agent orientation
  layer. It groups the same runtime skills by the high-level function they
  serve.

Active skills must stay at `skills/<skill-name>/SKILL.md` unless plugin loading
is changed and cache parity is proven. The grouped folders are an overlay so the
source is easier to understand without breaking runtime discovery.

There are currently 25 active runtime skills. Some top-level directories under
`skills/` are support/stub directories, not loadable skills.

Shared public adapter vocabulary lives in
[`docs/taxonomy.md`](docs/taxonomy.md). Use that glossary when a skill mentions
`issue_tracker`, `calendar_provider`, `team_chat`, `db_runtime`,
`eval_mirror`, or release/delivery adapter terms.

## Section Guide

### 00 Routing And Loop Control

Path: [`skill-groups/00-routing-and-loop-control/`](skill-groups/00-routing-and-loop-control/)

This is the front door. It decides the smallest correct next workflow instead
of loading the whole plugin or blindly running a chain.

Skills:

- `ticket-swarm-router`
- `goal-loop-operator`

Why this exists:

Agents are good at continuing momentum. They are worse at asking, "What kind of
work is this actually?" Routing prevents the system from treating discovery,
planning, implementation, review, and release as the same kind of task.

Memo connection:

The memo argues that agentic engineering needs a new definition of "ready."
Routing is where the workflow first asks whether the work is ready for
requirements discovery, contract creation, execution, review, or release.

### 10 Requirements Discovery And Product Truth

Path: [`skill-groups/10-requirements-discovery-and-product-truth/`](skill-groups/10-requirements-discovery-and-product-truth/)

This is the most important section. It preserves user/business truth before the
workflow turns into tickets and code.

Skills:

- `feature-decision-ledger`
- `annotation-reconciliation-guard`
- `ui-abstraction-guard`

Why this exists:

This section prevents the classic agent mistake: proving one requirement and
quietly acting like it proves all of them.

Example:

```text
"Let users connect a `team_chat` provider from inside Squad."
```

That is not one requirement. It splits into different proof surfaces:

- backend can create a managed auth link
- user can start connection from the app
- auth returns through the expected app flow
- connected state is durable and visible afterward
- the agent can use a `team_chat` provider only inside approved scope

A backend receipt cannot prove the user-facing app journey. A screenshot cannot
prove durable state. A human note cannot replace missing machine proof.

Memo connection:

The memo calls context engineering "requirements trawling under a new name."
That means the work is not just retrieving context. The work is deciding what
context is admitted, what authority it has, what assumptions it creates, what
conflicts remain, and what would count as enough to act.

For harness and mission-context work, context is a controlled input surface:
selected, compressed, sourced, freshness-aware, tied to product intent, tied to
proof surfaces, discardable when stale, versioned enough for receipts, and
evaluated against downstream behavior.

This section should produce a high-fidelity requirements map, not just a list.
The map is the compiled product-truth artifact that preserves discovery,
elicitation, source authority, data exposure, proof surfaces, and human
judgment before the workflow turns into tickets.

At minimum, the map should include:

- business/user problem
- actor or stakeholder
- scenario
- adjacent scenarios when they change business requirements
- distinct requirement claims
- requirement type
- fit criterion
- source authority
- assumptions to falsify
- proof surface
- forbidden substitutions
- autonomous verification plan
- human judgment packet
- trace or receipt target
- data exposed to the user, data hidden behind details, and data never exposed
- relevant commands, tools, events, projections, DB tables, UI surfaces, and
  runtime boundaries
- implementation status for each claim: `implemented`, `partial`, `missing`,
  `hold`, or `unknown`

Use [`skills/references/high-fidelity-requirements-map.md`](skills/references/high-fidelity-requirements-map.md)
as the shared output contract.

### 15 Mission Lifecycle

Path: [`skill-groups/15-mission-lifecycle/`](skill-groups/15-mission-lifecycle/)

This section drives a Squad-style mission product lifecycle. It is the bridge from
requirements/product truth into the mission tools, worker loop, Mission
Overview, and post-mission review.

Skills:

- `mission-context-discovery`
- `mission-definition-conveyor`
- `mission-task-operation`
- `mission-overview-readmodel`
- `mission-review-loop`

Why this exists:

Mission work can fail before implementation begins. The failure mode is usually
not that the agent cannot code. It is that the agent never made the environment
legible, never separated ontology from epistemology, never turned requirements
into proof surfaces, or treated runtime activity as product truth.

This section turns those boundaries into runtime skills. Context graphs carry
source authority and falsification rules across codebase, connector,
transcript, memory, and tribal-knowledge sources. Mission Definition uses
canonical tools after discovery, elicitation, requirements engineering, task DAG
decomposition, and governance selection. Task operation re-enters through
task/proof commands and produces a final task artifact. Mission Overview is a
minimal derived read model, not a control panel. Mission Review launches a
mission-scoped Chat after Mission Overview and asks humans for judgment only
after machine proof has been gathered.

### 20 Design And Implementation Contracts

Path: [`skill-groups/20-design-and-implementation-contracts/`](skill-groups/20-design-and-implementation-contracts/)

This section converts approved product truth into work that agents can execute.

Skills:

- `design-contract-conveyor`
- `implementation-contract-conveyor`
- `ticket-to-human-review`

Why this exists:

Ready for delegation is not the same as ready for development. Before agents
start coding, the contract needs to say what problem is being solved, which
files or seams are in scope, what must not be changed, what proof is required,
and what human review should judge.

Memo connection:

The memo says fit criteria are evals in disguise. This section turns fit
criteria into implementation contracts and proof obligations. It keeps agents
from discovering the acceptance target after they have already written the
patch.

### 30 Day Planning And Allocation

Path: [`skill-groups/30-day-planning-and-allocation/`](skill-groups/30-day-planning-and-allocation/)

This section turns board pressure, calendar reality, and dependencies into a
real execution day.

Skills:

- `ticket-day-operator`
- `calendar-dag-scheduler`
- `linear-day-allocator`
- `day-state-updater`

Why this exists:

Engineering work does not happen in an abstract backlog. It happens inside
calendar constraints, dependency order, review windows, blocked lanes, and
limited human attention.

Memo connection:

The memo argues that business events beat feature lists for agent decomposition.
This section asks: what real event are we responding to today, what must move,
what is blocked, who owns the decision, and what proof must exist before the day
can be called successful?

### 40 Execution Orchestration

Path: [`skill-groups/40-execution-orchestration/`](skill-groups/40-execution-orchestration/)

This section splits approved work into safe execution lanes.

Skills:

- `parallel-lane-orchestrator`
- `worktree-lane-orchestrator`

Why this exists:

Parallel agents are powerful only when their ownership boundaries are explicit.
Without lane ownership, agents collide, duplicate work, overwrite each other, or
optimize locally while breaking the larger contract.

Memo connection:

The memo frames agentic engineering as converting ambiguous desired change into
bounded, delegated, verified work. This section is where "delegated" becomes
concrete: lane scope, branch/worktree isolation, serialized resources, and proof
responsibility.

### 50 Review Reconciliation And Human QA

Path: [`skill-groups/50-review-reconciliation-and-human-qa/`](skill-groups/50-review-reconciliation-and-human-qa/)

This section collapses agent work back into something a human can judge.

Skills:

- `worktree-lane-reconcile`
- `review-batch-orchestrator`
- `sequential-ticket-review-queue`
- `ticket-human-review-runtime`

Why this exists:

The product is not "agents did work." The product is "a human can accept or
reject delegated work without reconstructing it from scratch."

Review should not ask the human to redo lint, typecheck, unit tests, browser
proof, or trace collection. Agents should do machine-verifiable work. Humans
should judge the parts that actually require taste, product sense, risk
acceptance, or business authority.

Memo connection:

The memo describes the proof package as the user relief moment. Review
reconciliation maps claims to evidence, identifies stale or missing proof, and
routes only the right residual judgment to a human.

### 60 Release And Delivery

Path: [`skill-groups/60-release-and-delivery/`](skill-groups/60-release-and-delivery/)

This section handles post-merge delivery posture.

Skills:

- `beta-release-assist`

Why this exists:

Merged is not delivered. Release work needs its own receipts: artifact checks,
manifest checks, updater feed verification, release notes, handoff, rollback
posture, and re-release posture.

Memo connection:

The memo's traceability idea applies after merge too. A release claim should be
traceable to artifacts and delivery evidence, not just a green branch.

### 90 Plugin Infra And References

Path: [`skill-groups/90-plugin-infra-and-references/`](skill-groups/90-plugin-infra-and-references/)

This section contains shared references and support material.

Why this exists:

Some workflow rules should be shared by multiple skills: merge close gates,
outcome-first skill contracts, verification expectations, and review rules.
Keeping them in references prevents every skill from inventing its own local
truth.

## What This Is Not

This plugin is not a generic prompt pack. It is not "use more agents." It is not
an attempt to turn engineers into requirements managers.

It is a working example of how requirements discipline can be compiled into an
agentic engineering workflow:

- agents trawl and propose
- humans correct high-leverage truth
- contracts freeze the acceptance target
- agents execute inside bounded lanes
- proof packages compress review
- memory captures learning without treating every generated claim as truth

## Why Teams Should Not Have To Handroll This

This repo-local plugin is useful as a teaching artifact and a way to demonstrate the
workflow. But handrolling and maintaining this kind of workflow is exactly the
kind of operational burden most engineering teams should not have to carry.

[TrySquad.ai](https://trysquad.ai) offers this out of the box: the product
turns messy engineering context into agent-ready missions, tunes the workflow to
your team's practices and team-member traces, and manages the workflow layer so
your team does not have to keep a homegrown agent factory alive.

The point is not more process. The point is less babysitting:

- clearer work before agents start
- fewer wrong-proof failures
- faster human review
- safer parallel execution
- reusable organizational learning

Squad manages the workflow machinery so engineering teams can focus on the
product decisions and the work that actually needs their judgment.

## Start Here

If you are new to the plugin:

1. Read [`skill-groups/README.md`](skill-groups/README.md).
2. Start with `00-routing-and-loop-control`.
3. Do not skip `10-requirements-discovery-and-product-truth` when the problem,
   actor, scenario, fit criterion, proof surface, or decision owner is unclear.
4. Move to contracts only after the acceptance target is explicit.
5. Treat proof and review as product work, not cleanup.
