#!/usr/bin/env bash
set -euo pipefail

# Use current Python (e.g., conda base); no installs here
PY=${PY:-python3}

export FLASK_APP=app/wsgi.py
export FLASK_ENV=${FLASK_ENV:-development}

echo "[+] Starting dev server on ${FLASK_HOST:-0.0.0.0}:${FLASK_PORT:-8000}"
exec "$PY" -m app.wsgi
