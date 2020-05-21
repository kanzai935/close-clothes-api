import os

from pymongo import MongoClient


class MongoDBClient(object):

    def __init__(self):
        self.__mongodb_username = os.environ['MONGODB_USERNAME']
        self.__mongodb_password = os.environ['MONGODB_PASSWORD']
        self.__mongodb_host = os.environ['MONGODB_HOST']
        self.__mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']
        self.__mongodb_port = os.environ['MONGODB_PORT']
        self.__mongodb_db = MongoClient(self.__mongodb_host, int(self.__mongodb_port))[self.__mongodb_database_name]
        self.__mongodb_db.authenticate(self.__mongodb_username, self.__mongodb_password)

    def get_mongodb(self):
        return self.__mongodb_db