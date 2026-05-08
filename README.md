# Ticket Swarm Workflow

Codex workflow plugin for moving Squad work from design contracts into signed-off implementation contracts, iterative multi-agent development/testing loops, review waves, layered verification, receipts, and release handoff.

## Contents

- `.codex-plugin/plugin.json` defines the plugin metadata and default routing prompt.
- `skills/` contains the workflow skills.
- `scripts/ticket_worktree.py` contains the local ticket worktree helper.

## Install

Use this repository as a Codex plugin source. The plugin root is the repository root.

```sh
codex plugin install git+https://github.com/danialhasan/ticket-swarm-workflow.git
```

## Notes

This plugin is extracted from the Squad repo-local workflow layer. Keep changes grounded in the actual ticket execution loop: Linear governance, filesystem receipts, review loops, verification proof, and human signoff.
