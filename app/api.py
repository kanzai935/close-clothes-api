import os
import uuid
from datetime import datetime

from pymongo import MongoClient
from redis import Redis

redis = Redis(host='redis', port=6379)


class User(object):

    def __init__(self):
        mongodb_username = os.environ['MONGODB_USERNAME']
        mongodb_password = os.environ['MONGODB_PASSWORD']
        mongodb_host = os.environ['MONGODB_HOSTNAME']
        mongodb_database = os.environ['MONGODB_DATABASE']
        self.client = MongoClient(mongodb_host, 27017)
        self.db = self.client[mongodb_database]
        self.db.authenticate(mongodb_username, mongodb_password)

    def add_one(self):
        post = {
            'user_id': str(uuid.uuid4()),
            'created_at': datetime.now()
        }
        return self.db.users.insert_one(post)


def index():
    redis.incr('hits')
    user = User()
    rest = user.add_one()
    return 'Hello World! I have been seen %s times.' % redis.get('hits')
