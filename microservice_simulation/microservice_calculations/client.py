import asyncio, aiohttp

async def microservice_sum(brojevi):
    async with aiohttp.ClientSession() as session:
        rezultat = await session.post("http://localhost:8081/zbroj",json=brojevi)
        return await rezultat.json()
    
async def microservice_ratio(brojevi, zbroj):
    async with aiohttp.ClientSession() as session:
        tijelo_zahtjeva = {"brojevi": brojevi, "zbroj": zbroj}  
        rezultat = await session.post("http://localhost:8082/ratio",json=tijelo_zahtjeva)
        return await rezultat.json()
async def main():
    brojevi = [i for i in range(1,11)]

    odgovor_sum = await microservice_sum({"brojevi": brojevi})


    odgovor_ratio= await microservice_ratio(brojevi, odgovor_sum["zbroj"])

    print(odgovor_ratio)


asyncio.run(main())