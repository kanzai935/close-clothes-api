from flask import Flask, session, render_template, request, redirect

from app import api


def create_app(env):
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
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

    @app.route('/role', methods=['POST'])
    def add_role():
        user_id = session.get('user_id')
        if user_id is None or api.validate_request_path(request.path, user_id):
            return redirect("/")
        role_name = request.form['role_name']
        role_policies = request.form.getlist('role_policy')
        api.add_role(role_name, role_policies)
        return ','.join(role_policies)

    @app.route('/role', methods=['GET'])
    def create_role():
        user_id = session.get('user_id')
        if user_id is None or api.validate_request_path(request.path, user_id):
            return redirect("/")
        return render_template('role/index.html')

    return app
