---
name: implementation-contract-conveyor
description: Use when approved Squad Design Contract clusters or implementation-readiness rows need to become seam-locked child contracts under the active Implementation Contract parent before ticket-to-human-review execution.
---

# Implementation Contract Conveyor

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when the selected next move is to materialize an
implementation-ready seam into a contract.

Use this skill after `$design-contract-conveyor` and before
`$ticket-to-human-review` contract signoff.

This skill turns approved design truth into implementation contracts. It does
not develop, test, deploy, or release the work. Its job is to compile the
contract that lets the plugin run development/testing through direct skill
composition without improvising.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

## Goal

Create the repeatable implementation conveyor:

```text
approved Design Contract cluster
  -> implementation-readiness row
  -> one seam-locked child under the active Implementation Contract parent
  -> human contract signoff
  -> iterative multi-agent dev/testing composition
  -> machine verification receipts
```

An implementation contract is not "what work should happen." It is the set of
evidence gates and composed workflow loops that must exist before development
and testing may start.

The implementation contract conveyor must normalize approved design clusters
against canon before child creation. A browser-approved surface bundle is not
implementation-ready until it maps to one primary canon seam.

## Use When

- a Design Contract cluster is approved and needs an implementation child
- an implementation-readiness row needs to become a child implementation
  contract under the active Implementation Contract parent
- Danial asks which approved surfaces can start implementation
- a broad wave plan needs to be split into one runnable implementation seam
- an implementation contract is almost ready for human signoff, but still lacks
  a proof matrix, review plan, governance posture, or source-of-truth contract

Do not use this skill when:

- the design cluster is still pending, cut, rejected, or folded into another
  route without an explicit implementation target
- the readiness row is `Needs cleanup`, `Blocked by design`, or `Blocked by
  backend`
- the user asked to execute an already-scoped ticket; use
  the direct dev/testing composition named by the signed-off implementation
  contract
- the work is only daily scheduling; use `$ticket-day-operator`,
  `$calendar-dag-scheduler`, or `$linear-day-allocator`
- multiple unrelated seams are trying to share one implementation child

## Required Inputs

- live Linear readback for the design issue, the active readiness/prep bridge,
  and the active Implementation Contract parent
- approved Design Contract references and approval notes
- browser receipts, screenshots, annotations, or review evidence
- readiness row, route cluster, or target implementation child
- relevant canon and glossary references
- current code surfaces and reusable primitives
- current source of truth and intended canonical inputs
- allowed local UI state, if the ticket is frontend-visible
- command, query, event, projector, realtime, or backend seams
- backend gaps or dependency tickets
- DB/RLS proof requirement, if persisted truth or access boundaries are touched
- human runtime review need, if the ticket changes visible product behavior
- delivery eligibility gate when the work is expected to reach beta users
- high-fidelity requirements map when the contract originates from discovery,
  elicitation, mission setup, orchestration, generative UI, governance, or
  model/eval behavior instead of an already-approved narrow design cluster

Use `/Users/danialhasan/dev/squad/docs/operations/sessions/2026-05-03/implementation-contract-template-v2.md`
as the repo-local template unless a newer template is explicitly accepted.

## Related Skills

Load these only when the current implementation-contract pass needs them:

- `linear:linear` for live issue, status, dependency, checklist, and comment
   readback before creating or updating implementation children.
- `$design-contract-conveyor` only as the source of approved design truth; do
   not reopen design while compiling the contract unless approval is missing.
- `$multi-agent-workflow` for bounded discovery lanes when canon, code,
   Linear, or review evidence need independent confirmation.
- `../references/high-fidelity-requirements-map.md` when the contract is being
   generated from requirements engineering or elicitation rather than a
   previously accepted design cluster.
- `$worktree-lane-orchestrator` only after the contract is accepted and a
   ticket is ready to execute.
- `$ticket-to-human-review` to human-review and sign off the compiled
   implementation contract.
- `$multi-agent-workflow`, `$layered-verification`,
   `$worktree-lane-orchestrator`, `$review-batch-orchestrator`, and related
   skills as the direct dev/testing composition after signoff.
