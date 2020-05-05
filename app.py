from flask import Flask
from redis import Redis
from pymongo import MongoClient
from datetime import datetime
import uuid
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


class User(object):

    def __init__(self):
        mongodb_username = os.environ['MONGODB_USERNAME']
        mongodb_password = os.environ['MONGODB_PASSWORD']
        mongodb_host = os.environ['MONGODB_HOSTNAME']
        self.client = MongoClient(mongodb_host, 27017)
        self.db = self.client['close-clothes']
        self.db.authenticate(mongodb_username,mongodb_password)

    def add_one(self):
        post = {
            'user_id': str(uuid.uuid4()),
            'created_at': datetime.now()
        }
        return self.db.users.insert_one(post)


@app.route('/')
def hello():
    redis.incr('hits')
    user = User()
    rest = user.add_one()
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
