import asyncio

from api.middlewares import auth_middleware
from aiohttp import web

from aiohttp_swagger import *

import api.routes


async def init(loop):
    # create aiohttp application
    app = web.Application()

    # register routes
    for route in api.routes.routes:
        app.router.add_route(*route)

    # Setup middlewares
    middlewares = [auth_middleware]
    app.middlewares.extend(middlewares)

    setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)

    host = "127.0.0.1"
    port = 4000

    return app, host, port


def main():
    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
