import shutil
from pathlib import Path

SRC = Path('/tmp/yuumimi_rules')
DST = Path('.')
MAP = {
    'SocialMedia': ['twitter','instagram','facebook','reddit'],
    'ForeignMedia': ['disney','spotify','bahamut','category-entertainment@!cn'],
}

(DST/'custom'/'Loon').mkdir(parents=True, exist_ok=True)
(DST/'custom'/'Clash').mkdir(parents=True, exist_ok=True)


def load_loon(name):
    p=SRC/'loon'/f'{name}.txt'
    if not p.exists():
        return []
    rows=[]
    for line in p.read_text(encoding='utf-8', errors='ignore').splitlines():
        s=line.strip()
        if not s or s.startswith('#'):
            continue
        rows.append(s)
    return rows


def load_clash(name):
    p=SRC/'clash'/f'{name}.txt'
    if not p.exists():
        return []
    rows=[]
    in_payload=False
    for line in p.read_text(encoding='utf-8', errors='ignore').splitlines():
        s=line.strip()
        if s=='payload:':
            in_payload=True
            continue
        if not in_payload:
            continue
        if s.startswith('- '):
            rows.append(s[2:].strip())
    return rows


def uniq(seq):
    out=[]; seen=set()
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

report=['# yuumimi 全量同步结果（按分类合并）','']
for cat, names in MAP.items():
    loon=[]; clash=[]
    for n in names:
        loon.extend(load_loon(n))
        clash.extend(load_clash(n))
    loon=uniq(loon)
    clash=uniq(clash)
    (DST/'custom'/'Loon'/f'{cat}.lsr').write_text('\n'.join(loon)+'\n', encoding='utf-8')
    (DST/'custom'/'Clash'/f'{cat}.yaml').write_text('payload:\n' + '\n'.join(f'  - {x}' for x in clash) + '\n', encoding='utf-8')
    report.append(f'## {cat}')
    report.append(f'- source: {", ".join(names)}')
    report.append(f'- loon total: {len(loon)}')
    report.append(f'- clash total: {len(clash)}')
    report.append('')
(DST/'docs'/'YUUMIMI-FULL-SYNC.md').write_text('\n'.join(report), encoding='utf-8')
