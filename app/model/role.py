import os

from pymongo import MongoClient

mongodb_username = os.environ['MONGODB_USERNAME']
mongodb_password = os.environ['MONGODB_PASSWORD']
mongodb_host = os.environ['MONGODB_HOST']
mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']


class Role(object):
    def __init__(self, role_name=None, role_policies=None):
        self.__role_name = role_name
        self.__role_policies = role_policies
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)

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

    def add_one(self):
        role_name_filter = {'role_name': self.role_name}
        role_policies = {'role_policies': self.role_policies}
        post = dict(**role_name_filter, **role_policies)
        self.mongodb_db.roles.update_one(role_name_filter, {'$set': post},
                                         upsert=True)

    def assign(self):
        pass

    def authorize(self, request_path, user_id):
        pass

    def authenticate(self):
        pass

    def fetch_roles(self):
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)
        mongodb_roles = self.mongodb_db.roles.find()
        roles = []
        for mongodb_role in mongodb_roles:
            role = Role(mongodb_role['role_name'], mongodb_role['role_policies'])
            roles.append(role)
        return roles
