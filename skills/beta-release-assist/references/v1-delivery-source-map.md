# Legacy Delivery Source Map Template

Use this file only when the target codebase has previous release behavior that
must be preserved during a Squad-style delivery pass.

Ask the reader's agent to fill this from the reader's own repository and release
records. Do not copy private local paths, old machine-specific scripts, or
company-internal release notes into a public skill.

## Source Files To Discover

- updater runtime: `<PROJECT_ROOT>/<path-to-updater-runtime>`
- release script or workflow: `<PROJECT_ROOT>/<path-to-release-entrypoint>`
- release policy or operator notes: `<release_policy_ref>`
- artifact manifest or package config: `<PROJECT_ROOT>/<path-to-artifact-manifest>`
- telemetry or proof query: `<proof_query>`

## Behaviors To Preserve

- artifact signing, notarization, or integrity checks required by the target
  platform
- publication to the configured `<artifact_host>`
- generation and verification of the configured `<updater_feed>`
- manifest compatibility endpoints required by the target app or deployment
  runtime
- updater runtime states and recovery flow
- release, updater, or deployment telemetry required by the host product
- primary release job and any documented fallback release path

## Output Contract

The release-assist agent should leave a source-map note that names:

- each source file inspected;
- which behavior it preserves;
- which behavior is intentionally retired;
- which behavior remains unknown or blocked;
- which proof receipt or `<proof_query>` verifies the current release path.