- `$beta-release-assist` only for separate post-development release handoff
   when the human explicitly enters release work.

## Phase 1: Live Topology And Approval Gate

Before drafting the contract, read live Linear.

Confirm:

- active Implementation Contract parent, resolved from live Linear instead of
  hard-coded from a prior project instance
- active readiness/prep bridge, when one exists
- source Design Contract issue is approved
- target child does not already exist, or can be safely updated
- required checklists, blockers, dependencies, and comments are current
- route cluster is not parked, duplicate, canceled, cut, or folded elsewhere

Stop with `Blocked` if approval is missing or the row is not implementation
ready. Do not create a Linear child from stale local notes alone.

Classify each candidate before child creation:

- `READY_AS_WRITTEN`: already maps to one primary seam with dependencies and
  proof obligations named.
- `SPLIT_REQUIRED`: approved design truth is valid, but the candidate bundles
  multiple independently runnable seams.
- `CANON_PROPOSAL_REQUIRED`: implementation would harden a new product noun or
  ownership boundary that canon has not accepted.
- `DELIVERY_BLOCKED`: development may continue, but beta exposure cannot be
  promised because Section `21` delivery truth is not ready.
- `PARKED`: not part of the active implementation wave.

## Phase 2: Implementation Identity

Name the contract in both product and tracker language.

Capture:

- Linear parent and proposed child id/title
- source Design Contract issue ids
- source readiness/prep row
- target route, state, or product surface
- owner and intended execution wave
- user-relief sentence
- one done signal that a human can observe

If the user-relief sentence or done signal cannot be made concrete, the
contract is not ready.

## Phase 3: Seam Lock

Lock exactly one primary seam.

Define:

- primary implementation seam
- explicit non-goals
- accepted design rules
- rejected, cut, or parked ideas
- dependent backend or design work
- allowed implementation breadth
- what would make the ticket too broad and force a split

If two independently shippable surfaces appear, split the contract before
execution.

Common split rules for the first mission loop:

- Chat mission proposal, mission definition admission, kickoff/grant, and
  start-run command UX are separate seams.
- Task spine/progress and selected task/attempt inspector are separate seams
  unless a child owns only generic inspector chrome.
- Proof readiness, proof package surface, review decision input, and lifecycle
  consequence application must remain separate.
- Settings policy definitions and mission execution grants are separate
  surfaces.
- `ContextGraph` is a representation of `ContextBundle`, not a standalone
  runtime truth object unless canon is changed.

## Phase 4: Canon, State, And Data Contract

Extract the system truth the implementer must obey.

If a high-fidelity requirements map exists, cite it here and preserve its
claim/proof split. Do not compress distinct data exposure, UI state,
runtime/tool, persistence, governance, eval, and human-judgment claims into one
implementation task unless the map explicitly binds them to the same proof
surface.

Record:

- canon references and obligations
- glossary terms that must not drift
- current runtime source of truth
- intended canonical inputs
- forbidden duplicate-truth patterns
- allowed local UI state
- commands, queries, events, projectors, realtime channels, or IPC surfaces
- backend gaps and linked tickets
- migration or DB/RLS implications
- open questions that block implementation

Keep product language visible. Internal architecture is included to constrain
the work, not to become the user-facing story.

## Phase 5: Mission Governance Grant

When the implementation touches mission startup, autonomous execution, external
actions, or approval posture, compile the governance grant as a first-class
contract section.

Answer:

- what capabilities the agent must ask for before the mission starts
- which data sources are needed
- which action permissions are needed
- which approval boundaries should be assigned to the mission
- whether existing governance policies cover the run
- whether a missing policy definition must be proposed before execution

This is an elicitation surface for mission autonomy: the user should be able to
approve or constrain the grant before a long run begins.

## Phase 6: Iterative Dev/Test Composition

Map the contract onto the compute-heavy development/testing composition that
will run after signoff.

Capture:

