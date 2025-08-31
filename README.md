<<<<<<< HEAD
# xavier-server
My own server with xavier
=======
# Jetson AGX Xavier · Minimal Flask Web Server

This is a minimal Flask-based web server scaffold suitable for running on a Jetson AGX Xavier. It serves a simple page with static assets and a health endpoint.

## Structure

```
Server/
├─ app/
│  ├─ __init__.py        # create_app()
│  ├─ views.py           # routes (/, /health)
│  ├─ wsgi.py            # entry for dev and gunicorn
│  ├─ templates/
│  │  ├─ base.html
│  │  └─ index.html
│  └─ static/
│     ├─ css/main.css
│     └─ js/main.js
├─ requirements.txt
├─ run.sh                # quick dev runner (creates venv)
├─ .env.example
├─ deploy/
│  └─ jetson-server.service  # systemd unit example
└─ .gitignore
```

## Quickstart (development)

1) Ensure Python 3.8+ is available (JetPack 5+ on Ubuntu 20.04 has it). Conda base or system Python is fine.

2) Start the dev server (no virtualenv used):

```
./run.sh
```

The server runs on `http://0.0.0.0:8000` by default.

You can override host/port via environment variables:

```
FLASK_HOST=127.0.0.1 FLASK_PORT=5000 ./run.sh
```

Open:

- Home: http://<jetson-ip>:8000/
- Health: http://<jetson-ip>:8000/health

## Production (systemd + gunicorn)

If you prefer not to use a virtual environment and will run with Conda/system Python, make sure `gunicorn` is installed in the environment that systemd will see for your user (PATH). Then:

```
sudo cp deploy/jetson-server.service /etc/systemd/system/jetson-server@<user>.service
sudo systemctl daemon-reload
sudo systemctl enable --now jetson-server@<user>
sudo systemctl status jetson-server@<user>
```

Note: The provided unit file originally referenced a virtualenv path for `gunicorn`. If you are not using a venv, edit the unit to run `gunicorn` from PATH, e.g. set `ExecStart=/usr/bin/env gunicorn --bind 0.0.0.0:8000 app.wsgi:app`.

To change port or environment, edit the `Environment=` lines in the unit file and `sudo systemctl daemon-reload && sudo systemctl restart jetson-server@<user>`.

## Notes

- If you are on an older JetPack (Python < 3.8), pin Flask `<3.0` or upgrade Python.
- For HTTPS and reverse proxy, front with Nginx and proxy to `127.0.0.1:8000`.
- Static assets live under `app/static/`; Jinja templates under `app/templates/`.
>>>>>>> First commit
