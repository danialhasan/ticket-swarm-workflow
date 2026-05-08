# Reconcile Checklist

Before a ticket reaches human verification, answer these questions explicitly:

- Which branch is the surviving integration candidate?
- Which lane outputs are already integrated into it?
- Which lane outputs are intentionally excluded?
- Which worktrees must remain for follow-up review or runtime repro?
- Which worktrees are safe to remove after verification?
- Is there any hidden file-surface overlap that was “resolved” without a receipt?

If any answer is unclear, the ticket is not ready for closeout.
