# Public Taxonomy

Ticket Swarm Workflow stays Squad-branded, but the runtime skills must not
pretend every reader has Squad's internal stack. Use the adapter terms below
when a workflow depends on project-specific tools, services, or proof surfaces.

When a term cannot be resolved from the current workspace, ask the reader's
agent to fill it from the reader's own codebase, tracker, release system, and
receipts.

## Adapter Terms

| Term | Meaning | Evidence it owns | Must not be treated as | Example providers |
| --- | --- | --- | --- | --- |
| `issue_tracker` | The system that owns ticket identity, state, dependency order, assignment, and due-date pressure. | Issue ids, status, blockers, dependencies, assignees, comments, checklist state. | A proof receipt, source of product truth by itself, or substitute for code/runtime verification. | Jira, Linear, GitHub Issues, Shortcut, YouTrack. |
| `calendar_provider` | The availability and scheduling source used to turn a work plan into real execution windows. | Calendar events, focus blocks, review windows, day constraints, meeting conflicts. | A dependency graph, release authority, or implementation receipt. | Google Calendar, Outlook Calendar, Cron, Cal.com. |
| `team_chat` | The collaboration surface where product decisions, clarifications, and handoffs may appear. | Message links, channel/thread references, decision excerpts, stakeholder corrections. | Canonical product state, durable requirements truth without source authority, or a complete audit log. | Slack, Microsoft Teams, Discord, Mattermost, Zulip. |
| `db_runtime` | The database-backed runtime that owns durable product state and queryable telemetry for the host product. | Canonical rows, read models, telemetry records, migrations, query results, persistence receipts. | A screenshot, in-memory fixture, local mock, or unverified trace. | Neon Postgres, Amazon RDS Postgres, Supabase, Railway Postgres, Cloud SQL. |
| `eval_mirror` | A non-authoritative mirror or review surface for eval examples, model traces, scorers, or run summaries. | Mirrored examples, run ids, trace links, scorer outputs, dataset sync receipts. | Canonical source of truth, promotion authority, or replacement for repo-owned fixtures and receipts. | Braintrust, LangSmith, W&B Weave, Arize/Phoenix, Humanloop, repo-owned exporters. |
| `research_control_plane` | The system used to organize research claims, experiments, evidence, or hypothesis graphs. | Claim ids, experiment records, source links, decision trails, evidence bundles. | Product runtime truth or evidence that a user-facing flow works. | Flywheel, Notion databases, Airtable, Coda, custom research graphs. |
| `ui_automation_driver` | The browser, desktop, or app automation layer used to inspect and prove user-facing behavior. | Screenshots, DOM snapshots, accessibility trees, click paths, route state, visual receipts. | Durable state proof, database proof, or release proof unless paired with the required backend evidence. | Playwright, Cypress, Browser Use, Selenium, Computer Use, WebDriver. |
| `artifact_host` | The place where release artifacts, packages, installers, or binaries are published. | Artifact URLs, checksums, signatures, release pages, download metadata. | Proof that the updater/feed is correct or that users received the release. | GitHub Releases, S3, R2, GCS, Azure Blob Storage, package registries. |
| `updater_feed` | The release metadata endpoint or channel feed consumed by an app or deployment runtime. | Feed URLs, manifest payloads, channel metadata, version pointers, compatibility endpoints. | A release decision, artifact signature, or successful install proof by itself. | Static JSON feed, update server, app-store channel, package registry metadata, custom API. |
| `release_policy_ref` | The reader's source of truth for release gates, approval boundaries, rollback rules, and exposure policy. | Policy docs, release checklists, deployment runbooks, approval gates, rollback procedures. | A live release receipt or proof that the current version is ready. | Repo docs, runbooks, platform playbooks, change-management records. |
| `proof_query` | A query or command that proves a claim from durable state, telemetry, or authoritative receipts. | Query text, result rows, timestamps, ids, correlation or causation references. | A summary, a manually written claim, or a raw log line with no durable backing. | SQL query, API runtime-proof endpoint, analytics query, saved dashboard query. |
| `primary_reviewer` | The configured human authority for product judgment, risk acceptance, or release exposure. | Approval notes, review decisions, HOLD waivers, explicit deferrals, release decisions. | A machine-verifiable proof substitute or a replacement for tests and runtime evidence. | Product owner, engineering lead, release manager, domain expert, founder. |

## Usage Rule

Skills should name the adapter role first and the vendor second. For example:

- say "read from the configured `issue_tracker`; examples include Jira,
  Linear, GitHub Issues, or Shortcut";
- do not say "read from Linear" unless the local workspace explicitly declares
  Linear as its `issue_tracker`;
- say "verify through the configured `db_runtime`";
- do not imply any specific Postgres provider is required.

Squad examples can remain in this repository as public examples of the workflow,
but private code paths, private ticket ids, and private release machinery should
be replaced with these adapter terms or with reader-owned placeholders.
