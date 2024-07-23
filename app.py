from aiohttp import web
from loguru import logger
from peewee_async import Manager
from models import Device, ApiUser, Location, db
from playhouse.shortcuts import model_to_dict

logger.add("app.log", rotation="1 MB", retention="10 days", level="INFO")

objects = Manager(db)

async def create_device(request):
    try:
        data = await request.json()
        device = await objects.create(Device, **data)
        logger.info(f"Device created: {device.id}")
        return web.json_response({'id': device.id})
    except Exception as e:
        logger.error(f"Error creating device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def get_device(request):
    try:
        device_id = request.match_info.get('device_id')
        device = await objects.get(Device, Device.id == device_id)
        logger.info(f"Device retrieved: {device_id}")
        return web.json_response(model_to_dict(device))
    except Device.DoesNotExist:
        logger.error(f"Device not found: {device_id}")
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        logger.error(f"Error retrieving device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def update_device(request):
    try:
        device_id = request.match_info.get('device_id')
        data = await request.json()
        await objects.execute(Device.update(**data).where(Device.id == device_id))
        logger.info(f"Device updated: {device_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error updating device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def delete_device(request):
    try:
        device_id = request.match_info.get('device_id')
        await objects.execute(Device.delete().where(Device.id == device_id))
        logger.info(f"Device deleted: {device_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error deleting device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)
    
async def create_api_user(request):
    try:
        data = await request.json()
        user = await objects.create(ApiUser, **data)
        logger.info(f"ApiUser created: {user.id}")
        return web.json_response({'id': user.id})
    except Exception as e:
        logger.error(f"Error creating api user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def get_api_user(request):
    try:
        user_id = request.match_info.get('user_id')
        user = await objects.get(ApiUser, ApiUser.id == user_id)
        logger.info(f"ApiUser retrieved: {user_id}")
        return web.json_response(model_to_dict(user))
    except ApiUser.DoesNotExist:
        logger.error(f"ApiUser not found: {user_id}")
        return web.json_response({'error': 'ApiUser not found'}, status=404)
    except Exception as e:
        logger.error(f"Error retrieving api user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def update_api_user(request):
    try:
        user_id = request.match_info.get('user_id')
        data = await request.json()
        await objects.execute(ApiUser.update(**data).where(ApiUser.id == user_id))
        logger.info(f"ApiUser updated: {user_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error updating api user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def delete_api_user(request):
    try:
        user_id = request.match_info.get('user_id')
        await objects.execute(ApiUser.delete().where(ApiUser.id == user_id))
        logger.info(f"ApiUser deleted: {user_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error deleting api user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def create_location(request):
    try:
        data = await request.json()
        location = await objects.create(Location, **data)
        logger.info(f"Location created: {location.id}")
        return web.json_response({'id': location.id})
    except Exception as e:
        logger.error(f"Error creating location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def get_location(request):
    try:
        location_id = request.match_info.get('location_id')
        location = await objects.get(Location, Location.id == location_id)
        logger.info(f"Location retrieved: {location_id}")
        return web.json_response(model_to_dict(location))
    except Location.DoesNotExist:
        logger.error(f"Location not found: {location_id}")
        return web.json_response({'error': 'Location not found'}, status=404)
    except Exception as e:
        logger.error(f"Error retrieving location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def update_location(request):
    try:
        location_id = request.match_info.get('location_id')
        data = await request.json()
        await objects.execute(Location.update(**data).where(Location.id == location_id))
        logger.info(f"Location updated: {location_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error updating location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

async def delete_location(request):
    try:
        location_id = request.match_info.get('location_id')
        await objects.execute(Location.delete().where(Location.id == location_id))
        logger.info(f"Location deleted: {location_id}")
        return web.json_response({'status': 200})
    except Exception as e:
        logger.error(f"Error deleting location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)

app = web.Application()

app.router.add_post('/apiuser', create_api_user)
app.router.add_get('/apiuser/{user_id}', get_api_user)
app.router.add_put('/apiuser/{user_id}', update_api_user)
app.router.add_delete('/apiuser/{user_id}', delete_api_user)

app.router.add_post('/location', create_location)
app.router.add_get('/location/{location_id}', get_location)
app.router.add_put('/location/{location_id}', update_location)
app.router.add_delete('/location/{location_id}', delete_location)

app.router.add_post('/device', create_device)
app.router.add_get('/device/{device_id}', get_device)
app.router.add_put('/device/{device_id}', update_device)
app.router.add_delete('/device/{device_id}', delete_device)

if __name__ == "__main__":
    web.run_app(app, host='localhost', port=8080)