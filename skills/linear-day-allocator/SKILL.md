---
name: linear-day-allocator
description: Use when a daily execution plan needs to become real Linear ownership, due-date, and state-allocation truth for dependency-ready child issues.
---

# Linear Day Allocator

Use this skill when the question is:

- which tickets are officially in scope for today
- which child issues should be due today
- who should own each selected ticket
- how do we reflect today's calendar-backed plan into Linear

This skill applies the day plan to Linear.
It should usually run after `calendar-dag-scheduler`.

## Inputs to gather first

- active Linear project
- today's selected ticket list
- parent/child relationship data
- dependency graph
- current issue states
- current assignees
- local date and timezone
- any policy for assignment fallback

Start by reading:

- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/calendar-dag-scheduler/SKILL.md`
- `/Users/danialhasan/dev/squad/plugins/ticket-swarm-workflow/skills/ticket-day-operator/SKILL.md`

Use Linear through Composio.

## Goal

Turn a schedule-backed close plan into honest Linear truth:

- selected child tickets are due today
- parent issues remain excluded
- current ownership is preserved when already explicit
- unassigned selected work gets a real owner

## Workflow

### 1. Validate scope

- confirm the target project
- confirm selected issues are child issues
- confirm they are dependency-ready or intentionally chosen grouped review blocks

Rules:

- never set parent issues due just to satisfy a board target
- never pull clearly blocked tickets into today's due-date set unless they are explicit blocker-clearing work

### 2. Apply due-date policy

For every selected child issue:

- set due date to the local current date
- treat that as `due by 11:59 PM local time`

Rules:

- use one consistent local date across the day's run
- do not silently leave a selected issue without a due date

### 3. Apply assignment policy

- preserve an existing assignee by default
- if no assignee exists, assign the configured owner for today
- if the issue is part of a parallel wave, ensure each ticket has one explicit owner

Rules:

- do not thrash assignees on already-owned work unless the operator explicitly asked for reassignment
- if ownership is ambiguous, surface it instead of guessing across multiple people

### 4. Reflect execution-wave metadata when helpful

Optional but preferred:

- add a brief comment or label convention that ties the ticket to today's wave
- note whether the ticket belongs to execution, grouped review, or patch follow-through

Rules:

- keep comments short and operational
- do not spam unchanged tickets

## Close rule

This skill is complete only when:

- parent issues were excluded
- selected child issues were updated for today
- ownership is explicit for today's selected work
- any ambiguity or auth blocker is surfaced honestly
