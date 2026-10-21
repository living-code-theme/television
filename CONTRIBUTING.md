# Maintaining this port

This repository owns its application mappings, generator, tests and committed theme files. It does not depend on a
core checkout during normal builds or installation. Requires Node 22.22+ and pnpm 12.9.0 for maintenance only.

## Build and verify

```sh
pnpm install --frozen-lockfile
pnpm build
pnpm check
pnpm test
```

- `src/generate.mjs`: this application's format and semantic-role mappings. The interface is `generate(flavors)`,
  returning `{ path, content }` records for the four resolved flavors in the pinned snapshot. It performs no writes.
- `palette/theme.json`: app-agnostic resolved palette data, pinned to a core Git revision and SHA-256 fingerprint.
- `scripts/color.mjs`: vendored core color math used for application-specific mixtures, verified against the pin.
- `scripts/generated.json`: this port's explicit managed-file allowlist. Build changes only these files; check
  reports stale bytes without writing them. Neither command contacts GitHub or reads another repository.
- `test/`: deterministic generation, palette adoption, containment and applicable native-format/grammar/semantic
  role regressions. These are maintained here, not in a central application generator.

README, metadata, marketplace identities, licenses, icons, screenshots, handwritten runtime files and publishing
workflows are not generated. Packaging uses committed files and refuses stale generated themes; it does not rebuild.

## Adopt a palette update explicitly

In a reviewed [core](https://github.com/living-code-theme/core) checkout, run `pnpm build`, `pnpm check` and
`pnpm test`, then commit the palette/math inputs. In this port:

```sh
pnpm palette:update /path/to/core
pnpm build
pnpm check
pnpm test
```

The update command verifies core's export against its committed palette/resolver/math files, refuses dirty/stale
inputs, and changes only this port's palette pin. It is never run on install or as part of a normal build. If core's
color math changed, review and copy that revision's `src/color.mjs` into this port's `scripts/color.mjs` first.

Review the pin and generated diff in this repository's own pull request. Preserve intentional app-specific choices;
update expected role contracts only when the policy change is deliberate. Refresh real application screenshots
when visible colors change. Publishing and release workflows remain separate maintainer operations.


## Upstream contract and packaging

`test/fixtures/upstream.json` records the reviewed upstream API and its source revision or published documentation.
`test/format.test.mjs` validates committed native payloads, semantic mappings and applicable contrast pairs.
Refresh the upstream fixture deliberately when the application changes; do not derive expected fields from the generator.
No application credentials, model calls, Docker daemon or sibling checkout are needed by the normal test suite.

Run `pnpm package` to verify and archive the committed files into `dist/`. CI uploads the same installable archive
as a workflow artifact. It does not publish a marketplace entry, create a release or regenerate any theme file.
Capture the real application before adding images; `port.json` currently declares `images: []` intentionally.

## Real application smoke test

Run `pnpm test:native` with Python 3 and `tv` installed on a POSIX system, or set `NATIVE_BINARY` to an absolute
binary path. It launches all four flavors in temporary homes and real pseudo-terminals with a local three-item
source command, checks for native theme errors, and requires the pinned palette in rendered output.
CI uses checksum-pinned Television 0.15.9. No channels are downloaded and no user configuration is read.
This is a loading/rendering smoke test, not a visual screenshot review.
