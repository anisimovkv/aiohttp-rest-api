from aiohttp import web

from app import simple_db


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
