#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from sync_lib import Category, sync_from_git

SOURCE = 'Code-Dramatist/Rule_Actions'
REPO_URL = 'https://github.com/Code-Dramatist/Rule_Actions.git'
CATEGORIES = (
    Category('direct', Path('Direct_Rule'), Path('clash/direct'), ('.list', '.rule')),
    Category('proxy', Path('Proxy_Rule'), Path('clash/proxy'), ('.list', '.rule')),
    Category('reject', Path('Reject_Rule'), Path('clash/reject'), ('.list', '.rule')),
)

if __name__ == '__main__':
    raise SystemExit(sync_from_git(SOURCE, REPO_URL, CATEGORIES, Path('_sync_report_code_dramatist.json'), 'code_dramatist'))
