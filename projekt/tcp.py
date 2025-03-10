import asyncio

async def handler(reader, writer):
    print("Nova konekcija!")
    pass
      
async def main():
    server= await asyncio.start_server(
        handler,
        "127.0.0.1", 8080
        )
    
    async with server:
        print("Server pokrenut!")
        await server.serve_forever()
    
    
    """print("Here")
    pass"""

asyncio.run(main())     #instanca korutine - funkcija koja je asinkrona