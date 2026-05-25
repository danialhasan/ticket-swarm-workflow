# Mastering The Requirements Process Through Agentic Engineering

Date: 2026-05-13
Source basis: reading pass over `Mastering the Requirements Process`, fourth edition

## Thesis

The book is more important for agentic engineering than it was for ordinary software teams.

For human teams, requirements engineering often became expensive coordination ceremony. Humans resist templates, skip provenance, compress uncertainty socially, and can use tacit organizational context to repair vague instructions.

Agents invert that cost curve. The things humans experienced as bureaucratic overhead become leverage:

- explicit scope becomes permission boundary
- stakeholder maps become source-authority maps
- business events become decomposition units
- fit criteria become evals
- non-functional requirements become trust constraints
- traceability becomes review compression
- rejected prototypes become anti-drift memory
- requirements repositories become context and proof infrastructure

The memetic advantage is not that agents should copy old requirements documents. It is that agents can execute the underlying discipline continuously, cheaply, and without social fatigue.

Agentic engineering is therefore not prompt engineering plus tools. It is the practice of converting ambiguous desired change into bounded, delegated, verified work through explicit context, authority, constraints, proof, and review loops.

## Part One: Field-Level Reading

### 1. Requirements Engineering Becomes The Missing Operating System For Delegation

The core problem in agentic engineering is not "how do we get the model to answer?" It is "how do we make delegated work safe to start, inspectable while running, and trustworthy enough to accept?"

The book gives the old discipline for this:

```text
purpose
  -> scope
  -> stakeholders / authority
  -> business events
  -> use cases / scenarios
  -> requirements / constraints
  -> fit criteria
  -> design / implementation
  -> proof / review
  -> change management
```

For agents, that becomes:

```text
user intent
  -> mission boundary
  -> source authority
  -> event/task partition
  -> context graph
  -> task contract
  -> eval/proof criterion
  -> tool/action run
  -> evidence package
  -> human review
  -> memory candidate / invalidation
```

This is the spine of serious delegated work.

### 2. Context Engineering Is Requirements Trawling Under A New Name

The book's strongest operational verb is trawling: search, interview, model, compare, extract, test, and refine until the real requirements become visible.

Most current "context engineering" talk collapses this into retrieval, prompt stuffing, or long-context formatting. The book says that is too shallow. The work is not merely finding related material. The work is deciding what material is admitted, how it is interpreted, what authority it has, what assumptions it creates, what conflicts remain, and what would count as enough to act.

Context engineering should therefore own:

- source admission
- authority ranking
- scope partition
- assumption and conflict tracking
- viewpoint separation
- candidate solution comparison
- fit-criteria extraction
- trace to proof and review

Retrieval is just one input.

### 3. Business Events Beat Feature Lists For Agent Decomposition

Agents tend to over-decompose by surface noun: route, component, file, ticket, doc, API endpoint, workflow step.

The book's business-event framing is better. A business event is an outside happening that the work must respond to. It forces the agent to ask:

- what triggered this work?
- who or what experienced the event?
- what information arrived?
- what decision or state change must happen?
- what output proves the response was correct?

This is a better primitive for agentic engineering because it couples context, action, and proof. It also prevents agents from optimizing the visible interface while missing the actual work event.

### 4. Brown Cow Thinking Is A Cure For Agent Solution Lock-In

The Brown Cow model separates:

- current implementation
- current essence
- desired essence
- future implementation

This matters because agents are dangerously fluent at improving the current artifact without asking whether the artifact is the real system.

For agentic engineering, every context object should be taggable by viewpoint:

- Are we describing the current mess?
- The underlying need?
- The desired future behavior?
- A proposed implementation?

Without this, agents automate existing dysfunction, mistake prototypes for decisions, and preserve accidental complexity.

### 5. Fit Criteria Are Evals In Disguise

This may be the single strongest translation.

The book's fit criterion asks: how will we know this requirement has been satisfied?

