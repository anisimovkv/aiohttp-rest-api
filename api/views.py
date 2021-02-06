from datetime import datetime, timedelta

from aiohttp import web
import jwt

from api.db import simple_db
from api.db import pass_db
from api.utils import login_required


async def get_list(request):
    # get all data
    json_data = simple_db
    return web.json_response({'list': json_data})


async def get_data(request):
    data_id = int(request.match_info['id'])
    try:
        data = simple_db[data_id]
    except IndexError:
        data = {"id": "None"}
    return web.json_response({'list': data})


@login_required
async def set_data(request):
    data = await request.json()
    simple_db.append(data)
    return web.json_response({'list': data, 'id': len(simple_db) - 1})


async def delete_data(request):
    data_id = int(request.match_info['id'])
    try:
        data = simple_db.pop(data_id)
    except IndexError:
        data = {"id": "None"}
    return web.json_response({'object was deleted:': data})


async def login(request):
    """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - Health check
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return "pong" text
            "405":
                description: invalid HTTP Method
    """
    data = await request.json()
    username = data.get('username', None)
    raw_password = data.get('password', None)

    pass_from_db = None
    data_db = None
    if username is not None:
        data_db = pass_db.get(username.lower(), None)
        pass_from_db = data_db.get('password', None)
    if pass_from_db is not None:
        if pass_from_db.lower() == raw_password.lower():
            encoded = jwt.encode(
                {"id": data_db['id']}, username, algorithm="HS256")
            return web.json_response({'token': encoded})

    return web.json_response(
        {'Error': 'Wrong username or password'}, status=400)
