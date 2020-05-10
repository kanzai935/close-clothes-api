import os
import uuid
from datetime import datetime

from pymongo import MongoClient

mongodb_username = os.environ['MONGODB_USERNAME']
mongodb_password = os.environ['MONGODB_PASSWORD']
mongodb_host = os.environ['MONGODB_HOST']
mongodb_database_name = os.environ['MONGODB_DATABASE_NAME']


class User(object):

    def __init__(self):
        self.mongodb_db = MongoClient(mongodb_host, 27017)[mongodb_database_name]
        self.mongodb_db.authenticate(mongodb_username, mongodb_password)

    def add_one(self):
        user_id = str(uuid.uuid4())
        post = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.mongodb_db.users.insert_one(post)
        return user_id

    def fetch_one(self, user_id):
        user = self.mongodb_db.users.find_one({'user_id': user_id})
        return user['user_id']
