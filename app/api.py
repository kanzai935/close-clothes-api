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
    return user_id


def fetch_user(user_id):
    user = User()
    mongodb_user_id = user.fetch_one(user_id)
    return mongodb_user_id


def add_role(role_name, role_policies):
    role = Role(role_name, role_policies)
    role.add_one()


def fetch_roles():
    roles = Role.fetch_roles()
    return roles
