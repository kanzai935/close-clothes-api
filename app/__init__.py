from flask import Flask, session, render_template, request, redirect

from app import api
from app.api import validate_value_is_none
from app.api import validate_request_path


def create_app(env):
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        counter = api.index()
        roles = api.fetch_roles()
        return render_template('index.html', counter=counter, roles=roles)

    @app.route('/user', methods=['POST'])
    def add_user():
        user_name = request.form['user_name']
        role_name = request.form['role_name']
        user = api.add_user(user_name, role_name)
        session['user_id'] = user.user_id
        return render_template('user/welcome.html', user=user)

    @app.route('/user', methods=['GET'])
    def fetch_user():
        user_id = session.get('user_id')
        user = api.fetch_user(user_id)
        return render_template('user/mypage.html', user=user)

    @validate_request_path
    @validate_value_is_none(session.get('user_id'))
    @app.route('/role', methods=['POST'])
    def add_role():
        user_id = session.get('user_id')
        if user_id is None or not api.validate_request_path(request.path, request.method, user_id):
            return redirect("/")
        role_name = request.form['role_name']
        role_policies = request.form.getlist('role_policy')
        api.add_role(role_name, role_policies)
        return ','.join(role_policies)

    @validate_request_path
    @validate_value_is_none(session.get('user_id'))
    @app.route('/role', methods=['GET'])
    def create_role():
        user_id = session.get('user_id')
        if user_id is None or not api.validate_request_path(request.path, request.method, user_id):
            return redirect("/")
        role_policies = api.fetch_role_policies()
        return render_template('role/index.html', role_policies=role_policies)

    return app
