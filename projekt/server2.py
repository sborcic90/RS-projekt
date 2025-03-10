from aiohttp import web
import aiohttp
import asyncio

asyncio def get(request):
    duljina=await idi_na_google()
    return web.json_response(data={"status":"OK"})

async def idi_na_google():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.google.com") as resp:
            return len(await resp.text())        
app=web.Application()
app.add_routes([web.get("/services", get)])

web.run_app(app )