from aiohttp import web
import json
import requests

"""data = {"ime" : "Ivo", "prezime" : "Ivić", "godine" : 25}

app = web.Application()

#def handler_function(request):
 #   print("Korisnik poslao zahtjev")
  #  return web.json_response(data) #serijaliziraj i pošalji http odg

async def dodaj_korisnika():
    body = await request.json()
    print("Dodan novi korisnik", body)
    return web.Response()

#
# app.router.add_get("/", handler_function)

app.router.add_post("/korisnici", dodaj_korisnika)

web.run_app(app, port=8080)"""

#Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na adresu http://localhost:8081/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
    
async def get_proizvodi(request):
  data={"naziv" : "laptop" , "cijena" : 800, "količina": 10}
  return web.json_response(data)

async def post_proizvodi():
  data = await request.json()
  print(data)
  return web.json_response(data)

app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)
web.run_app(app,host="localhost", port=8081)





