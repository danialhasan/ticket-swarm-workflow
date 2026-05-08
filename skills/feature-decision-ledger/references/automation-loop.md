# Automation Loop

Use this reference when composing the ledger skill into an automation.

## Good cadences

- nightly when Slack and Linear move quickly
- weekly when roadmap churn is lower

## Automation loop

1. read the current ledger
2. gather new Slack, meeting, and Linear inputs since the last pass
3. normalize ideas into candidate rows
4. dedupe against canon cuts, holding epics, and current ledger rows
5. update only the rows whose source truth changed
6. emit a short delta summary

## Output expectations

Every automation run should emit:

- current beta thesis
- explicit beta non-goals
- parking-lot features
- kill-list candidates
- discussed-but-undecided gaps
- what changed since the last run

## Guardrails

- do not rewrite the whole ledger when only one row changed
- do not create duplicate parking-lot rows for the same feature family
- do not infer a product decision from vague discussion
- escalate conflicts between canon and recent discussion instead of auto-resolving them
