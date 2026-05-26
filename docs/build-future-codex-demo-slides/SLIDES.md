# Build Future x Codex Demo Slides

Working source for `index.html`.

This file now tracks the current talk plan only. Stale section plans, alternate
openings, old layout mocks, function-shape scaffolding, and option lists have
been removed so the deck source stays production-oriented.

## Current Demo Strategy

The product demo is Squad's recursive language model surface: subagents are
allowed to manage subagents. That is the concrete thing built with Codex.

The first minute follows the host guide:

1. Introduce Danial and why Codex is the surface.
2. Show the product artifact quickly and slowly: Squad running recursive
   language models where subagents can create and manage subagents.
3. Then move into the workflow doctrine that made the artifact possible.

The rest of the deck should not become a long live product walkthrough. After
each major workflow section, insert a sped-up clip of Codex acting out the
workflow:

- requirements engineering
- execution orchestration
- implementation from `/goal`
- layered verification
- closeout receipt packet

Those clips are the main feature. The slides teach the concept; the clips prove
that Codex can act out the workflow.

## Core Thesis

Codex can already move code. The harder problem is making delegated work
trustworthy. The emerging software-factory pattern is not "more agents." It is
the system around the agents: requirements, orchestration, implementation
contracts, layered proof, and reviewable receipts.

For this talk, the proof object is Squad's recursive language model work. The
workflow sections explain how that kind of agentic product work becomes
delegable without turning the human into the control plane.

## Slide Sequence

### Slide 1 - Title Image

On screen: generated title image for using Codex in product and harness
engineering.

Speaker beat:

```text
This is about how I use Codex for product engineering and harness engineering.
The concrete thing I built is a Squad demo of recursive language models:
subagents managing subagents. The rest of the talk is about the discipline that
makes that kind of delegated work reviewable.
```

### Slide 2 - Who I Am

On screen: Danial intro with profile screenshot.

Speaker beat:

```text
I'm Danial Hasan. I'm an applied AI engineer building products and harnesses
with agents. I care less about whether an agent sounds autonomous and more about
whether the system around it creates less friction, more motion, and clearer
review.
```

### Slide 3 - Why Codex

On screen: Codex as product-engineering and harness-engineering surface.

Speaker beat:

```text
I am using Codex because it sits at the point where product work and harness
work meet. It can change the product surface, and it can also change the system
that teaches agents how to do the work.
```

Demo insertion:

```text
Slow first-minute demo:
- Open the Squad recursive language model surface.
- Show the core product behavior: subagents can manage subagents.
- Keep this short. The audience only needs to see what was built before the
  workflow explanation starts.
```

### Slide 4 / 2.1 - Codex For Product Engineering

On screen: product-engineering chapter title.

Speaker beat:

```text
I started the obvious way: brain dump into Codex, refine a plan, and let it
execute. That works for small product changes. The problem appears when the task
has hidden requirements, coordination constraints, and proof obligations.
```

### Slide 5 / 2.2 - It Worked Surprisingly Well

On screen: Codex carrying a real task for 23m13s.

Speaker beat:

```text
The obvious loop was not useless. Codex could move real code and get visible
product changes onto the screen. That is why this is interesting. The baseline
works well enough to expose the next bottleneck: trusted scale.
```

### Slide 6 / 2.3 - Vibe Coding Doesn't Scale Cleanly

On screen: failure-mode slide with external examples.

Speaker beat:

```text
As tasks got chunkier, the failures were not just bad code. Codex could finish
local pieces while missing the real workflow: preserve intent, wire the whole
path, make ownership clear, and leave proof that a human can actually judge.
```

### Slide 7 / 2.4 - Why The Problems Exist

On screen: software engineering iceberg.

Speaker beat:

```text
Code is the visible surface of a larger product object. Under it are
requirements, business constraints, source authority, proof obligations, and
human judgment. If Codex only sees the executable surface, it can produce
working-looking diffs that are semantically incomplete.
```

### Slide 8 / 2.5 - How Do We Fix It?

On screen: transition into old engineering discipline encoded into skills.

Speaker beat:

```text
The fix is not just better prompting. The useful move is to take old engineering
discipline, encode it into skills, and serve it inside the harness. The new part
is that Codex can run that discipline continuously while it works.
```

### Slide 9 / 2.5.1 - Engineering Discipline Map

On screen: requirements engineering, implementation contracts, execution
orchestration, layered verification, receipt closeout.

Speaker beat:

```text
This is the map. Requirements engineering turns messy intent into claims we can
verify. Implementation contracts tell Codex what to change and what not to
touch. Execution orchestration turns work into owned lanes. Layered verification
matches each claim to the right proof. Receipt closeout leaves links a human or
agent can audit later.
```

### Slide 10 / 2.6 - Naive Plan Mode

On screen: requirements engineering problem slide with book cover.

Speaker beat:

```text
Normal plan mode is too naive for real product engineering because requirements
are recursive. The first prompt usually hides multiple actors, scenarios,
sources, assumptions, and proof surfaces. Codex can make a plan from that, but
the plan may be shaped around confidence instead of truth.
```

