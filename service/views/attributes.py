from aiohttp import web
from service.constants import *


class AttributesView(web.View):

    async def get(self):
        result = self.request.app[REDIS_PROVIDER].get_all(self.request.app[REDIS_PROVIDER].ATTRIBUTE)
        return web.json_response(result)

    async def post(self):
        request_data = await self.request.json()
        redis_key = f'{self.request.app[REDIS_PROVIDER].ATTRIBUTE}/{request_data.get("id")}'
        self.request.app[REDIS_PROVIDER].set(redis_key, request_data)
        return web.json_response(request_data)
