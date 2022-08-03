from aiohttp.web_response import Response


async def liveness(_):
    return Response(text='fuck you cop, ama a dnb producer')
