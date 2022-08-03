from aiohttp.web_app import Application
from aiohttp.web_routedef import get

from service.views.base import liveness


def create_app() -> Application:
    aiohttp_app = Application()
    aiohttp_app.on_startup.extend([init_routes])
    return aiohttp_app


async def init_routes(aiohttp_app: Application) -> None:
    aiohttp_app.add_routes([get('/health/liveness', liveness)])
