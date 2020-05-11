import os

from pymongo import MongoClient

mongodb_username = os.environ['MONGODB_USERNAME']
mongodb_password = os.environ['MONGODB_PASSWORD']
mongodb_host = os.environ['MONGODB_HOST']
mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']


class Model(object):

    def __init__(self, name=None, role=None):
        self.name = name
        self.role = role
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)

    def add_one(self, post=None):
        self.mongodb_db.users.insert_one(post)

    def fetch_one(self, mongodb_filter_key=None, mongodb_filter_value=None):
        mongodb_entity = self.mongodb_db.users.find_one({mongodb_filter_key: mongodb_filter_value})
        return mongodb_entity
