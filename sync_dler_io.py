#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from sync_lib import Category, sync_from_git

SOURCE = 'dler-io/Rules'
REPO_URL = 'https://github.com/dler-io/Rules.git'
CATEGORIES = (
    Category('provider', Path('Surge/Surge 3/Provider'), Path('surge/provider'), ('.list',)),
    Category('media', Path('Surge/Surge 3/Provider/Media'), Path('surge/media'), ('.list',)),
)

if __name__ == '__main__':
    raise SystemExit(sync_from_git(SOURCE, REPO_URL, CATEGORIES, Path('_sync_report_dler_io.json'), 'dler_io'))
