import assert from 'node:assert/strict';
export const keys = (value, expected) => assert.deepEqual(Object.keys(value).sort(), [...expected].sort());
export function hexColors(value) {
  if (typeof value === 'string') assert.match(value, /^#[a-f0-9]{6}$/);
  else if (Array.isArray(value)) value.forEach(hexColors);
  else { assert.ok(value && typeof value === 'object'); Object.values(value).forEach(hexColors); }
}
const luminance = hex => {
  assert.match(hex, /^#[a-f0-9]{6}$/);
  return [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16) / 255).map(c => c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4).reduce((n, c, i) => n + c * [0.2126, 0.7152, 0.0722][i], 0);
};
export function assertContrast(fg, bg, minimum = 4.5) {
  const a = luminance(fg), b = luminance(bg);
  const ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
  assert.ok(ratio >= minimum, fg + ' on ' + bg + ': contrast ' + ratio.toFixed(2) + ' < ' + minimum);
}
