# Hourly Kill Plan

Use this reference to turn a board target into one honest day packet.

## Required inputs

- current local time
- free windows for the rest of the day
- board target for the day
- current close count
- ordered candidate list

## Candidate ordering

Default order:

1. `In Progress` child issues with bounded remaining proof
2. ready-now `Todo` child issues with no open blockers
3. newly unlocked child issues with low remaining work
4. blocker-breaking tickets only when the first three buckets do not cover the target

## Per-block structure

Every plan should include:

- one opening block to lock the active list
- one midday seam-proof checkpoint
- one late-day replan checkpoint
- one final closeout block

## Throughput honesty

When the target is aggressive, report:

- `floor`: what should close with normal execution
- `base case`: what closes if the active set behaves
- `stretch`: what closes only if unlocked follow-ons stay cheap

Do not blur:

- real `Done` closes
- softer state movements
- parent-issue motion

Only the first category should count toward a strict "close N tickets today" promise unless the
operator explicitly says otherwise.