### Slide 11 / 2.6.1 - What Requirements Engineering Covers

On screen: actors, scenarios, claims, source authority, fit criteria, forbidden
substitutions, verification, human judgment.

Speaker beat:

```text
Requirements engineering gives Codex something concrete to verify against. It
turns intent into actors, scenarios, distinct claims, source authority,
assumptions to falsify, fit criteria, proof surfaces, and the human judgment
packet.
```

Demo insertion:

```text
Sped-up Codex clip:
- Start with a harness optimization task seeded with the database, datasets, the
  existing harness optimizer, the flows document, and LangSmith traces.
- Show Codex running the requirements-engineering skill against that real
  context.
- End on a requirements/proof map that names the actor, scenario, claims,
  assumptions, forbidden proof substitutions, and receipt targets.
```

### Slide 12 / 2.6.2 - Without Requirements Engineering

On screen: plausible but under-specified Codex output.

Speaker beat:

```text
This is what the naive version looks like. It sounds scoped and professional,
but it does not preserve enough of the product truth. The agent turns missing
requirements into implementation activity.
```

### Slide 13 / 2.6.3 - With Requirements Engineering

On screen: verifiable requirements map.

Speaker beat:

```text
With requirements engineering, the output is not just a better plan. It is a map
of what must be true and how we will know. That is the difference between asking
Codex to be confident and giving Codex something it can falsify.
```

### Slide 14 / 2.7 - Worker Orchestration

On screen: execution orchestration problem slide with NASA WBS handbook.

Speaker beat:

```text
Once requirements are split, the next failure is orchestration. Agents can spawn
workers, but workers collide when ownership is vague. The problems show up as
same-file conflicts, stale tests, UI/backend contract drift, missing dependency
waves, and manual branch reconciliation.
```

### Slide 15 / 2.7.1 - What Execution Orchestration Covers

On screen: lane ownership, dependency waves, serialized resources, worktree
isolation, proof responsibility, review convergence.

Speaker beat:

```text
Execution orchestration makes delegation safe. It decides what can run together,
what must serialize, which branch or worktree owns each lane, what proof each
lane owes, and how the work comes back together for review.
```

Demo insertion:

```text
Sped-up Codex clip:
- Start from the approved harness optimization requirements/proof map.
- Show Codex demoing the execution-orchestration skill by building the
  dependency graph and lane plan.
- Capture the skill's visual outputs too: Mermaid dependency diagrams, execution
  waves, lane ownership, and serialized-resource notes.
- End on owned lanes for implementation, tests, UI proof, and review
  convergence.
```

### Slide 16 / 2.7.2 - Without Execution Orchestration

On screen: conflict screenshot.

Speaker beat:

```text
Without orchestration, parallelism looks busy but creates review chaos. Multiple
agents can optimize locally, touch the same abstraction, or assume different
contracts. The human inherits the integration problem.
```

### Slide 17 / 2.7.3 - With Execution Orchestration: Dependency Graph

On screen: Codex clip or dependency graph screenshot for the execution
orchestration skill.

Speaker beat:

```text
The first safe move is the dependency graph. It exposes what can happen in
parallel, what must wait, which surfaces collide, and which proof targets must
converge before the work can be trusted.
```

### Slide 18 / 2.7.4 - With Execution Orchestration: Execution Map

On screen: Codex clip or execution lane map screenshot. The clip should include
the Mermaid diagrams and lane-map artifacts produced by the skill.

Speaker beat:

```text
The second move is the execution map. Codex turns the graph into lane ownership,
isolation boundaries, proof targets, and a convergence path. That is the
difference between worker activity and owned delegated work.
```

### Slide 19 / 2.10 - Goal Executes Contract

On screen: `/goal` -> Linear implementation contract -> dev/test composition.

Speaker beat:

```text
Implementation starts from a signed-off implementation contract in Linear.
Slash goal is not a loose prompt. It points Codex at a ticket that already
contains the seam, non-goals, source of truth, lane plan, proof matrix, and
receipt targets.
```

Demo insertion:

```text
Sped-up Codex clip:
- Start with `/goal` pointed at the recursive-language-model implementation
  contract.
- Show Codex reading the ticket and locating the relevant code surfaces.
- End as Codex enters the bounded dev/test loop.
```

### Slide 20 / 2.10.1 - Implementation Contract Contents

On screen: seam, non-goals, source of truth, lane map, dev/test composition,
verification matrix. Production visual option: a Mermaid diagram where the
overall plan fans out into implementation-contract nodes, and each node carries
its own scope, owner, dependencies, and proof obligations.

Speaker beat:

```text
The implementation contract embeds the earlier discipline into the ticket. It
lets Codex spend compute without expanding the task: one seam, explicit
exclusions, known truth owners, owned lanes, review loops, and proof
obligations.
```

### Slide 21 / 2.10.2 - Implementation Loop

On screen: read contract -> inspect code -> implement -> review and patch ->
receipt.

Speaker beat:

```text
Implementation is where Codex spends most of the compute, but the compute is
bounded. It reads the contract, inspects the existing system, makes the smallest
green change, routes review findings back into patches, and leaves evidence or
a real blocker.
```

