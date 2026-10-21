// Television theme documents use flat TOML keys, not the main config's [ui] table.
const roles = { background: 'bg', border_fg: 'border', text_fg: 'fg', dimmed_text_fg: 'fgMuted', input_text_fg: 'accent',
  result_count_fg: 'fgMuted', result_name_fg: 'fg', result_line_number_fg: 'number', result_value_fg: 'fgAlt',
  selection_fg: 'fg', selection_bg: 'selection', match_fg: 'accent', preview_title_fg: 'heading',
  channel_mode_fg: 'bg', channel_mode_bg: 'accent', remote_control_mode_fg: 'bg', remote_control_mode_bg: 'success',
  action_picker_mode_fg: 'bg', action_picker_mode_bg: 'info' };
export function generate(flavors) {
  return flavors.map(f => ({ path: `themes/${f.slug}.toml`, content: Object.entries(roles).map(([key, role]) => `${key} = "${f.r(role)}"`).join('\n') + '\n' }));
}
