---
name: beta-release-assist
description: "Use when a merged Squad slice is ready for delivery work and we need the post-merge beta release workflow: deploy-readiness verification, artifact and manifest checks, updater feed verification, release-note assembly, human-triggered release handoff, and rollback or re-release receipts."
---

# Beta Release Assist

Use this skill for **post-merge delivery work**, not for implementing product tickets.

This skill owns the release-assist loop for the first external beta:

- verify deploy readiness
- verify artifacts and manifests
- verify updater feed health
- prepare release notes and operator handoff
- support human-triggered beta release
- record rollback or re-release posture

Do not use this skill for:

- ordinary product ticket implementation
- canon changes unrelated to delivery
- automatic beta exposure

## Inputs to gather first

- target version or release tag
- merged commit SHA
- release channel
- deploy-readiness report
- deploy-seam truth verdict
- CI result
- required test result
- human review receipt
- artifact locations
- updater feed URL and verification endpoints
- human release decision owner
- explicit human deploy intent

Start by reading:

- `/Users/danialhasan/dev/squad/canon/21-cicd-and-delivery-model.md`
- `/Users/danialhasan/dev/squad/docs/canon-proposals/section-21-delivery-autoupdate-v1-lock.md`
- `/Users/danialhasan/dev/squad/docs/execution-system/delivery-autoupdate-lowering.md`
- `/Users/danialhasan/dev/squad/docs/execution-system/manifests/delivery-ticket-manifest.json`

Read these references from this skill when needed:

- `references/release-receipt-checklist.md` for required release receipts
- `references/v1-delivery-source-map.md` for old-repo salvage context and behavior to preserve
- `../ticket-day-operator/references/deploy-truth-and-cadence.md` when the actual deploy entrypoint,
  cadence, or fallback posture is unclear

## Workflow

### 1. Confirm release scope

- identify the merged slice or slices included in the release
- identify the exact version or tag being exposed
- confirm whether this is initial beta exposure, re-release, or rollback follow-up

Stop if:

- the work has not been merged
- CI has not passed
- required tests have not passed
- human review receipt is missing
- required verification is still missing
- the human release owner is not identified
- there is no explicit human intent to deploy this version
- the release path being promised is not supported by repo reality

### 2. Build deploy-readiness packet

Assemble one deploy-readiness packet with:

- merged commit
- deploy-seam truth verdict: `ready`, `partial`, `missing`, or `conflicted`
- CI status
- verification status
- required test status
- human review status
- artifact status
- updater feed status
- human-trigger eligibility

This packet is the core handoff object for the human release decision.

### 3. Verify artifacts and manifests

Check:

- packaged artifacts exist
- manifests exist
- package URLs and manifest URLs resolve correctly
- checksums or signatures are present where required
- release publication state is consistent with the version being exposed

Do not treat “build succeeded” as enough.

### 4. Verify updater feed health

Check the updater feed independently of the packaged app:

- manifest reachability
- package reachability
- cache-bust behavior
- current version correctness

If the feed is wrong, the release is not ready even if artifacts exist.

### 5. Verify in-app updater posture

Confirm the updater runtime contract remains honest:

- checking
- available
- not available
- progress
- downloaded
- apply recovery needed
- error

This can be proven through runtime receipts, smoke checks, or operator-facing checks depending on
the ticket set already landed.

### 6. Prepare human-trigger handoff

Assemble the human-trigger packet with:

- version/tag
- merged commit
- included slices
- canon alignment summary
- product-surface change summary
- deploy-readiness result
- updater verification result
- telemetry expectation summary
- release notes summary
- rollback or re-release posture

The human still chooses exposure. This skill prepares that decision; it does not take it.

### 7. Record release outcome

After the human-triggered action:

- record whether release happened
- record which version was exposed
- record which updater endpoint was verified
- record rollback or rerun posture

If release is blocked, record the blocker explicitly instead of hand-waving “not ready.”

## Verification posture

This skill is delivery-focused, so it should explicitly consider:

- artifact verification
- feed verification
- smoke where it protects updater behavior
- runtime telemetry and release receipts
- the canonical predeploy gate from Section `21`

It should not invent new bureaucracy or second-guess product truth already verified elsewhere.

## Required outputs

Every run should leave behind:

- deploy-readiness packet
- artifact verification note
- updater feed verification note
- release handoff note
- release decision receipt

If any of those are missing, the release-assist pass is incomplete.

## Close rule

The release-assist loop is complete only when:

- readiness is explicit
- the human trigger boundary is preserved
- updater/feed behavior is proven
- release or non-release outcome is receipt-backed
