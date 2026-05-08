# V1 Delivery Source Map

These old-repo files are source material for the first external beta delivery seams:

- updater runtime: `/Users/danialhasan/dev/oldsquad/apps/desktop/src-electron/updater.ts`
- local release flow: `/Users/danialhasan/dev/oldsquad/apps/desktop/scripts/release-local.sh`
- release operator notes: `/Users/danialhasan/dev/oldsquad/apps/desktop/RELEASING.md`

Preserve these behaviors when lowering or implementing delivery in `squad`:

- signed/notarized macOS artifacts
- GitHub Releases publication
- Cloudflare Worker updater feed
- manifest generation and verification, including compatibility endpoints such as `latest.json` and
  `latest-mac.json` when the v1 policy keeps them alive
- updater runtime states and recovery flow
- release/updater telemetry
- primary local operator-machine release job, with any GitHub Actions path treated only as a
  recipe/reference/emergency fallback unless canon later promotes it
