from aiohttp import web
from service.constants import *


class AttributesView(web.View):

    async def get(self):
        request_data = await self.request.json()
        if 'id' in request_data:
            redis_key = f'{self.request.app[REDIS_PROVIDER].ATTRIBUTE}/{request_data.get("id")}'
            result = self.request.app[REDIS_PROVIDER].get(redis_key)
        else:
            result = self.request.app[REDIS_PROVIDER].getall(self.request.app[REDIS_PROVIDER].ATTRIBUTE)
        return web.json_response(result)

    async def post(self):
        request_data = await self.request.json()
        redis_key = f'{self.request.app[REDIS_PROVIDER].ATTRIBUTE}/{request_data.get("id")}'
        self.request.app[REDIS_PROVIDER].set(redis_key, request_data)
        return web.json_response(request_data)