### Slide 22 / 2.11 - Layered Verification

On screen: repo floor, property, unit, contract, model, integration, smoke,
DB-backed, Electron/UI, Computer Use, telemetry, receipt verdict.

Speaker beat:

```text
Layered verification lets you trade compute for robust engineering. Every
ticket owes a repo floor unless explicitly not applicable. Then Codex selects
the proof layers that match the work: contract, integration, DB-backed state,
Electron/UI, Computer Use, telemetry, and receipt verdict.
```

Demo insertion:

```text
Sped-up Codex clip:
- Show the verification matrix for the recursive-language-model ticket.
- Show Codex selecting and running the relevant proof layers.
- Include Computer Use as one proof layer, not the whole section.
- End on the receipt packet verdict.
```

### Slide 23 / 2.11.1 - Proof Matches Claim Type

On screen: backend contract, durable state, UI journey, human interaction, and
model behavior mapped to verification layers.

Speaker beat:

```text
Different parts of the app need different verification layers. A backend test
does not prove a UI journey. A screenshot does not prove durable state. Model
behavior needs eval or trace proof. The proof has to match the part of the app
that changed.
```

### Slide 24 / 2.12 - Closeout Receipts

On screen: closeout receipt packet. Next visual pass should use text-left /
screenshot-right with a 30/70 split. Screenshot source:
`CLOSEOUT_RECEIPT_PACKET_EXAMPLE.md`.

Speaker beat:

```text
Closeout tells the human exactly what to review. The packet shows what passed,
what is blocked, what was not claimed, and which receipt links prove each part.
Bring the document up on screen and use it as the human review path.
```

Demo insertion:

```text
Sped-up Codex clip:
- Show the closeout packet being assembled.
- Show the review index and the receipt references the human should inspect.
- End on the human spot-check path and any remaining HOLDs.
```

### Slide 25 / 2.13 - Software Factory

On screen: 50/50 close with thesis copy on the left and factory cross-section
diagram on the right.

Speaker beat:

```text
This ties back to the factory cross-section. Codex can move the code. The hard
part is keeping the context: what the human wants, what the business cares
about, what counts as proof, and why the work is worth doing. The diagram makes
the core point visible: a software factory is a workflow, not a worker.
```

### Slide 26 - Resources

On screen: three QR rows.

Speaker beat:

```text
Three links to take with you. Scan the first QR code for the research. Scan the
second QR code for the plugin that contains the skills discussed in the
presentation. Scan the third QR code to try Squad.
```

Links:

- Research: `https://x.com/dhasandev/status/2057519809017897061`
- Skills: `https://github.com/danialhasan/ticket-swarm-workflow`
- Try Squad: `https://trysquad.ai`

## Capture Checklist

### First-Minute Product Demo

- Record a short, slow demo of Squad recursive language models.
- Show subagents managing subagents.
- Do not over-explain the full workflow here. This is the artifact reveal.

### Requirements Engineering Clip

- Source: messy intent for the recursive-language-model feature.
- Action: Codex turns intent into requirements, proof surfaces, assumptions,
  and receipt targets.
- Insert after slide 11 or between slides 11 and 12.

### Execution Orchestration Clip

- Source: approved requirements/proof map.
- Action: Codex builds dependency graph, Mermaid diagrams, execution waves, lane
  ownership, isolation boundaries, serialized-resource notes, and convergence
  plan.
- Insert after slide 15 or between slides 17 and 18.

### Implementation Clip

- Source: `/goal` against a signed-off Linear implementation contract.
- Action: Codex reads the ticket, inspects code, implements, reviews, patches,
  and records evidence.
- Insert around slide 19 or slide 21.

### Layered Verification Clip

- Source: completed implementation candidate.
- Action: Codex runs selected proof layers and records PASS/HOLD per layer.
- Include Computer Use as a verification layer.
- Insert around slide 22 or slide 23.

### Closeout Packet Screenshot

- Open `CLOSEOUT_RECEIPT_PACKET_EXAMPLE.md`.
- Screenshot the top of the markdown file with the verification index and
  receipt tree visible.
- Use on slide 24 as the right-side image.

## Production Notes

- Keep section `2.8` and `2.9` out of the rendered deck. The talk now jumps
  from orchestration into implementation because requirements and execution
  planning are already signed off.
- Do not add a separate Section 3 lifecycle-function sequence.
- Do not reintroduce old option lists or alternate endings unless the live deck
  needs them.
- Keep speaker beats focused on the recursive-language-model artifact and the
  workflow discipline that made it possible.
- The computer-use QA material belongs inside layered verification as one proof
  layer, not as the main narrative frame.

## Open Production Tasks

- Update rendered slide 24 to the 30/70 text-left / screenshot-right layout
  after the markdown screenshot is captured.
- Record and insert the first-minute recursive-language-model product demo.
- Record the sped-up workflow clips for requirements engineering, execution
  orchestration, implementation, layered verification, and closeout.
- Add the final ending/contact slide only after the demo assets are locked.
