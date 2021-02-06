from aiohttp import web


def login_required(func):
    async def wrapper(request):
        if not request.headers.get('user', None) \
                and not request.headers.get('Authorization', None):
            return web.json_response({'Error': 'Auth required'}, status=401)
        return await func(request)
    return wrapper
