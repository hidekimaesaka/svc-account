from flask import Flask

from app.routes import health, svc_account


def create_app():
    app = Flask(__name__)

    # starting routes
    health.start(app)
    svc_account.start(app)

    return app
