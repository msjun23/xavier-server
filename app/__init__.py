from flask import Flask


def create_app():
    app = Flask(__name__)

    # Simple route registrations live here to keep things small.
    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    return app

