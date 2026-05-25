---
name: annotation-reconciliation-guard
description: Use when Danial's live product annotations must become hard reconciliation rows before a goal loop, ticket swarm, or QA pass may claim readiness.
---

# Annotation Reconciliation Guard

For ambiguous Ticket Swarm requests, use `$ticket-swarm-router` first. Activate
this skill only when human annotations are the blocker that must be reconciled
before readiness claims.

Use this skill when a mission depends on Danial's Browser comments, product
annotations, design-review notes, or other human product judgment.

This is a scope-control skill. It prevents a later implementation pass from
quietly converting human feedback into softer labels like `outside golden path`,
`owned by contract`, or `broader scope`.

For the compact skill contract shared across this plugin, see
[../references/outcome-first-skill-contract.md](../references/outcome-first-skill-contract.md).

## Goal

Turn every human annotation into a tracked reconciliation row:

```text
annotation
  -> route/surface
  -> expected product behavior
  -> observed issue
  -> owner rail
  -> required proof
  -> final disposition
  -> evidence
```

The goal is complete only when every row has one of these final dispositions:

- `implemented-and-proven`
- `blocked-human`
- `blocked-technical`
- `explicitly-deferred-by-Danial`
- `not-dogfood-blocking-with-evidence`

## Forbidden Final Dispositions

These may appear as intermediate notes, but never as final status:

- `owned-by-contract`
- `outside-golden-path`
- `broader-scope`
- `partial`
- `unknown`
- `risk`
- `already-has-receipt`

## Special Rule: Should Not Exist

If Danial says a route, card, component, or surface should not exist, the row can
close only by one of:

- removal
- redirect
- proof the dogfood user cannot access it
- explicit Danial-approved deferral

Copy cleanup, visual polish, or a narrower golden-path proof does not satisfy a
`should not exist` annotation.

## Required Ledger

Create or update:

`docs/operations/sessions/<YYYY-MM-DD>/annotation-reconciliation/<slug>.md`

Each row must include:

- annotation id
- route/surface
- expectation
- observed issue
- owner rail or `SQD-*`
- current status
- required proof
- final disposition
- evidence link
- whether Danial approval is required

## Workflow

1. Extract every annotation from the source receipt or browser comments.
2. Group rows by route/surface only after each row has a stable id.
3. Mark visible dogfood routes as blocking unless fixed, hidden, inaccessible, or
   explicitly deferred by Danial.
4. Route each row to hotfix, implementation contract, QA rerun, human blocker,
   technical blocker, or explicit deferral.
5. Refuse readiness claims while any row is unresolved or silently downgraded.

## Close Rule

The guard is complete when the annotation ledger can answer:

- what was fixed
- what proof exists
- what remains blocked
- what Danial explicitly deferred
- what is genuinely not dogfood-blocking and why

If the ledger cannot answer that, the goal loop is not allowed to claim
readiness.
