from aiohttp.web_response import Response
from aiohttp import hdrs


async def liveness(request):
    response = Response()
    response.text = 'fuck you cop, ama a dnb producer'
    response.headers[hdrs.ACCESS_CONTROL_ALLOW_ORIGIN] = request.headers.get(hdrs.ORIGIN)
    response.headers[hdrs.ACCESS_CONTROL_REQUEST_HEADERS] = 'apikey'
    response.headers[hdrs.ACCESS_CONTROL_ALLOW_METHODS] = 'GET'
    return response
