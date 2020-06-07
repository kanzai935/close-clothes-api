from app.model.role.enum_role_policy import EnumRolePolicy
from app.model.role.enum_role_policy_name import EnumRolePolicyName
from app.model.role.role import Role
from app.model.role.role_policy import RolePolicy
from app.model.user.user import User
from app.module.mongodb.mongo_client import MongoDBClient
from app.module.redis.redis_client import RedisClient


def __fetch_api(request_path, request_method):
    mongodb_db = MongoDBClient().get_mongodb()
    mongodb_api = mongodb_db.apis.find_one({'$and': [{'api': request_path}, {'method': request_method}]})
    return mongodb_api


def index():
    redis = RedisClient().get_redis_client()
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


def add_user(user_name, role_name):
    user = User(user_name, role_name)
    user_id = user.add_user()
    user.user_id = user_id
    return user


def fetch_user(user_id):
    user = User()
    mongodb_user = user.fetch_user(user_id)
    user.user_id = mongodb_user['user_id']
    user.user_name = mongodb_user['user_name']
    user.role_name = mongodb_user['role_name']
    return user


def add_role(role_name, role_policies):
    role = Role(role_name, role_policies)
    role.add_role()


def fetch_roles():
    role = Role()
    roles = role.fetch_roles()
    return roles


def validate_request_path(func):
    def wrapper(*args, **kwargs):
        request_path = func(args[0])
        request_method = func(args[1])
        user_id = func(args[2])

        user = fetch_user(user_id)
        role = Role()
        mongodb_role = role.fetch_role(user.role_name)
        role.role_policies = mongodb_role['role_policies']
        mongodb_api = __fetch_api(request_path, request_method)
        return role.authorize(mongodb_api['role_policy'])

    return wrapper


def validate_value_is_none(value):
    def _validate_value_is_none(func):
        def wrapper(*args, **kwargs):
            return value is None

        return wrapper

    return _validate_value_is_none


def fetch_role_policies():
    role_policies = []
    for num_role_policy, role_policy_name in zip(EnumRolePolicy, EnumRolePolicyName):
        role_policy = RolePolicy(num_role_policy, role_policy_name)
        role_policies.append(role_policy)
    return role_policies
