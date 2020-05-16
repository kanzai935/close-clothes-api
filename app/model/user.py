import uuid
from datetime import datetime

from app.model.person import Person


class User(Person):

    def __init__(self, user_name=None, role_name='default', user_id=None):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__role_name = role_name
        super(User, self).__init__()

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def role_name(self):
        return self.__role_name

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    @role_name.setter
    def role_name(self, value):
        self.__role_name = value

    @user_id.deleter
    def user_id(self):
        del self.__user_id

    @user_name.deleter
    def user_name(self):
        del self.__user_name

    @role_name.deleter
    def role_name(self):
        del self.__role_name

    def add_one(self):
        user_id = str(uuid.uuid4())
        mongodb_post = {
            'user_id': user_id,
            'user_name': self.user_name,
            'role_name': self.role_name,
            'created_at': datetime.now()
        }
        super(User, self).add_one(mongodb_post)
        return user_id

    def fetch_one(self, user_id):
        mongodb_filter = {'key': 'user_id', 'value': user_id}
        mongodb_user = super(User, self).fetch_one(mongodb_filter)
        return mongodb_user
