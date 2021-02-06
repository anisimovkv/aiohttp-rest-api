from aiohttp import web


async def get_list(request):
    return web.Response(text="Hello, world")
