from aiohttp import web


@web.middleware
async def authorization_middleware(request: web.Request, handler) -> web.Response:
    apikey = request.headers.get('apikey')
    if apikey:
        if apikey == 'i_love_big_black_cocks':
            return await handler(request)
    return web.Response(text='ты проебал апикей в запроссе братишка')
