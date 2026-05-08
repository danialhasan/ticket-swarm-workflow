---
name: feature-decision-ledger
description: Use when feature ideas are scattered across Slack, meetings, and Linear and we need one durable ledger for beta thesis, explicit non-goals, parking-lot features, kill-list candidates, and undecided gaps.
---

# Feature Decision Ledger

Use this skill when the problem is not "build the next ticket" but "remember what we already
discussed and stop beta scope from drifting."

This skill maintains one durable compiled surface:

- `/Users/danialhasan/dev/squad/docs/operations/feature-decision-ledger.md`

It does not replace canon or Linear.
It compiles them into one operator-facing decision ledger.

## Use when

- feature ideas are spread across Slack, meetings, and Linear
- someone is building a kill list or beta non-goal list
- the team keeps revisiting old ideas without knowing what was already parked
- roadmap discussion is outrunning product-memory hygiene
- you want a nightly or weekly automation to keep feature memory fresh

Do not use when:

- the question is one narrow ticket implementation
- the thesis itself is still blurry enough that every idea feels equally important
- there is no source material to compile yet

## Inputs to gather first

- current beta thesis
- canon cuts and explicit non-goals
- live Linear project and holding-epic data
- Slack threads, meeting notes, docs, or transcripts that mention feature ideas
- current ledger file, if it exists
- known human decisions that overruled older ideas

Start by reading:

- `/Users/danialhasan/dev/squad/docs/operations/feature-decision-ledger.md`
- `/Users/danialhasan/dev/squad/canon/22-initial-slice-v1-scope.md`
- `references/ledger-categories.md`
- `references/source-priority.md`
- `references/automation-loop.md`

When the source set is live:

- use Composio Slack for Slack messages, threads, and canvases
- use Composio Linear for project issues, comments, and holding epics
- use calendar or meeting notes only when they actually contain feature ideas or scope decisions

## Goal

Maintain one decisioning surface that continuously emits:

- current beta thesis
- explicit beta non-goals
- parking-lot features
- kill-list candidates
- "this was discussed but never decided" gaps

## Workflow

### 1. Freeze the current beta thesis

Start from canon and the current human release posture, not from the latest brainstorm.

The ledger must always begin with:

- current beta thesis sentence
- exact in-scope story being protected
- source of truth for that thesis

If the thesis changed, record who changed it and what older thesis was replaced.

### 2. Gather source material

Collect candidate ideas from:

- Slack
- meeting notes or transcripts
- Linear issues, comments, and holding epics
- existing ledger rows

Do not treat every mention as a feature.
Normalize each candidate into one row with:

- feature or idea name
- source link or source ref
- date seen
- why it came up
- any user pain or evidence attached to it

### 3. Dedupe against canon cuts and holding epics

Before adding a new row, check whether the idea is already:

- explicitly cut from the current beta in canon
- already parked in a holding epic
- already present in the ledger under a different label
- already resolved by a later human decision

Do not create duplicate parking-lot entries for the same idea family.

### 4. Classify every candidate

Every candidate must end in one of the ledger buckets from `references/ledger-categories.md`.

Required buckets:

- current beta thesis
- explicit beta non-goal
- parking-lot feature
- kill-list candidate
- discussed but undecided

If the classification is ambiguous, prefer `discussed but undecided` over quietly promoting the
idea into scope.

### 5. Write the durable ledger

Update `/Users/danialhasan/dev/squad/docs/operations/feature-decision-ledger.md`.

Rules:

- preserve explicit decisions until a later explicit decision replaces them
- keep rows short and source-backed
- include the dedupe target when an idea maps to an existing holding epic
- do not bury new uncertainty inside prose; put it in the undecided section

### 6. Emit the operator summary

Every run should summarize:

- what changed since the last pass
- any new explicit non-goals
- any new parking-lot features
- any new kill-list candidates
- any unresolved gaps that now block roadmap or beta decisions

## Automation posture

This skill is safe to compose into a nightly or weekly automation.

Automation-friendly rules:

- read the current ledger first
- only rewrite rows whose source truth actually changed
- prefer additive deltas over large rewrites
- escalate conflicts between Slack, Linear, and canon instead of guessing
- if there is no real change, emit a concise delta note instead of churn

## Close rule

This skill is complete only when:

- the beta thesis is explicit
- canon cuts and holding epics were checked for dedupe
- the durable ledger file was updated or explicitly left unchanged
- new uncertainty is visible in the undecided bucket instead of hiding in discussion memory
