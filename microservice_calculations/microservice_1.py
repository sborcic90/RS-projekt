import asyncio
from aiohttp import web

async def microservice_1(request):
    try:
        data = await request.json()
        print(f"Primljeni podaci: {data}")  # Logiranje za provjeru

        # Provjera postoji li lista brojeva u JSON zahtjevu
        if "brojevi" not in data or not isinstance(data["brojevi"], list):
            return web.json_response({"error": "Proslijedite listu brojeva u JSON formatu."}, status=400)

        # Izračun zbroja brojeva
        total_sum = sum(data["brojevi"])

        return web.json_response({"zbroj": total_sum})
    
    except Exception as e:
        return web.json_response({"error": f"Greška u obradi zahtjeva: {str(e)}"}, status=500)

app = web.Application()
app.router.add_post("/zbroj", microservice_1)
web.run_app(app, host="localhost", port=8083)