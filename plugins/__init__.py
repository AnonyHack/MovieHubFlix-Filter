# Don't Remove Credit Tg - @Silando
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Freenethubtech
# Ask Doubt on telegram @Silando

# Clone Code Credit : YT - @Freenethubtech / TG - @Silando / GitHub - @Anony101

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
