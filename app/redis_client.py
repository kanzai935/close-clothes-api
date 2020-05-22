import os

from redis import Redis


class RedisClient(object):
    def __init__(self):
        pass

    @staticmethod
    def get_redis_client():
        return Redis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']))
