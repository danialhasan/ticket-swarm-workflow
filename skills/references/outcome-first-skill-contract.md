# Outcome-First Skill Contract

Ticket Swarm skills should stay compact when first loaded. Put the decision
contract at the top and move long checklists, examples, and edge-case catalogs
into references.

## Skill Body Shape

Each skill should answer these six questions before detailed process:

1. When should this skill be used?
2. When should it not be used?
3. What inputs are required?
4. What success condition closes the skill?
5. What stop condition requires human judgment?
6. What receipt must be left behind?

## Prompting Posture

- Start from outcome, success, constraints, and evidence.
- Let the model choose local tactics unless exact sequencing protects product
  truth, permissions, safety, or verification.
- Prefer one primary workflow per pass.
- Avoid repeating generic receipt, Linear, proof, and stop rules in every
  skill; link to shared references when the same rule applies.
- Keep primary product claims stricter than implementation progress claims.

## Routing Rule

Use `$ticket-swarm-router` before activating multiple Ticket Swarm skills. The
router picks the smallest correct next skill and prevents the whole workflow
library from entering context at once.
