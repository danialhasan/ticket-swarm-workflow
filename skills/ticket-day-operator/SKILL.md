---
name: ticket-day-operator
description: Use when a Squad execution day has real board pressure, calendar constraints, or schedule-slip correction and we need a calendar-aware close plan before ticket execution starts.
---

# Ticket Day Operator

Use this skill when the question is:

- what do we close today
- how do we fit that into the real calendar
- what should count as a close
- when does deploy happen
- how does a slipped start date change today's target

This skill does not replace release-thesis shaping or per-ticket execution. It sits between slice
selection and the ticket loop.

Do not use this skill when:

- no time-bound target exists
- the work is still too broad to name a concrete close list
- the board data is too stale to support an hourly plan

## Inputs to gather first

- local date and timezone
- today's board target
- current board counts:
  - Done child issues
  - In Progress child issues
  - In Review child issues
  - ready-now Todo child issues
  - dependency-blocked child issues
- candidate tickets with identifiers, parents, blockers, and likely close effort
- today's `calendar_provider` events and free windows
- repo path and current branch
- desired deploy boundary or gate
- any shifted schedule assumption such as "started one business day late"

Start by reading:

- `references/hourly-kill-plan.md`
- `references/shifted-schedule-math.md`
- `references/deploy-truth-and-cadence.md`
- `../ticket-to-human-review/SKILL.md`
- `../beta-release-assist/SKILL.md` when release work may happen today

## Goal

Produce one execution-day packet with:

- free windows and hard blocks
- hourly close targets
- ordered close list
- shifted schedule target and next gate
- deploy-seam verdict
- deploy cadence for the day
- assumptions and stretch rules

## Workflow

### 1. Read calendar truth first

Use the configured `calendar_provider` adapter.

Required reads:

- current local date/time
- remaining timed events for the day
- free windows for the same interval

Rules:

- do not plan over real meetings, travel, or hard offline windows
- plan against free windows, not against an imaginary 16-hour day
- convert free windows into explicit work blocks before touching the board

### 2. Rebase schedule truth when the start date moved

If the schedule slipped by one or more business days, rebase the baseline before classifying
Ahead/On/Behind.

Required outputs:

- previous business-day close target
- today's close target
- next gate date and name
- exact amount ahead or behind

Always report absolute dates.
Never rely on floating phrases like "today" or "tomorrow" when a correction is being made.

### 3. Enter throughput mode

Default close order:

1. child issues already `In Progress`
2. ready-now child issues in `Todo`
3. cheap unlocked follow-ons
4. blocker-breaking work only if the first three buckets are insufficient

Rules:

- do not count parent issues as closes
- separate "real Done closes" from softer state movements
- prefer tickets with low remaining work and high unlock value
- if a ticket needs deep discovery, it is probably not today's close candidate

### 4. Build the hourly kill plan

Use the free windows and the ordered close list to build one hourly packet.

Required structure:

- first block locks the kill list and active ownership
- at least one midday integration or seam-proof checkpoint
- at least one late-day replan checkpoint
- final block for closeout, receipts, and deploy decision

Rules:

- size goals per free block, not by naive equal-hour math
- if a close target is aggressive, explicitly label:
  - floor
  - base case
  - stretch
- if the target assumes state movements rather than all-net-new completions, say so plainly

### 5. Detect deploy-seam truth before promising cadence

Inspect repo reality before saying anything like "we can deploy after each ticket" or "we'll deploy
midday."

Check:

- whether a deploy entrypoint actually exists in the repo
- whether package scripts and docs agree
- whether release docs name a real primary path and real fallback path
- whether required environment and artifact surfaces are explicit

Classify the deploy seam as one of:

- `ready`
- `partial`
- `missing`
- `conflicted`

If the seam is not `ready`, do not promise a cadence the repo cannot support.

### 6. Apply deploy cadence policy

Default policy:

- local proof per ticket
- first integration deploy only once one vertical seam is real and repo truth supports it
- final deploy at the gate boundary or end-of-day integrated proof point
- no automatic beta exposure

Do not model deploy-after-each-ticket unless repo reality, packaging time, and operator cost all
support it.

### 7. Emit the execution-day packet

Every run should leave behind:

- free-window summary
- hourly kill plan
- ordered close list
- deploy-seam verdict
- deploy cadence for the day
- shifted target math when applicable
- assumptions and explicit risk

## Close rule

This skill is complete only when:

- the calendar has been read
- the board target has been rebased if needed
- the close list is ordered
- the deploy cadence matches repo reality
- the hourly plan is concrete enough for the next ticket loop to execute without improvising the day
