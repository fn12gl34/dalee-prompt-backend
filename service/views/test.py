from aiohttp import web

from service.constants import *


class TestHandler(web.View):
    async def get(self):
        r = self.request.app[REDIS_PROVIDER]
        keys = r.get()
        return {'result': keys}

    async def post(self):
        try:
            r = self.request.app[REDIS_PROVIDER]
            r.set()
        except Exception as e:
            print(f'ERROR: {e}')


class AbobaHandler(web.View):
    async def get(self):
        return {'result': 'aboba'}
