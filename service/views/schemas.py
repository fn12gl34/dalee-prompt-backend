from aiohttp import web
from service.constants import *


class SchemasView(web.View):

    async def get(self):
        schema = self.request.app[REDIS_PROVIDER].get('schema')
        return web.json_response(schema)

    async def post(self):
        request_data = await self.request.json()
        self.request.app[REDIS_PROVIDER].set('schema', request_data)
        return web.json_response(request_data)

