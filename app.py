import os

from aiohttp import web

from service.base import create_app

if __name__ == '__main__':
    try:
        app = create_app()
        web.run_app(app, port=os.getenv('PORT'))
    except Exception as e:
        print('Unhandled exception in dalee-prompt-backend, error: %s', e)
