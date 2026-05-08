# Review Modes

Use this reference when choosing the runtime surface for human review.

## Default: Ticket Mode

Use the surviving integration worktree for one ticket.

Choose this when:

- the review question is "did this ticket make the promised relief real?"
- findings should stay easy to route
- the ticket already has a closeout packet and verification receipt

Recommended runtime boot:

- `pnpm install`
- `pnpm dev` for full-stack tickets
- `pnpm dev:desktop` for desktop-only tickets
- `pnpm dev:api` for API-only tickets

## Optional: Bundle Mode

Use a temporary review branch/worktree, never root `main`.

Choose this only when:

- each constituent ticket already closed automated review and verification
- the human question is cross-ticket coherence
- you need to experience the integrated loop as one product slice

Bundle mode rules:

- merge ticket integration branches in dependency order
- use the temporary bundle worktree only as a review surface
- route fixes back into the owning ticket worktree
- refresh the bundle worktree after owner fixes land

## Prohibited: Root Main Review Workspace

Do not merge active ticket worktrees into root `main` just to review them.

Why:

- breaks the operator-only root-main rule
- blurs ticket ownership
- makes patch routing ambiguous
- turns human review into branch archaeology instead of product QA
