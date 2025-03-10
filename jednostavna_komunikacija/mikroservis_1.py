import asyncio
from aiohttp import web


async def mikroservis_1(request):
    await asyncio.sleep(3)
    return web.json_response({"message": "Pozdrav nakon 3 sekunde"})
        
app=web.Application()

app.router.add_get("/pozdrav", mikroservis_1)

web.run_app(app, host="localhost", port=8081)

