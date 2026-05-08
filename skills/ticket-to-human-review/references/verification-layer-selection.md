# Verification Layer Selection

Every ticket must inspect all verification layers. Run the ones that protect the seam and
explicitly mark the rest as not required with a short reason.

Every verification plan must also include the touched-scope repo health floor:

- lint
- typecheck
- test
- build

If one of these is not applicable, say why explicitly. "We forgot to run it" is not a valid reason.

## Property

Use for:

- invariants
- reducers
- serializers
- event ordering
- retry behavior
- state-space rules

Skip when the seam has no meaningful invariant beyond concrete examples.

## Unit

Use for:

- pure functions
- mappers
- local decision logic
- small utilities

Skip when the seam is mostly contract wiring or end-to-end behavior.

## Contract

Use for:

- API envelopes
- command/query/realtime contracts
- schema validation
- error shapes

Skip only when the ticket cannot affect any public or shared contract surface.

## Model

Use for:

- lifecycle rules
- transition systems
- proof/review lineage
- blocked vs waiting distinctions

Skip when the ticket does not change model behavior or state transitions.

## Integration

Use for:

- multi-layer behavior
- persistence plus projection plus query flows
- adapter boundaries
- auth, provider, and integration posture

Skip only when the change is truly isolated and cannot fail at a boundary.

## Smoke

Use for:

- user-visible surface activation
- route-level sanity
- first-loop workflow checks

Skip when the seam is fully internal and has no operator-visible consequence.

## Electron MCP / UI green pass

Use for:

- Electron tickets
- UI tickets
- any operator-visible surface where an agent can drive the app directly

The verification plan must name:

- the entry window, route, or screen
- the exact clicks, inputs, and navigation steps to execute
- the expected green state after each meaningful interaction
- the evidence to capture in the receipt
- the serialized Electron lease note for that verifier run

Skip only when the ticket has no UI or Electron runtime surface.

## Telemetry / runtime queries

Use for:

- runtime-proof surfaces
- receipts
- events, projections, and lifecycle visibility
- anything that must be proven in the running system

Skip only when no runtime evidence is expected for the seam.
