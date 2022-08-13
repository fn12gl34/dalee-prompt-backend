from aiohttp.web_response import Response
from aiohttp import hdrs


async def liveness(request):
    return Response(text='fuck you cop')
