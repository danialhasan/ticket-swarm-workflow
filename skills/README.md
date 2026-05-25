# Runtime Skills

This directory intentionally stays flat because Codex plugin discovery loads
skills from `skills/<skill-name>/SKILL.md`.

Use `../skill-groups/` for high-level function segmentation. Do not infer that
every top-level directory here is a runtime skill; a directory is an active
skill only when it contains `SKILL.md`.

Current active runtime skills:

- `annotation-reconciliation-guard`
- `beta-release-assist`
- `calendar-dag-scheduler`
- `day-state-updater`
- `design-contract-conveyor`
- `feature-decision-ledger`
- `goal-loop-operator`
- `implementation-contract-conveyor`
- `linear-day-allocator`
- `mission-context-discovery`
- `mission-definition-conveyor`
- `mission-overview-readmodel`
- `mission-review-loop`
- `mission-task-operation`
- `parallel-lane-orchestrator`
- `review-batch-orchestrator`
- `sequential-ticket-review-queue`
- `squad-harness-engineering`
- `ticket-day-operator`
- `ticket-human-review-runtime`
- `ticket-swarm-router`
- `ticket-to-human-review`
- `ui-abstraction-guard`
- `worktree-lane-orchestrator`
- `worktree-lane-reconcile`

Shared applied-AI/context-engineering doctrine:

- `squad-harness-engineering/references/bitter-lesson-applied-ai-context-engineering-doctrine.md`

Future Codex sessions should read that reference before optimizer,
hillclimbing, context-composition, reward-signal, semantic-judge, or
no-promotion/promotion planning work. It defines the search-and-selection model,
the harness/optimizer/product-runtime role split, the deterministic versus
semantic scorer boundary, product-intent inference expectations, compute policy,
and ref attachment rules.

Non-runtime support/stub directories currently present:

- `references`
- `setup-ticket-swarm-workflow`
- `ui-annotation-conveyor`
