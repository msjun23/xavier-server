import os
from . import create_app

app = create_app()

if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", "8000"))
    debug = os.getenv("FLASK_ENV", "").lower() == "development"
    app.run(host=host, port=port, debug=debug)

