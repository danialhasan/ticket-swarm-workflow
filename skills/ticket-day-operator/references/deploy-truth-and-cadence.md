# Deploy Truth And Cadence

Use this reference before promising any deploy rhythm.

## Deploy-seam truth detection

Inspect repo reality and classify the deploy seam:

- `ready`: one explicit primary path exists and the repo, docs, and env surfaces agree
- `partial`: some path exists, but entrypoints, scripts, or env requirements are incomplete
- `missing`: no real deploy entrypoint can be proven
- `conflicted`: multiple paths disagree or the docs point to missing code

## Minimum evidence

Check:

- deploy script or package command exists
- release or deploy docs point to real files
- required environment surface is explicit
- artifact or publish path is explicit
- primary versus fallback path is not ambiguous

## Cadence policy

Default project cadence:

- local proof per ticket
- first integration deploy after one vertical seam is real
- final deploy at the gate boundary or end-of-day proof point
- beta exposure remains human-triggered

Ask the reader's agent to replace this default with the host product's release
cadence, human approval boundary, deploy frequency, and proof gates before
promising a rhythm.

Do not promise deploy-after-each-ticket unless:

- the seam is `ready`
- the packaging cost is low enough
- the human/operator burden is acceptable
