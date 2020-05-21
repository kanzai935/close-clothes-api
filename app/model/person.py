from app.mongo_client import MongoDBClient


class Person(object):

    def __init__(self):
        self.__mongodb_db = MongoDBClient().get_mongodb()

    def __get_collection_name_from_child_class_name(self):
        return '%ss' % self.__class__.__name__.lower()

    def add_one(self, mongodb_post=None):
        collection_name = self.__get_collection_name_from_child_class_name()
        self.__mongodb_db[collection_name].insert_one(mongodb_post)

    def fetch_one(self, mongodb_filter=None):
        collection_name = self.__get_collection_name_from_child_class_name()
        mongodb_entity = self.__mongodb_db[collection_name].find_one({mongodb_filter['key']: mongodb_filter['value']})
        return mongodb_entity
