import jwt
from aiohttp import web
from api.views import KEY
from api.db import pass_db


@web.middleware
async def auth_middleware(request, handler):
    user = request.headers.get('user', None)
    if user:
        id = pass_db[user]['id']
        jwt_token = request.headers.get('Authorization', None)
        if jwt_token:
            if jwt_token.startswith('Bearer '):
                jwt_token = jwt_token[7:]
                print(jwt_token)
                try:
                    decode = jwt.decode(jwt_token, KEY, algorithms="HS256")
                    print(decode)
                except (jwt.DecodeError, jwt.ExpiredSignatureError):
                    return web.json_response(
                        {'message': 'Token is invalid'}, status=400)
    return await handler(request)