- required lanes and owners
- which files or modules each mutating lane may touch
- whether one worktree is enough or parallel worktrees are justified
- serialized resources, especially browser, Electron, DB, or migration proof
- lane fan-out through `$multi-agent-workflow`
- non-author review swarm
- patch and re-review loop until zero blocking findings
- `$layered-verification` loop until green or true blocker
- UI/Electron verifier lane when required
- Computer Use focus preflight for UI/Electron proof: exact Electron app path, raised/focused window, and real renderer HTML content in the accessibility tree before clicks or visual judgment
- persisted/DB-backed proof row when required
- receipt destinations

This composition is not linear. The contract should make it clear where the
system is expected to spend more tokens/compute to improve quality.

## Phase 7: Assumption Falsification And Verification Gates

Select proof before execution starts.

The contract must name:

- assumptions falsified before ticket creation
- assumptions that must be falsified during implementation
- assumptions allowed to survive closeout
- assumptions that would become blockers
- failing RED test, fixture, smoke, or product proof to create first
- smallest GREEN change that can satisfy the seam
- required repo floor commands
- required layered verification rows with workflow owner and reason
- DB/RLS proof class when applicable:
  `service-role`, `authenticated RLS`, `authenticated denial`, `anon denial`,
  `cross-user denial`, or `mixed`
- Browser Use or Electron route path for visible UI
- degraded, recovery, or error states that must be checked
- proof that can be deferred, with a reason

Do not let implementation begin with only a prose plan.

## Phase 8: Contract Signoff, Receipts, And Release Boundary

Define how the contract crosses human signoff and how later development/testing
will prove the seam.

Capture:

- non-author review focus
- abstraction-drift or duplicate-truth review need
- simplification review need
- contract signoff path through `$ticket-to-human-review`
- receipt paths to create
- Linear checklist and comment updates
- machine verification receipt requirements
- explicit deployment/release boundary
- release eligibility gate through Section `21` when beta exposure is expected

`SIGNED_OFF` from `$ticket-to-human-review` means the implementation contract is
approved for development/testing. It does not mean the work is implemented,
verified, deployed, or released. Deployment/release is handled by a separate
human-triggered workflow.

If the implementation contract claims a signed-off slice can reach beta users,
it must reference the Section `21` delivery rail and the deploy-readiness packet
required by `$beta-release-assist`. Do not let implementation contracts silently
inherit release capability from the development workflow.

## Contract Object

Use this shape when writing the packet:

```ts
type ImplementationContract = {
  identity: {
    parentIssue: string
    childIssue?: string
    title: string
    sourceDesignIssues: string[]
    sourceReadinessRow?: string
    userRelief: string
    doneSignal: string
  }
  designApproval: {
    status: "Approved"
    receipts: string[]
    acceptedRules: string[]
    rejectedOrParked: string[]
  }
  implementationPacket: {
    seam: string
    nonGoals: string[]
    codeSurfaces: string[]
    dependencies: string[]
  }
  canonBrief: {
    canonRefs: string[]
    sourceOfTruth: string
    canonicalInputs: string[]
    allowedLocalState: string[]
    forbiddenDuplicateTruth: string[]
  }
  laneMap: string[]
  worktreePlan: string
  devTestComposition: string[]
  reviewLoop: string[]
  patchLoop: string
  verificationMatrix: string[]
  dbProofRequirement?: string
  contractSignoffPlan: string
  reconciliationPlan: string
  closeout: string
  releaseBoundary: string
}
```

## Output

Return a compact packet with:

- readiness verdict: `Ready for contract signoff`, `Needs cleanup`, or
  `Blocked`
- proposed or updated Linear child
- implementation contract body
- SDLC composition map for development/testing
- required receipts
- first execution command or next workflow skill
- explicit blocker reason for anything incomplete

If Linear mutation is requested, create or update the implementation child only
after live readback and action-time user approval. If mutation is not approved,
return the proposed ticket body and mark it ready for creation.

## Close Rule

This skill is complete when:

- approved design truth was traced to the implementation contract
- the implementation seam is singular and concrete
- the source-of-truth and local-state boundary is explicit
- contract signoff, iterative dev/testing composition, and proof receipts are
  named
- deployment/release is explicitly out of scope
- the next action is either Linear creation/update or `$ticket-to-human-review`
  contract signoff
