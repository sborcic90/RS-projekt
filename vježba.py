from aiohttp import web
import asyncio
from aiohttp.web import AppRunner
from aiohttp import ClientSession 

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]

lista_narudzbi= []

async def post_narudzba(request):
    data = await request.json()
    proizvod_id = int(data.get("proizvod_id"))
    kolicina = data.get("kolicina", 1)  
      
    for proizvod in proizvodi:
        if proizvod["id"] == proizvod_id:
            narudzba = {"proizvod_id": proizvod_id, "naziv": proizvod["naziv"], "kolicina": kolicina}
            lista_narudzbi.append(narudzba)
            return web.json_response(lista_narudzbi)
        
    return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"})
        
    
async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvodi_id(request):
    proizvod_id = request.match_info["id"]
    
    if not proizvod_id.isdigit():  # Provjera je li ID broj
        return web.json_response({"error": "Neispravan ID"}, status=400)

    proizvod_id = int(proizvod_id)
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)

    return web.json_response(proizvod if proizvod else {"error": "Proizvod s traženim ID-em ne postoji"}, status=200 if proizvod else 404)

app = web.Application()

app.router.add_get("/proizvodi", get_proizvodi)

app.router.add_get("/proizvodi/{id}", get_proizvodi_id)

app.router.add_post("/narudzbe", post_narudzba)

web.run_app(app,host="localhost", port=8081)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8081")
    
async def test_routes():
    """Testiranje API ruta kroz klijentsku sesiju."""
    async with ClientSession() as session:
        # Testiranje GET /proizvodi (dohvati sve proizvode)
        async with session.get("http://localhost:8081/proizvodi") as response:
            data = await response.json()
            print("Svi proizvodi:", data)

        # Testiranje GET /proizvodi/1 (dohvati proizvod s ID-em 1)
        async with session.get("http://localhost:8081/proizvodi/1") as response:
            data = await response.json()
            print("Proizvod 1:", data)
            
        async with session.post("http://localhost:8081/narudzbe", json={"proizvod_id": 2, "kolicina": 3}) as response:
            data = await response.json()
            print("Narudžba:", data)
            
async def main():
    await start_server()
    
    await test_routes()
    
asyncio.run(main())
    
"""async def get_users(requests):
    return web.json_response({"korisnici": ["Ivo", "Ana", "Marko", "Maja", "Iva", "Ivan "]})

app=web.Application()

app.router.add_get("/korisnici", get_users)

async def start_server():
    runner=AppRunner(app)
    await runner.setup()
    site=web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
        print("Klijentska sesija otvorena!")
        pass
            
asyncio.run(main())

korisnici = [
{'ime': 'Ivo', 'godine': 25},
{'ime': 'Ana', 'godine': 17},
{'ime': 'Marko', 'godine': 19},
{'ime': 'Maja', 'godine': 16},
{'ime': 'Iva', 'godine': 22}
]
    
async def get_korisnik(request):
    filtrirani=[korisnik for korisnik in korisnici if korisnik["godine"] >= 18]
    return web.json_response(filtrirani)
    print(filtrirani)
    
app = web.Application()
app.router.add_get("/punoljetan", get_korisnik)
                  
web.run_app(app, host="localhost", port=8082)

proizvodi = [
    {"naziv": "laptop", "cijena": 800, "količina": 10},
    {"naziv": "telefon", "cijena": 500, "količina": 25}
]
async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
  data = await request.json()
  print("Podaci primljeni",data)
  
  proizvodi.append(data)
  return web.json_response(proizvodi)

app = web.Application()

app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)
web.run_app(app,host="localhost", port=8081"""