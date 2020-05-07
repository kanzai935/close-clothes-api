from flask import Flask

from app import api


def create_app(env):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return api.index()

    return app
