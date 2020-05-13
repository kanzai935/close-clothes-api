import os

from pymongo import MongoClient

mongodb_username = os.environ['MONGODB_USERNAME']
mongodb_password = os.environ['MONGODB_PASSWORD']
mongodb_host = os.environ['MONGODB_HOST']
mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']


class Person(object):

    def __init__(self, name=None):
        self.name = name
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)

    def __get_collection_name_from_child_class_name(self):
        return '%ss' % self.__class__.__name__.lower()

    def add_one(self, post=None):
        collection_name = self.__get_collection_name_from_child_class_name()
        self.mongodb_db[collection_name].insert_one(post)

    def fetch_one(self, mongodb_filter=None):
        collection_name = self.__get_collection_name_from_child_class_name()
        mongodb_entity = self.mongodb_db[collection_name].find_one({mongodb_filter['key']: mongodb_filter['value']})
        return mongodb_entity
