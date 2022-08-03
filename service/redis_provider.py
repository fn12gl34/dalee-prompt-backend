import os

import redis
from redis import Redis


class RedisProvider:

    # key prefixes
    TAG = 'tag'
    SCHEMA = 'schema'
    ATTRIBUTE = 'attribute'

    def __init__(self):
        self.__redis: Redis = redis.from_url(os.environ.get('REDIS_URL'))
        self._prefixes = {self.TAG, self.SCHEMA, self.ATTRIBUTE}

    def validate_prefix(self, prefix: str) -> bool:
        return any([i for i in self._prefixes if i in prefix])

    @property
    def redis_connection(self):
        return self.__redis

    def get(self, key: str):
        if not self.validate_prefix(key):
            return None
        value = self.redis_connection.get(key)
        return value

    def set(self, key: str, data):
        if not self.validate_prefix(key):
            return
        self.redis_connection.set(key, data)

    def get_all(self, prefix: str):
        if not self.validate_prefix(prefix):
            return None
        keys = self.redis_connection.keys(f'{prefix}/*')
        data = []
        for key in keys:
            data.append(self.get(key))
        return data

