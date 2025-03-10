import aiohttp
import asyncio
from aiohttp import web

app =web.Application()

async def pozdrav(request):
    return web.json_response({"message" : "Hello from Microservice 1"})

app.router.add_get("/", pozdrav)
web.run_app(app, port=8081)