import asyncio
from aiohttp import web


async def mikroservis_2(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})
        
app=web.Application()

app.router.add_get("/pozdrav", mikroservis_2)

web.run_app(app, host="localhost", port=8082)
