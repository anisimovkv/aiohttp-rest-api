import jwt
from aiohttp import web


@web.middleware
async def auth_middleware(request, handler):
    user = request.headers.get('user', None)
    if user:
        jwt_token = request.headers.get('Authorization', None)
        if jwt_token:
            if jwt_token.startswith('Bearer '):
                jwt_token = jwt_token[7:]
            try:
                decode = jwt.decode(
                    jwt_token, user.lower(), algorithms="HS256")
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return web.json_response(
                    {'message': 'Token is invalid'}, status=400)
    return await handler(request)
