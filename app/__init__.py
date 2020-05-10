from flask import Flask, session, render_template

from app import api


def create_app(env):
    app = Flask(__name__)

    @app.route('/')
    def index():
        counter = api.index()
        return render_template('index.html', counter=counter)

    @app.route('/user', methods=['POST'])
    def add_user():
        user_id = api.add_user()
        session['user_id'] = user_id
        return render_template('user/welcome.html', user_id=user_id)

    @app.route('/user', methods=['GET'])
    def fetch_user():
        user_id = session.get('user_id')
        mongodb_user_id = api.fetch_user(user_id)
        return render_template('user/mypage.html', mongodb_user_id=mongodb_user_id)

    return app
