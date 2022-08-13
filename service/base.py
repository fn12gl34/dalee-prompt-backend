from aiohttp.web_app import Application
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS

from service.middlewares import authorization_middleware
from service.views.base import liveness
from service.redis_provider import RedisProvider
from service.constants import *
from service.views.attributes import AttributesView
from service.views.tags import TagsView
from service.views.schemas import SchemasView


def create_app() -> Application:
    aiohttp_app = Application()
    aiohttp_app[REDIS_PROVIDER]: RedisProvider = init_redis_provider()
    aiohttp_app.on_startup.extend([init_routes, init_middlewares])
    return aiohttp_app


async def init_routes(aiohttp_app: Application) -> None:
    aiohttp_app.router.add_view('/attributes', AttributesView)
    aiohttp_app.router.add_view('/tags', TagsView)
    aiohttp_app.router.add_view('/schema', SchemasView)
    aiohttp_app.router.add_route('GET', '/health/liveness', liveness)


def init_redis_provider():
    return RedisProvider()


async def init_middlewares(aiohttp_app: Application) -> None:
    aiohttp_app.middlewares.append(cors_middleware(allow_all=True, allow_headers=DEFAULT_ALLOW_HEADERS + ('apikey',)))
    aiohttp_app.middlewares.append(authorization_middleware)
