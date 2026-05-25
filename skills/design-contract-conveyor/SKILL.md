---
name: design-contract-conveyor
description: Use when turning a live browser-backed design review into durable Design Contract tickets, then handing approved route clusters into implementation-contract compilation.
---

# Design Contract Conveyor

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected next move is to convert live human design
steering into durable Design Contract truth.

Use this skill when a Squad frontend route or state needs to move from live
human design steering into execution-ready `issue_tracker` work.

This skill sits before `$implementation-contract-conveyor`. It captures human
taste and product signoff first, then hands approved design truth to
implementation-contract compilation.

## Goal

Turn this loop into a repeatable operating system:

```text
references + live browser context
  -> generated design pass
  -> reviewer steers
  -> Codex records Design Contract truth
  -> approved cluster becomes implementation-contract input
  -> implementation-contract compilation
```

Design Contract tickets capture human taste and product truth. Implementation
contracts convert that approved truth into development/testing-ready contracts.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

## Required Inputs

- active route or route-state
- Design Contract `issue_tracker` issue, or parent issue for creating one
- current session plan or walkthrough file
- medium-fi ASCII packet or route/state tree
- relevant prior design packets, screenshots, annotations, or browser receipts
- current live browser state in `@browser-use`
- implementation contract target, if the route cluster is already approved

## Related Skills

Load these only when the current design-contract pass needs them:

- `$browser-use:browser` for local live UI walkthroughs, DOM snapshots,
   screenshots, route inspection, and visual receipts.
- `$design-interview-loop` for human taste iteration against concrete screens.
- `$medium-fidelity-ascii-design` for recursive screen structure, cut states,
   folded states, and route/state source hierarchy.
- `linear:linear` for Design Contract ticket hygiene and implementation-contract
   ticket updates.
- `$implementation-contract-conveyor` only after the relevant route cluster is
   approved.
- `$ticket-to-human-review` only after the implementation contract is compiled
   and ready for human signoff.
- `$multi-agent-workflow`, `$layered-verification`, and review/optimization
   skills only after implementation-contract signoff.

For local Squad UI walkthroughs, use `@browser-use` with the Codex in-app
browser. Do not use `agent-browser`, `agent-browser-work`, Playwright-driven
Chrome profiles, or `dev-browser` unless the configured product reviewer explicitly asks for that
fallback in the current thread.

## Phase 1: Context Intake

Ground the design pass before generating or editing.

Read:

- the active Design Contract ticket and parent route-family ticket
- current session plan, progress log, and prior receipt folders
- medium-fi ASCII packet and route/state tree
- related implementation tickets when the route cluster is already approved
- relevant claim-boundary or launch-framing notes
- current `@browser-use` URL, DOM snapshot, and screenshot

Record the working context in plain language:

- route/state being reviewed
- user decision on this screen
- next movement after the screen
- visible UI that matters
- hidden or deferred UI
- cut, folded, or non-goal states
- styling or design-system constraints

Do not start implementation-contract compilation or dev/testing execution during
this phase.

## Phase 2: Generate

Create or patch the smallest live UI state that can carry reviewer feedback.

Default generation rules:

- start from the minimum concrete artifact
- preserve existing shell geometry unless the design question is shell geometry
- remove stale explanatory or debug composition before adding new product UI
- make the center panel own the primary work unless the route contract says
  otherwise
- keep right-side panels quiet until a selected item, file, artifact, or
  inspector target exists
- use semantic design-system tokens and existing primitives/composites
- avoid route-local styling truth

The generated pass is allowed to be incomplete. It must be concrete enough for
human steering.

## Phase 3: Human Steering

The configured product reviewer reviews the live route/state through `@browser-use` annotations,
screenshots, and direct feedback.

Codex should translate feedback into reusable design rules, not isolated tweaks.

Examples:

- "remove this" -> delete the composition from the active surface, not the
  reusable component unless asked
- "this panel is movement, not explanation" -> keep the panel focused on
  navigation/actions and remove helper prose
- "start with the composer" -> make the center composer the product anchor
- "keep continuity honest" -> expose readiness/retry/recovery and avoid hidden
  failover claims

After each steering checkpoint, update the active route/state before asking for
the next reaction when implementation mode is allowed.

## Phase 4: Learn And Record

After every `@browser-use` design checkpoint, Codex owns `issue_tracker` and filesystem
hygiene.

Update the relevant Design Contract ticket with:

- approval status: `Pending`, `Approved`, `Rejected`, `Cut`, or `Folded`
- accepted feedback
- rejected feedback
- open questions
- screenshot or browser receipt references
- styling contract and preset behavior
- implementation contract target, if approved

Update the durable session file with:

- route/state reviewed
- `issue_tracker` issue id
- decision and product rule
- receipt path
- next route/state

Save screenshots or browser receipts under the session receipt folder. Do not
leave important context only in chat.

## Phase 5: Approval Gate

Do not create implementation contracts or run dev/testing until the route
cluster is approved.

Approval rules:

- `Pending`: still under design review
- `Approved`: can feed an implementation contract
- `Rejected`: needs another design pass
- `Cut`: should stay visible in tracking but must not generate implementation
  work
- `Folded`: implemented or reviewed as part of another approved route/state

Do not infer approval. Require explicit human approval or an explicit prior
signoff record.

## Phase 6: Implementation Contract Handoff

Once a route cluster is approved, hand it to `$implementation-contract-conveyor`
to create or update the implementation contract.

The handoff must include:

- approved Design Contract refs
- screenshot and browser receipt refs
- explicit non-goals
- frontend composition and local state scope
- API, query, command, or backend seams
- backend gaps or linked backend tickets
- browser-use smoke path
- `$layered-verification` layers and repo health floor
- DB/RLS proof class when auth, session, persisted readiness, projections, or
  product truth are touched
- non-author review focus

Then route the compiled implementation contract into `$ticket-to-human-review`
for contract signoff. Development/testing starts only after signoff and is run
through the composed workflow named by the implementation contract.

## Close Rule

This skill is complete for a route/state only when:

- the live browser review surface was inspected or generated
- reviewer feedback was converted into explicit design rules
- the Design Contract ticket was updated
- receipt references were saved
- the session progress log was updated
- approval status is explicit
- no implementation contract was created before approval
- approved route clusters have a clear implementation-contract target

## Output

Return:

- active Design Contract issue
- route/state status
- accepted design rules
- rejected or deferred ideas
- receipt paths
- next route/state
- implementation contract target, when approved
