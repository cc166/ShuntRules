#!/usr/bin/env python3
"""
Sync Code-Dramatist/Rule_Actions to ShuntRules
"""
from pathlib import Path
import subprocess
import json
import time

REPO_URL = "https://github.com/Code-Dramatist/Rule_Actions.git"
TEMP_DIR = Path("/tmp/Code-Dramatist-Rule_Actions")
OUT_BASE = Path("clash")
OUT_DIRECT = OUT_BASE / "direct"
OUT_PROXY = OUT_BASE / "proxy"
OUT_REJECT = OUT_BASE / "reject"

report = {
    'meta': {
        'source': 'Code-Dramatist/Rule_Actions',
        'url': REPO_URL,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
    },
    'direct': {'ok': [], 'failed': []},
    'proxy': {'ok': [], 'failed': []},
    'reject': {'ok': [], 'failed': []}
}

def run(cmd):
    """Run shell command and return stdout"""
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\n{r.stderr}")
    return r.stdout.strip()

def clone_or_pull():
    """Clone or pull Code-Dramatist/Rule_Actions"""
    if TEMP_DIR.exists():
        print(f"Pulling latest from {REPO_URL}...")
        run(f"cd {TEMP_DIR} && git pull")
    else:
        print(f"Cloning {REPO_URL}...")
        run(f"git clone --depth 1 {REPO_URL} {TEMP_DIR}")

def sync_category(src_dir, out_dir, category):
    """Sync a category of rules"""
    out_dir.mkdir(parents=True, exist_ok=True)
    
    for item in src_dir.iterdir():
        if item.is_file():
            try:
                dest = out_dir / item.name
                dest.write_text(item.read_text(encoding='utf-8'), encoding='utf-8')
                report[category]['ok'].append(item.name)
                print(f"✓ {category}/{item.name}")
            except Exception as e:
                report[category]['failed'].append({'name': item.name, 'error': str(e)})
                print(f"✗ {category}/{item.name}: {e}")

def sync_all():
    """Sync all categories"""
    sync_category(TEMP_DIR / "Direct_Rule", OUT_DIRECT, 'direct')
    sync_category(TEMP_DIR / "Proxy_Rule", OUT_PROXY, 'proxy')
    sync_category(TEMP_DIR / "Reject_Rule", OUT_REJECT, 'reject')

def save_report():
    """Save sync report"""
    report_file = Path("_sync_report_code_dramatist.json")
    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"\n📊 Report saved to {report_file}")
    print(f"Direct: {len(report['direct']['ok'])} ok, {len(report['direct']['failed'])} failed")
    print(f"Proxy: {len(report['proxy']['ok'])} ok, {len(report['proxy']['failed'])} failed")
    print(f"Reject: {len(report['reject']['ok'])} ok, {len(report['reject']['failed'])} failed")

if __name__ == "__main__":
    print("=== Syncing Code-Dramatist/Rule_Actions ===")
    clone_or_pull()
    sync_all()
    save_report()
