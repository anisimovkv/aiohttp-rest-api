import argparse
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

    return app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default="0.0.0.0")
    parser.add_argument('--port', type=int, default=4000)
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init(loop))
    web.run_app(app, host=args.host, port=args.port)


if __name__ == '__main__':
    main()
