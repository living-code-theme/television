// Package committed, verified payloads. Never regenerate or adopt a palette at release time.
import { execFileSync } from 'node:child_process';
import { mkdir, readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { check } from './check.mjs';
const root = fileURLToPath(new URL('../', import.meta.url));
const { manifest, pkg } = await check();
execFileSync(process.execPath, ['--test', 'test/format.test.mjs'], { cwd: root, stdio: 'inherit' });
await mkdir(new URL('../dist/', import.meta.url), { recursive: true });
const output = 'dist/living-code-' + manifest.slug + '-' + pkg.version + '.tar.gz';
execFileSync('tar', ['-czf', output, '--', 'README.md', 'LICENSE', 'port.json', ...manifest.files], { cwd: root, stdio: 'inherit' });
console.log(output);
