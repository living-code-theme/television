#!/usr/bin/env python3
"""Optional real-terminal smoke test. Runs in temporary homes without credentials or user config."""
import fcntl, json, os, pathlib, re, select, shutil, signal, struct, subprocess, tempfile, termios, time
repo = pathlib.Path(__file__).resolve().parents[1]
binary = shutil.which(os.environ.get('NATIVE_BINARY', 'tv'))
if not binary:
    raise SystemExit('Install tv or set NATIVE_BINARY to its absolute path')
flavors = json.loads((repo/'palette/theme.json').read_text())['flavors']
for flavor in flavors:
    slug = flavor['slug']
    with tempfile.TemporaryDirectory(prefix='living-code-television-') as temporary:
        home = pathlib.Path(temporary)
        config = home/'.config'; config.mkdir()
        work = home/'work'; work.mkdir()
        (work/'example.rs').write_text('fn greet(name: &str) -> String {\n    format!("Hello, {name}")\n}\n')
        env = { 'PATH': os.environ['PATH'], 'HOME': str(home), 'XDG_CONFIG_HOME': str(config), 'XDG_CACHE_HOME': str(home/'.cache'),
                'XDG_DATA_HOME': str(home/'.local/share'), 'XDG_STATE_HOME': str(home/'.local/state'), 'TERM': 'xterm-256color',
                'COLORTERM': 'truecolor', 'MICRO_TRUECOLOR': '1', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'SHELL': '/bin/sh' }
        if os.environ.get('TERMINFO_DIRS'): env['TERMINFO_DIRS'] = os.environ['TERMINFO_DIRS']
        shutil.copytree(repo/'themes', config/'television/themes', dirs_exist_ok=True)
        (config/'television/config.toml').write_text('[ui]\ntheme = "'+slug+'"\n')
        args = [binary, '--source-command', "printf 'alpha\\nbeta\\ngamma\\n'", '--no-preview']
        pid, fd = os.forkpty()
        if pid == 0:
            os.chdir(work)
            fcntl.ioctl(0, termios.TIOCSWINSZ, struct.pack('HHHH', 36, 120, 0, 0))
            os.execve(binary, args, env)
        output = b''
        try:
            end = time.monotonic()+2
            while time.monotonic() < end:
                ready, _, _ = select.select([fd], [], [], 0.1)
                if not ready: continue
                try: data = os.read(fd, 1024*1024)
                except OSError: break
                if not data: break
                output += data
                if b'\x1b[6n' in data: os.write(fd, b'\x1b[1;1R')
                if b']11;?' in data: os.write(fd, b'\x1b]11;rgb:1010/1818/2020\x07')
                if b']10;?' in data: os.write(fd, b'\x1b]10;rgb:d0d0/d0d0/d0d0\x07')
        finally:
            try: os.kill(pid, signal.SIGTERM)
            except ProcessLookupError: pass
            time.sleep(0.05)
            try: os.kill(pid, signal.SIGKILL)
            except ProcessLookupError: pass
            os.waitpid(pid, 0)
            os.close(fd)
        hits = set()
        for value in flavor['colors'].values():
            color = value['hex']
            rgb = [int(color[i:i+2], 16) for i in (1, 3, 5)]
            if (';2;'+';'.join(map(str, rgb))).encode() in output: hits.add(color)
        clean = re.sub(rb'\x1b\[[0-9;? :><]*[a-zA-Z~]', b'', output).decode('utf8', 'replace')
        if re.search(r'(?i)(failed to (?:parse|load|deserialize)|invalid (?:color|theme|config)|could not load theme|error loading theme|panicked at)', clean):
            raise SystemExit(slug+': theme/config error: '+clean[-1500:])
        if len(hits) < 2: raise SystemExit(slug+': palette not observed in real terminal output: '+clean[-1500:])
        print(slug+': native application rendered '+str(len(hits))+' pinned palette colors')
