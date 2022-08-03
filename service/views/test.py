from aiohttp import web
from aiohttp.web_response import Response

from service.constants import *


class TestHandler(web.View):
    async def get(self):
        r = self.request.app[REDIS_PROVIDER]
        keys = r.get()
        return Response(body={'result': keys})

    async def post(self):
        try:
            r = self.request.app[REDIS_PROVIDER]
            r.set()
        except Exception as e:
            print(f'ERROR: {e}')
        return Response(text='fuck you boy')
