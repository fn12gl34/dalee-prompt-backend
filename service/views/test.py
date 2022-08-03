from aiohttp import web

from service.constants import *


class TestHandler(web.View):
    async def get(self):
        r = self.request.app[REDIS_PROVIDER]
        keys = await r.get()
        return {'result': keys}

    async def post(self):
        r = self.request.app[REDIS_PROVIDER]
        await r.set()
