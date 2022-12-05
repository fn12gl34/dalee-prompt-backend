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
    aiohttp_app.on_startup.extend([init_routes])
    return aiohttp_app


async def init_routes(aiohttp_app: Application) -> None:
    aiohttp_app.router.add_view('/', AttributesView)
