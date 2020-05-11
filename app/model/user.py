import uuid
from datetime import datetime

from app.model.model import Model


class User(Model):

    def __init__(self):
        super(User, self).__init__()

    def add_one(self):
        user_id = str(uuid.uuid4())
        post = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        super(User, self).add_one(post)
        return user_id

    def fetch_one(self, user_id):
        user = super(User, self).fetch_one('user_id', user_id)
        return user['user_id']
