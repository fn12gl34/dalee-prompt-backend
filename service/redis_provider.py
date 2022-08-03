import os
import random
import uuid

from aredis import StrictRedis


class RedisProvider:

    def __init__(self):
        self._redis_cluster: StrictRedis = StrictRedis(host=os.environ.get('REDIS_URL'), port=14159)

    async def get(self):
        r = await self._redis_cluster.keys('*')
        return r

    async def set(self):
        await self._redis_cluster.set(uuid.uuid4(), random.randint(228, 1488))
