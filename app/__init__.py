import os
from datetime import datetime

from flask import Flask, make_response

from app import api


def create_app(env):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return api.index()

    @app.route('/user/add', methods=['GET'])
    def add_user():
        user_id = api.add_user()
        response = make_response()
        max_age = 60
        domain = os.environ['DOMAIN_NAME']
        expires = int(datetime.now().timestamp()) + max_age
        response.set_cookie('user_id', value=user_id, max_age=max_age, expires=expires, path='/*', domain=domain,
                            secure=None, httponly=True)
        return response

    @app.route('/user', methods=['GET'])
    def fetch_user():
        # user_id = request.cookies.get('user_id')
        return api.fetch_user('f649d16b-854d-41ae-b900-60aa1373692f')

    return app
