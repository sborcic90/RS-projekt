# microservice_3.py
import asyncio
from aiohttp import web

async def kolicnik(request):
    data = await request.json()

    if "umnozak" not in data or "zbroj" not in data:
        return web.json_response({"error": "Proslijedite umnožak i zbroj u JSON formatu."}, status=400)

    # Provjera dijeljenja s nulom
    if data["zbroj"] == 0:
        return web.json_response({"error": "Zbroj ne može biti 0, ne možete dijeliti s nulom."}, status=400)

    # Izračun količnika
    result = data["umnozak"] / data["zbroj"]

    return web.json_response({"kolicnik": result})

app = web.Application()
app.router.add_post("/kolicnik", kolicnik)
web.run_app(app, host="localhost", port=8085)
