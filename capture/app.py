"""Capture Television's real search and preview over the shared fixture project."""


def prepare(c):
    c.copy(f'themes/{c.slug}.toml', f'.config/television/themes/{c.slug}.toml')
    c.write('.config/television/config.toml', f'[ui]\ntheme = "{c.slug}"\n')
    return ['tv', '--source-command', 'find . -type f | sort', '--preview-command', 'cat {}']


def drive(c):
    c.wait_text(r'FieldRenderer|package.json')
    c.type('Field')
    c.wait_text('FieldRenderer')
