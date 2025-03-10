import aiohttp
import asyncio
from aiohttp import web
import time

async def poziv_mikroservisa_1():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8081/pozdrav") as response:
            return await response.json()
      
async def poziv_mikroservisa_2():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8082/pozdrav") as response:
            return await response.json()
        
async def korutina(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:{port}{url}") as response:
            return await response.json()

async def main():
   početak=time.time()
   odgovor= await poziv_mikroservisa_1()
   print(odgovor)
   odgovor_2 = await poziv_mikroservisa_2()
   print(odgovor_2)
   završetak=time.time()
   početak1=time.time()
   odgovor3, odgovor4=await asyncio.gather(korutina("/pozdrav", 8081),  # Pozivanje mikroservisa 1
        korutina("/pozdrav", 8082))
   #odgovor_1, odgovor_2 = await asyncio.gather(poziv_mikroservis_1(), poziv_mikroservis_2()
    )
   završetak1=time.time()
   print(odgovor3)   
   print(odgovor4)
   print(f"{završetak-početak:.2f}s")
   print(f"{završetak1-početak1:.2f}s")

asyncio.run(main())