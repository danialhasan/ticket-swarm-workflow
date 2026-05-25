---
name: mission-review-loop
description: Use when a completed or terminated mission enters human review and Squad must verify mission and task outcomes, surface evidence, collect feedback, and preserve learning without treating human attention as missing machine proof.
---

# Mission Review Loop

## Goal

Help the human decide whether the mission delivered the required outcome while
Squad handles all machine-verifiable review work first.

The user-facing relief is:

```text
Squad shows me the outcome, the proof, and the few decisions that actually need
my judgment.
```

Mission Review is a chat collaboration, not a Mission Overview mode. Mission
Overview can launch review and display mission readback, but the back-and-forth
review process happens in a new mission-scoped Chat with this skill loaded.

## Use This Skill When

- A completed, blocked, or terminated mission exposes `Review mission`.
- Chat checks mission status and finds a completed or review-ready mission.
- The user opens Mission Review from Mission Control, from the Chat side rail
  above conversations, or from Chat after the agent checks mission status.
- Feedback from review should update future mission memory or trigger follow-up
  work outside mission runtime.

## Do Not Use This Skill When

- The mission is still defining; use `mission-definition-conveyor`.
- A task is actively running; use `mission-task-operation`.
- The user only wants status without a review decision; use
  `mission-overview-readmodel`.

## Required Inputs

- Mission operating context and final mission readback.
- Mission requirements, acceptance criteria, task DAG, authority, proof package,
  receipts, artifacts, and review surface.
- Task final artifacts.
- Frontend media, backend endpoint proofs, devops deployment proofs, and
  telemetry/runtime-proof receipts as required by task type.
- Human decision question and feedback capture target.

## Review Procedure

1. From Mission Control, Chat side rail, or Chat status output, route the user
   to the Mission Overview route for the selected mission.
2. From Mission Overview, the `Review` button opens a new chat conversation
   scoped to mission review and loads this skill.
3. Load mission overview and proof/readiness readback into Chat.
4. Review the mission layer: outcome, requirements, acceptance, authority,
   task DAG, proof package, and open `HOLD`s.
5. Review every task layer:
   - backend: hit endpoints or replay tests where safe;
   - frontend: display screenshots/videos and verify user flows;
   - devops: verify health, hashes, release/feed posture, and frontend impact.
6. Use generated UI for mission cards and task cards when it helps the human
   inspect outcomes, proof media, and task artifacts in the conversation.
7. Run autonomous checks before asking the human to judge.
8. Surface only irreducible human attention:
   - whether the delivered outcome is acceptable;
   - whether UX/copy/behavior feels right;
   - whether a risk or deferral is acceptable.
9. Capture feedback and memory updates for future missions.
10. If changes are needed, collaborate in chat directly. Do not reopen the
   terminated mission runtime unless a new mission is explicitly created.

## Proof Rules

- Backend endpoint proof does not prove frontend outcome.
- Frontend media does not prove durable state.
- Deployment health does not prove product behavior.
- A proof package summary does not prove each task receipt.
- Human approval does not replace missing machine proof.

## Output

Return a mission review packet with:

- mission outcome verdict;
- requirement-by-requirement status;
- task verdicts and receipt refs;
- mission card/task card generated UI refs when used;
- proof surfaces satisfied;
- machine-verifiable gaps;
- human judgment decisions;
- feedback captured for memory;
- recommended follow-up path: accept, changes in chat, new mission, or blocker.

## Stop Condition

Hold review when:

- proof package is missing for a claim that requires it;
- task final artifacts are absent;
- required frontend media is missing;
- runtime-proof telemetry cannot distinguish happy and negative paths;
- the human would need to reconstruct context the agent should have gathered.
- review is being kept inside Mission Overview instead of being launched into
  mission-scoped Chat.

## Receipt

Receipt must include:

- mission refs and review surface refs;
- task final artifact refs;
- proof queries and media paths;
- human decision packet;
- memory update or explicit non-update;
- remaining `HOLD`s and non-claims.
