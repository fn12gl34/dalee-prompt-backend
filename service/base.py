from aiohttp.web_app import Application
from aiohttp.web_routedef import get

from service.views.base import liveness
from service.redis_provider import RedisProvider
from service.constants import *
from service.views.attributes import AttributesView
from service.views.tags import TagsView
from service.views.schemas import SchemasView


def create_app() -> Application:
    aiohttp_app = Application()
    aiohttp_app[REDIS_PROVIDER]: RedisProvider = init_redis_provider()
    aiohttp_app.on_startup.extend([init_routes])
    return aiohttp_app


async def init_routes(aiohttp_app: Application) -> None:
    aiohttp_app.add_routes([get('/health/liveness', liveness)])
    aiohttp_app.router.add_view('/attributes', AttributesView)
    aiohttp_app.router.add_view('/tags', TagsView)
    aiohttp_app.router.add_view('/schema', SchemasView)


def init_redis_provider():
    return RedisProvider()
