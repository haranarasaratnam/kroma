#!/usr/bin/env bash
# Auto-deploy KROMA on PythonAnywhere.
#
# Fast-forwards the checkout to origin/main, then touches the WSGI file
# (which triggers a web-app reload) only if HEAD actually moved.
#
# Intended for the PythonAnywhere "Tasks" tab. Override REPO/WSGI with
# env vars if your layout differs from the defaults.

set -euo pipefail

REPO="${KROMA_REPO:-${HOME}/kroma}"
WSGI="${KROMA_WSGI:-/var/www/${USER}_pythonanywhere_com_wsgi.py}"

cd "$REPO"

before="$(git rev-parse HEAD)"
git pull --ff-only --quiet origin main
after="$(git rev-parse HEAD)"

if [[ "$before" == "$after" ]]; then
    echo "[$(date -u +%FT%TZ)] up-to-date at $(git rev-parse --short HEAD)"
    exit 0
fi

touch "$WSGI"
echo "[$(date -u +%FT%TZ)] deployed ${before:0:7} -> ${after:0:7}"
