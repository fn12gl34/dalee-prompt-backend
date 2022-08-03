import os
import random
import uuid

import redis
from redis import Redis


class RedisProvider:

    def __init__(self):
        self._redis: Redis = redis.from_url(os.environ.get('REDIS_URL'))
        print(f'REDIS: {self._redis}')

    def get(self):
        r = self._redis.keys('*')
        return r

    def set(self):
        self._redis.set(str(uuid.uuid4()), random.randint(228, 1488))