Agentic engineering asks: how will we know the agent's work is correct enough to accept?

Same question.

For agents, fit criteria should exist before execution. They should shape:

- task contracts
- tool permissions
- test plans
- proof package requirements
- acceptance criteria
- reviewer instructions
- stop conditions

An agentic system without fit criteria is a system that delegates work before defining what trust means.

### 6. Non-Functional Requirements Are Trust Requirements

In ordinary software, NFRs are often treated as late polish: performance, security, usability, accessibility, observability, maintainability.

For agentic systems, they are trust gates.

The delegated work can be functionally correct and still unacceptable if it is:

- unauditable
- unrecoverable
- inaccessible
- too slow to inspect
- insecure
- impossible to roll back
- culturally wrong for the team
- too hard to review
- dependent on hidden model judgment

Agentic engineering should treat NFRs as first-class trust requirements.

### 7. Requirements Repository Becomes Context/Proof Infrastructure

The old repository idea should not return as a giant requirements database. It should return as a living trace system.

The useful unit is not "a requirement document." The useful unit is a connected claim:

```text
source
  -> authority
  -> requirement / assumption / constraint
  -> rationale
  -> fit criterion
  -> task / action
  -> evidence
  -> review decision
  -> change / invalidation
```

This is exactly what agentic systems need to avoid invisible context drift.

### 8. AI-Generated Requirements Are Inputs, Not Truth

The book's AI posture is refreshingly sober: AI can generate questions, candidates, drafts, and analysis prompts, but its outputs need review.

That matters for agentic engineering because the field will be tempted to let agents generate their own requirements, certify their own scope, run their own tasks, and mark their own proof as sufficient.

The safer model:

- agents may propose requirements
- agents may compare and critique them
- agents may expose missing questions
- agents may generate fit criteria
- agents may assemble proof
- but admission into truth requires provenance, criteria, and review

The agent can accelerate analysis. It cannot be the only authority for the analysis it then acts on.

## What This Means For Agentic Engineering As A Field

### The Field Needs Three Core Objects

1. Work program

A durable unit of delegated work with objective, scope, control posture, and review endpoint.

2. Context model

The admitted, interpreted, scoped, authority-aware understanding that makes the work safe to attempt.

3. Proof model

The claim/evidence/review structure that makes the result safe to accept or reject.

Everything else is supporting substrate: models, tools, memory, agents, queues, graphs, tests, connectors, UIs.

### The Field Needs A New Definition Of "Ready"

Human software teams have "ready for dev." Agentic engineering needs "ready for delegation."

Ready for delegation means:

- the objective is outcome-shaped
- scope and exclusions are explicit
- source authority is known
- business event or trigger is understood
- assumptions and conflicts are visible
- fit criteria are known
- required evidence is feasible
- control posture is set
- reviewer decision path is clear

Without this, autonomy creates speed without accountability.

### The Field Needs Benchmarks Beyond Task Success

Most agent benchmarks reward final answer correctness or coding task completion. Requirements engineering suggests richer benchmarks:

- Can the agent identify that the user requested a solution before stating the problem?
- Can it extract the real business event from mixed context?
- Can it separate current implementation from desired essence?
- Can it generate alternative candidates and reject the weak ones?
- Can it define fit criteria before acting?
- Can it preserve source authority and unresolved assumptions?
- Can it assemble a review package that a human can judge in five minutes?
- Can it notice when new information invalidates old context?

These are better benchmarks for real work delegation than isolated output quality.

### The Field's Product Doorway

Do not sell this as requirements engineering.

The user-facing promise is:

> Turn messy intent into delegated work you can trust.

The field-level version:

> Agentic engineering is the discipline of making AI work delegatable, inspectable, and acceptable.

## Part Two: How [Squad](https://trysquad.ai) Applies This

### 1. [Squad](https://trysquad.ai) Is Built Around Missions You Can Trust

