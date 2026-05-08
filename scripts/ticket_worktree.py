#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "lane"


def run_git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=False,
    )


def default_layout(repo_root: Path, ticket_id: str, lanes: list[str], base_ref: str) -> dict:
    ticket_root = repo_root / ".worktrees" / ticket_id
    integration_branch = f"ticket/{ticket_id}/integration"
    integration_path = ticket_root / "integration"
    lane_entries = []
    for lane in lanes:
        lane_slug = slugify(lane)
        lane_entries.append(
            {
                "lane": lane,
                "lane_slug": lane_slug,
                "branch": f"ticket/{ticket_id}/{lane_slug}",
                "path": str(ticket_root / lane_slug),
                "base_ref": integration_branch,
            }
        )
    return {
        "ticket_id": ticket_id,
        "repo_root": str(repo_root),
        "base_ref": base_ref,
        "ticket_root": str(ticket_root),
        "integration": {
            "branch": integration_branch,
            "path": str(integration_path),
            "base_ref": base_ref,
        },
        "lanes": lane_entries,
    }


def ensure_branch_does_not_exist(repo_root: Path, branch: str) -> None:
    result = run_git(repo_root, "show-ref", "--verify", f"refs/heads/{branch}")
    if result.returncode == 0:
        raise SystemExit(f'Branch already exists: "{branch}"')


def create_worktree(repo_root: Path, path: str, branch: str, base_ref: str) -> None:
    ensure_branch_does_not_exist(repo_root, branch)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    result = run_git(repo_root, "worktree", "add", "-b", branch, path, base_ref)
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "git worktree add failed")


def cmd_plan(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    layout = default_layout(repo_root, args.ticket, args.lanes, args.base_ref)
    print(json.dumps(layout, indent=2))
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    layout = default_layout(repo_root, args.ticket, args.lanes, args.base_ref)

    integration = layout["integration"]
    create_worktree(
        repo_root,
        integration["path"],
        integration["branch"],
        integration["base_ref"],
    )

    for lane in layout["lanes"]:
        create_worktree(
            repo_root,
            lane["path"],
            lane["branch"],
            lane["base_ref"],
        )

    print(json.dumps(layout, indent=2))
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    ticket_root = repo_root / ".worktrees" / args.ticket
    result = run_git(repo_root, "worktree", "list", "--porcelain")
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "git worktree list failed")

    worktrees = []
    current: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if not line:
            if current:
                worktrees.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        current[key] = value
    if current:
        worktrees.append(current)

    matching = []
    for entry in worktrees:
        path = entry.get("worktree", "")
        if path.startswith(str(ticket_root)):
            matching.append(entry)

    print(json.dumps({"ticket_id": args.ticket, "worktrees": matching}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Plan or create per-ticket worktrees for parallel lane execution."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo-root", default=".", help="Path to the repo root. Defaults to cwd.")
    common.add_argument("--ticket", required=True, help="Ticket id, for example SQD-884")
    common.add_argument("--base-ref", default="main", help="Base ref for the integration branch")
    common.add_argument(
        "--lane",
        dest="lanes",
        action="append",
        default=[],
        help="Lane name. May be provided multiple times.",
    )

    plan_parser = subparsers.add_parser("plan", parents=[common])
    plan_parser.set_defaults(func=cmd_plan)

    create_parser = subparsers.add_parser("create", parents=[common])
    create_parser.set_defaults(func=cmd_create)

    status_parser = subparsers.add_parser("status", parents=[common])
    status_parser.set_defaults(func=cmd_status)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "lanes", None):
        args.lanes = []
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
