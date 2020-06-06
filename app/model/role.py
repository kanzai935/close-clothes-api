from app.module.mongodb.mongo_client import MongoDBClient


class Role(object):
    def __init__(self, role_name=None, role_policies=None):
        self.__role_name = role_name
        self.__role_policies = role_policies
        self.__mongodb_db = MongoDBClient().get_mongodb()

    @property
    def role_name(self):
        return self.__role_name

    @property
    def role_policies(self):
        return self.__role_policies

    @role_name.setter
    def role_name(self, value):
        self.__role_name = value

    @role_policies.setter
    def role_policies(self, value):
        self.__role_policies = value

    @role_name.deleter
    def role_name(self):
        del self.__role_name

    @role_policies.deleter
    def role_policies(self):
        del self.__role_policies

    def add_role(self):
        role_name_filter = {'role_name': self.__role_name}
        role_policies = {'role_policies': self.__role_policies}
        post = dict(**role_name_filter, **role_policies)
        self.__mongodb_db.roles.update_one(role_name_filter, {'$set': post},
                                           upsert=True)

    def assign(self):
        pass

    def authorize(self, mongodb_role_policies_on_apis):
        self.__role_policies.sort()
        return self.__role_policies[0] in mongodb_role_policies_on_apis

    def authenticate(self):
        pass

    def fetch_roles(self):
        mongodb_roles = self.__mongodb_db.roles.find()
        roles = []
        for mongodb_role in mongodb_roles:
            role = Role(mongodb_role['role_name'], mongodb_role['role_policies'])
            roles.append(role)
        return roles

    def fetch_role(self, role_name):
        mongodb_role = self.__mongodb_db.roles.find_one({'role_name': role_name})
        return mongodb_role