[Squad](https://trysquad.ai) is organized around missions, not generic chat. That matters because a mission is the smallest unit of delegated work that can hold:

- the desired outcome
- the work boundary
- the context agents are allowed to use
- the fit criteria for success
- the evidence agents must return
- the review decision a human still owns
- the acceptance, correction, or follow-up

The product risk is not choosing the wrong container. The risk is letting agents start before the mission is clear enough to trust. [Squad](https://trysquad.ai) should make the work legible before it makes the work fast.

### 2. Trace Should Be A Reader Surface, Not User Ceremony

The useful idea is not a new requirements object for users to manage. The useful idea is a trace the user can read.

In [Squad](https://trysquad.ai), the trace should be a view across the work:

```text
source
  -> authority
  -> work event
  -> mission boundary
  -> fit criteria
  -> agent work
  -> evidence
  -> review decision
  -> reusable learning
```

Its job is to make lineage inspectable. The user should be able to see why the work started, what counted as good, what evidence came back, and what still needs judgment.

### 3. The Best [Squad](https://trysquad.ai) Translation Is "Trace The Real Work Event Into Proof"

[Squad](https://trysquad.ai) should not make users learn requirements vocabulary.

The public doorway should stay closer to:

> [Squad](https://trysquad.ai) turns messy work context into a mission you can trust agents to execute.

The sharper second sentence is:

> It traces the real work event into proof, so you can see why the work was started, what would count as fit, and whether the result earned trust.

This preserves the deep book insight without making the user learn a requirements vocabulary.

### 4. Context Needs Authority And Viewpoint

Context is not just material pasted into a prompt. In [Squad](https://trysquad.ai), mission context should carry authority, interpretation, uncertainty, and proof expectations.

That means the system should preserve:

- source authority map
- work scope
- business event
- stakeholder or customer segment authority
- current behavior vs desired behavior
- assumptions
- conflicts
- rejected candidates
- fit criteria
- trust requirements

This is not more context. It is better-shaped context.

### 5. [Squad](https://trysquad.ai) Needs Fit Criteria Before Execution

[Squad](https://trysquad.ai) should know what would count as fit before agents start. The mission brief should answer:

- what real event triggered the work?
- what outcome advantage matters?
- what would count as fit?
- what NFRs would make this unacceptable even if functionally done?
- what evidence must exist for review?
- what control posture follows from the risk?

The practical move is not a big form. It is a readiness gate that asks for fit and proof criteria before autonomous execution.

### 6. Proof Is Where The Book Becomes User Relief

[Squad](https://trysquad.ai)'s relief moment is proof review.

The book's traceability, fit criteria, completeness checks, and quality reviews should converge into a compact proof view:

```text
claim
  -> requirement / fit criterion
  -> source/context lineage
  -> task
  -> artifact/receipt/validation
  -> unresolved caveat
  -> reviewer instruction
```

This is the user's relief moment. They should not need to read logs, browse every artifact, or trust a clean summary. They should see what was claimed, why it mattered, what evidence supports it, and where judgment is still required.

### 7. Learning Should Be Proposed, Not Silently Added

The book's learning chapters map directly onto how [Squad](https://trysquad.ai) should handle reusable knowledge.

After a mission, the system can propose durable learning such as:

- this workflow pattern recurs
- this source is authoritative for this domain
- this review criterion matters for this user
- this rejected candidate should not be retried casually
- this term or ontology fragment was stabilized

But those learnings should remain candidates until reviewed. [Squad](https://trysquad.ai) should separate mission context from durable organizational memory.

## Public Product Risks

### Risk 1: Becoming A Requirements Management Product

Wrong move: surface requirements objects everywhere.

Right move: use requirements discipline inside [Squad](https://trysquad.ai) to make missions easier to trust.

### Risk 2: Context Worship

Wrong move: make the context graph the product.

Right move: use the graph to make mission readiness and proof review inspectable.

### Risk 3: User Burden

Wrong move: ask the user to fill out Volere-style fields.

Right move: have agents trawl, propose, and compress; ask the user only for high-leverage corrections and approvals.

### Risk 4: False Certainty

Wrong move: let agents generate fit criteria, satisfy them, and approve the result in one closed loop.

Right move: preserve source lineage, unresolved issues, and human review gates.

### Risk 5: Trying To Prove The Whole System At Once

Wrong move: implement the whole knowledge model.

Right move: start with fit criteria and claim-to-evidence trace inside one mission/proof path.

## The Practical [Squad](https://trysquad.ai) Pattern

The practical pattern is:

1. Ask for fit criteria before execution.
2. Preserve the source and authority behind each mission.
3. Map proof claims to fit criteria and evidence.
4. Show a compact review surface that explains why the work was in scope, what counted as fit, and what evidence supports the claim.

## Final Compression

For agentic engineering:

> Requirements engineering becomes powerful again because agents can carry its discipline without human ceremony fatigue.

For [Squad](https://trysquad.ai):

> Do not sell requirements. Compile requirements discipline into mission readiness, proof review, and memory-safe learning.

The five-minute user sentence should be:

> "It knew what had to be true before it started, and now I can review the result without reading the whole agent history."

## Addendum: The Memo Through Examples

This addendum restates the memo in examples. The point is not to add a second theory. It is to show what the theory changes in actual agentic engineering work.

### Example 1: One User Request Is Secretly Multiple Requirements

User request:

> "Let users connect Slack from inside [Squad](https://trysquad.ai)."

Weak agent interpretation:

> "Make sure the backend can generate a Slack auth link."

That may be useful, but it is only one requirement. The user-facing request actually contains several different claims:

| Requirement | Requirement type | Fit criterion | Valid proof | Forbidden substitution |
| --- | --- | --- | --- | --- |
| Backend can create a managed auth link | backend/tool-call | API returns a valid provider auth URL for the right workspace/user context | backend receipt, API test, provider response | none; this only proves the backend claim |
| User can start connection from the app | user journey | user clicks Connect in the visible app surface and gets the auth handoff | browser/app click-path proof | direct backend call, terminal command, copied URL |
| App reflects connected state after auth | durable UI/state | returning to [Squad](https://trysquad.ai) refreshes readiness and shows connected state | app state readback, UI proof, persistence receipt | screenshot before refresh, stale local state |
| Agent can use Slack after user grants access | tool permission/runtime | tool invocation succeeds under the connected user/workspace boundary | tool-call receipt with connection id/workspace | auth success alone |

Requirements engineering prevents the agent from accepting the first row as proof of all four rows.

Agentic lesson:

> Different proof surfaces mean different requirements.

### Example 2: Context Engineering Is Trawling, Not Retrieval

Mission:

> "Make onboarding less confusing."

Weak context engineering:

> Retrieve onboarding docs, recent tickets, screenshots, and paste them into the prompt.

Requirements trawling version:

| Trawling question | Example answer |
| --- | --- |
| What event causes the pain? | A user returns after auth and cannot tell whether setup completed. |
| Who experiences it? | First-time workspace owner, not the backend operator. |
| What source has authority? | Live app path, user annotation, current product behavior, current auth receipt. |
| What is current implementation? | The app redirects to Settings and shows source-readiness state. |
| What is desired essence? | The user knows what is connected and what can be used next. |
| What assumption must be falsified? | "Settings readiness equals connector readiness." |
| What would count as fit? | User can complete the path without leaving the app context or asking what happened. |

Retrieval finds related material. Trawling decides what the material means, what authority it has, and what must be proven before action.

Agentic lesson:

> Context is not the pile of facts. Context is the admitted, interpreted, authority-ranked basis for work.

### Example 3: Business Events Beat Feature Lists

Feature-list decomposition:

```text
- add connector menu
- add settings row
- add auth callback
- add readiness badge
- add tests
```

Business-event decomposition:

```text
Event: user decides to connect Slack during work.
Required response: the app offers a visible Connect action in the current work context.
Proof: click Connect from the app surface and receive auth handoff.

Event: user returns after Slack auth.
Required response: the app reconciles connection state and shows what changed.
Proof: app readback shows connected state tied to the right workspace.

Event: agent tries to use Slack in a mission.
Required response: the app checks permission and either uses Slack or asks for approval/connection.
Proof: tool receipt or approval-required receipt.
```

The feature list tells agents what files might change. The business events tell agents what real-world moments must work.

Agentic lesson:

> Decompose by the outside event the system must respond to, not by the component that looks easiest to edit.

### Example 4: Brown Cow Thinking Prevents Automating The Current Mess

Problem:

> "The Settings connector flow is confusing."

Without Brown Cow thinking, an agent may polish the current Settings UI and preserve the wrong model.

| View | Connector example |
| --- | --- |
| Current implementation | The composer redirects to Settings; Settings uses old readiness commands. |
| Current essence | User needs to authorize an external tool before the agent can use it. |
| Desired essence | User understands which capability is needed, grants it, and sees the mission can proceed. |
| Future implementation | The in-app connector action, Settings row, auth callback, and tool runtime share one connection lifecycle. |

The future implementation may still include Settings, but Settings is no longer mistaken for the requirement.

Agentic lesson:

> Do not let the current UI route define the real requirement.

### Example 5: Fit Criteria Are Evals

Vague requirement:

> "Make human review easier."

Fit-criteria version:

| Requirement | Fit criterion | Eval/proof |
| --- | --- | --- |
| Reviewer sees the claim being made | Every proof package has one top-level claim sentence | static proof-package check |
| Reviewer sees why the work was in scope | Claim links to source/context/mission definition | trace receipt |
| Reviewer sees what evidence supports it | Each claim maps to test, browser proof, DB proof, or explicit human judgment | proof matrix check |
| Reviewer is not asked to redo machine work | Human checklist excludes lint/type/test/browser checks that agents can run | checklist audit |
| Reviewer can decide in five minutes | Packet has claim, evidence, caveat, and decision button without reading raw logs | human QA timing / product review |

This converts "easier" from taste into acceptance.

Agentic lesson:

> A fit criterion is an eval with a human-readable reason for existing.

### Example 6: Non-Functional Requirements Are Trust Requirements

Functional requirement:

> "The agent can post a Slack update."

Trust requirements:

| Trust requirement | Why it matters | Proof |
| --- | --- | --- |
| Consent | Posting externally affects other people. | approval/permission receipt |
| Auditability | User may need to know what was sent and why. | message link, trace, source claim |
| Privacy | Context may include information not meant for Slack. | redaction/policy check |
| Recovery | Bad message may need correction. | edit/delete capability or fallback note |
| Tone | The message represents the operator. | human-review packet if tone is judgment-heavy |

The Slack post can technically succeed and still be unacceptable if these trust requirements fail.

Agentic lesson:

> For agents, NFRs are not polish. They are conditions of delegation.

### Example 7: Requirements Trace Becomes Staleness Detection

Generated work without trace:

```text
Agent changed checkout flow.
Tests passed.
```

Generated work with trace:

```text
Requirement: pricing checkout supports annual discount.
Source: pricing memo and issue tracker ticket.
Assumption: annual discount is 20 percent.
Code: checkout-pricing.ts, pricing-summary.vue.
Proof: unit test, browser checkout proof, receipt.
Stale if: pricing memo changes, discount policy changes, checkout contract changes.
```

When pricing changes, [Squad](https://trysquad.ai) can say:

> These two files and one proof claim are stale. The rest of the mission is unaffected.

Without the trace, everything is maybe stale, which means nothing is practically actionable.

Agentic lesson:

> Bounded context is what makes later invalidation useful.

### Example 8: AI-Generated Requirements Are Drafts, Not Authority

Agent says:

> "The requirement is to add OAuth support to Settings."

Better workflow:

```text
Candidate requirement from agent:
Users can connect Slack from Settings.

Source check:
User correction says real users use the in-app connector flow.

Revised admitted requirement:
Users can start and complete Slack connection through the in-app connector flow, with Settings as a secondary management surface.

Decision owner:
Product owner owns the user-facing path.

Proof:
Browser walkthrough of the in-app connector flow plus backend connection receipt.
```

The agent is allowed to propose. It is not allowed to make its own proposal the authority it then proves.

Agentic lesson:

> Agents can generate requirements, but only provenance and review can admit them into truth.

### Example 9: Ready For Delegation Is Not Ready For Dev

Old ready-for-dev packet:

```text
Ticket: Fix connector flow.
Acceptance: Slack connects.
```

Ready-for-delegation packet:

```text
Objective:
Users can connect Slack from the app path they naturally use.

Scope:
Composer connector action, Settings connector action, auth handoff, readiness refresh.

Non-goals:
Do not redesign all provider settings. Do not add new provider types.

Source authority:
Product correction, visible app flow, connector provider contract, Settings readiness code.

Business event:
User tries to use Slack capability during a mission and is not connected.

Assumptions to falsify:
Settings readiness command can represent managed auth state.
Composer path can reuse Settings setup command.

Fit criteria:
Click Connect from app surface, complete auth, return, see connected state, run Slack tool.

Proof:
App journey proof, backend receipt, tool receipt.

Human judgment:
Does the flow feel like it belongs in [Squad](https://trysquad.ai) rather than like an external side channel?
```

This is longer, but it saves the agent from proving the wrong thing at speed.

Agentic lesson:

> Ready for delegation means the agent knows what it is allowed to prove.

### Example 10: The Proof Package Is The User Relief

Bad closeout:

> "Implemented Slack connector support. Tests pass."

Better closeout:

```text
Claim:
Users can connect Slack from the in-app connector flow.

Requirement:
REQ-SLACK-IN-APP-CONNECTOR-FLOW.

Source:
Product correction and visible connector menu.

Fit criterion:
User starts from app, completes auth, returns, sees connected state, and can use Slack.

Evidence:
App path receipt, backend connection receipt, Slack tool invocation receipt.

Caveat:
Workspace picker edge case still needs human review.

Human decision:
Confirm whether the auth handoff feels like a [Squad](https://trysquad.ai)-owned flow.
```

The review burden changes. The user is not asked to infer what happened from a diff, transcript, or confident summary. The work arrives with its claim, lineage, evidence, and remaining judgment call.

Agentic lesson:

> The product is not "agents did work." The product is "the user can accept or reject delegated work without reconstructing it."

### Example 11: The Same Pattern In A Financial Advice Product

User-visible claim:

> "You can save $2,100 by changing retirement contributions."

Requirements split:

| Requirement | Proof |
| --- | --- |
| Income was extracted correctly | source document extraction receipt |
| Current contribution rate is known | payroll/source fact |
| Tax assumption is explicit | assumption set |
| Calculation is correct | deterministic calculator run |
| Advice boundary is safe | policy check |
| User-visible explanation matches math | grounding/math consistency eval |
| Human expert review is needed or not | review routing rule |

An LLM can explain the recommendation. It cannot be the source of financial truth.

Agentic lesson:

> Same architecture, different validator: financial truth replaces product-flow truth.

### Example 12: What [Squad](https://trysquad.ai) Should Actually Sell

Operating discipline:

```text
requirements trawling
source authority
fit criteria
proof matrix
traceability
human judgment routing
```

User-facing doorway:

> "[Squad](https://trysquad.ai) turns messy work into missions your agents can execute and you can actually trust."

Five-minute user moment:

> "I can see what had to be true, what the agents proved, and what still needs my judgment."

That is the book expressed as product relief.
