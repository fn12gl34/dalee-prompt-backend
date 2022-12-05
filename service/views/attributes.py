from aiohttp import web
from service.constants import *


class AttributesView(web.View):

    async def post(self):
        request_data = await self.request.json()
        print(request_data)
        return web.json_response(request_data)
