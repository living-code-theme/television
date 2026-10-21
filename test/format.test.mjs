import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { resolveAll } from '../scripts/palette.mjs';
import { keys, hexColors, assertContrast } from './helpers.mjs';
const fixture = JSON.parse(await readFile(new URL('./fixtures/upstream.json', import.meta.url)));
const read = path => readFile(new URL('../' + path, import.meta.url), 'utf8');
import * as TOML from 'smol-toml';

for (const f of resolveAll()) test(f.name + ': complete Television flat TOML theme', async () => {
  const t = TOML.parse(await read('themes/' + f.slug + '.toml'));
  keys(t, fixture.colors); hexColors(t);
  assert.equal(t.background, f.r('bg')); assert.equal(t.text_fg, f.r('fg'));
  assert.equal(t.match_fg, f.r('accent')); assert.equal(t.result_line_number_fg, f.r('number'));
  assertContrast(t.text_fg, t.background); assertContrast(t.selection_fg, t.selection_bg);
  for (const mode of ['channel', 'remote_control', 'action_picker']) assertContrast(t[mode + '_mode_fg'], t[mode + '_mode_bg']);
});
