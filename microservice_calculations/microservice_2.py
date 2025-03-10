import asyncio
from aiohttp import web

"""Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. Na endpointu
/umnozak neka vraća JSON odgovor s umnoškom svih brojeva. Dodajte provjeru ako brojevi nisu
proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod."""

async def umnozak(request):
    data = await request.json()
    if 'brojevi' not in data:
        return web.json_response({'error': 'Nisu proslijeđeni brojevi'}, status=400)
    brojevi = data['brojevi']
    umnozak = 1
    for broj in brojevi:
        umnozak *= broj
        if not isinstance(broj, (int, float)):
            return web.json_response({'error': 'Svi brojevi moraju biti numerički'}, status=400)
    return web.json_response({'umnozak': umnozak})

app = web.Application()

app.add_routes([web.post('/umnozak', umnozak)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8084)
    
    