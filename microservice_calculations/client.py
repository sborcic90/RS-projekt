import asyncio
import aiohttp

async def poziv_microservice_1():
    async with aiohttp.ClientSession() as session:
        # Osigurajte da se JSON pravilno šalje
        async with session.post("http://localhost:8083/zbroj", json={"brojevi": [1, 2, 3, 4, 5]}) as response:
            return await response.json()

async def poziv_microservice_2():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8084/umnozak", json={"brojevi": [2, 4, 6, 8, 10]}) as response:
            return await response.json()
     
async def poziv_microservice_3(umnozak, zbroj):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8085/kolicnik", json={"umnozak": umnozak, "zbroj": zbroj}) as response:
            return await response.json()
                  
async def main():
    #odgovor = await poziv_microservice_1()
    #print(odgovor)
    #odgovor1 = await poziv_microservice_2
    #print(odgovor1)
    odgovor_1, odgovor_2 = await asyncio.gather(poziv_microservice_1(), poziv_microservice_2())
    print(odgovor_1)
    print(odgovor_2)
    odgovor= await poziv_microservice_3(odgovor_2["umnozak"], odgovor_1["zbroj"])
    print(odgovor)
    
asyncio.run(main())