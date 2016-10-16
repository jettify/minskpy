from django.http import HttpResponse

def my_view(request):
    r = requests.get('http://graph.facebook.com/v2.5/{uid}')
    data = r.json()
    # ...
    return HttpResponse(status=201)


from aiohttp import web

async def my_view(request):
    session = request.app['session']
    r = await session.get('http://graph.facebook.com/v2.5/{uid}')
    data = await r.json()

    return web.Response(status=201)
