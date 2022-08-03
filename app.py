import logging

from aiohttp import web

from service.base import create_app

if __name__ == '__main__':
    try:
        app = create_app()
        web.run_app(app)
    except Exception as e:
        print('Unhandled exception in platform-restrictions-settings-service, error: %s', e)