from aiohttp import web

async def zbroj_brojeva_lista(request):
    tijelo_zahtjeva = await request.json()
    
    brojevi=tijelo_zahtjeva.get("brojevi")
    zbroj=sum(brojevi)
    print(tijelo_zahtjeva)
    return web.json_response({"zbroj": zbroj})
                             
app = web.Application()

app.router.add_post("/zbroj", zbroj_brojeva_lista)

web.run_app(app, host="localhost", port=8081)