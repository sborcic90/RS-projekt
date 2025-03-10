import asyncio, aiohttp

async def fetch_service1():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8081') as response:
            return await response.json() 

async def fetch_service2():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8082') as response:
            return await response.json() 

async def main():
    print("Pokrećem main kourtinu!")
    konkurentno = await asyncio.gather(fetch_service1(), fetch_service2())
    #rezultat_prvog = await fetch_service1()
    #rezultat_drugog = await fetch_service2()
        
    #print(rezultat_prvog["message"], rezultat_drugog["message"])
    print(konkurentno)
    
asyncio.run(main())