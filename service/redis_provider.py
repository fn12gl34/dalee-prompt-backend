import random
import uuid

from aredis import StrictRedis


class RedisProvider:

    def __init__(self):
        self._redis_cluster: StrictRedis = StrictRedis(host='redis://:pb2c7fb1a07102688307b10e1eb913a7c1fe603c71bc160564c22df24a077f5e5@ec2-52-48-130-152.eu-west-1.compute.amazonaws.com', port=14159)

    async def get(self):
        r = await self._redis_cluster.keys('*')
        return r

    async def set(self):
        await self._redis_cluster.set(uuid.uuid4(), random.randint(228, 1488))
