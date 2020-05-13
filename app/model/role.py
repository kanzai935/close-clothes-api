import os

from pymongo import MongoClient

mongodb_username = os.environ['MONGODB_USERNAME']
mongodb_password = os.environ['MONGODB_PASSWORD']
mongodb_host = os.environ['MONGODB_HOST']
mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']


class Role(object):
    def __init__(self, role_name=None, role_policies=None):
        self.role_name = role_name
        self.role_policies = role_policies
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)

    def add_one(self):
        post = {
            'role_name': self.role_name,
            'role_policies': self.role_policies
        }
        self.mongodb_db.roles.insert_one(post)

    def assign(self):
        pass

    def authorize(self):
        pass

    def authenticate(self):
        pass
