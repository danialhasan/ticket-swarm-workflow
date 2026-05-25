# 30 Day Planning And Allocation

Use these skills when the question is about today's execution shape, calendar
truth, dependency pressure, and real ownership allocation.

Skills:

- `ticket-day-operator`: calendar-aware close plan for a pressured execution
  day.
- `calendar-dag-scheduler`: maps real `calendar_provider` windows onto the
  `issue_tracker` dependency graph.
- `linear-day-allocator`: turns the day plan into live `issue_tracker`
  ownership, due-date, and state allocation. Linear is one possible
  `issue_tracker`, not a required provider.
- `day-state-updater`: reflows the day when blockers clear, lanes slip, or
  review lands differently than planned.
