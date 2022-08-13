'''import os

from aiohttp import web

from service.base import create_app

if __name__ == '__main__':
    try:
        app = create_app()
        web.run_app(app, port=os.getenv('PORT'))
    except Exception as e:
        print('Unhandled exception in platform-restrictions-settings-service, error: %s', e)'''
import os

import aiohttp_cors
from aiohttp import web
from aiohttp.web_response import Response


async def t(_):
    return Response(text='hello')

app = web.Application()
app.router.add_get("/t", t)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=os.getenv('PORT'))