import os

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from project.api.ping import ping_blueprint


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)

    app.register_blueprint(ping_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
