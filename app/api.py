from redis import Redis

from app.model.role import Role
from app.model.user import User

redis = Redis(host='redis', port=6379)


def index():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


def add_user(user_name, role_name):
    user = User(user_name, role_name)
    user_id = user.add_one()
    user.user_id = user_id
    return user


def fetch_user(user_id):
    user = User()
    mongodb_user = user.fetch_one(user_id)
    user.user_id = mongodb_user['user_id']
    user.user_name = mongodb_user['user_name']
    user.role_name = mongodb_user['role_name']
    return user


def add_role(role_name, role_policies):
    role = Role(role_name, role_policies)
    role.add_one()


def fetch_roles():
    role = Role()
    roles = role.fetch_roles()
    return roles
