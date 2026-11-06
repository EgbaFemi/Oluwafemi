import os, stat
from pathlib import Path
p=Path('fixtures');p.mkdir(exist_ok=True)
f=p/'demo.conf';f.write_text('synthetic=true\n');f.chmod(0o666)
before=stat.S_IMODE(f.stat().st_mode)
assert before & stat.S_IWOTH
f.chmod(0o640)
after=stat.S_IMODE(f.stat().st_mode)
assert after == 0o640 and not after & stat.S_IWOTH
print(f'World-writable fixture detected: {oct(before)}; remediated: {oct(after)}')
print('PASS: insecure permission detected and remediation verified')
