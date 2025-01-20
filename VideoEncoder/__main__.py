import dns.resolver
from pyrogram import idle
from . import web_server, WEBHOOK
from aiohttp import web
from . import app, log

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']  # this is a google public dns


async def main():
    await app.start()
    if WEBHOOK:
            apps = web.AppRunner(await web_server())
            await apps.setup()       
            await web.TCPSite(apps, "0.0.0.0", 8080).start()     
            print(f"Webhook is running on port 8080")
    await app.send_message(chat_id=log, text=f'<b>Le bot est en marche !</b>')
    await idle()
    await app.stop()

app.loop.run_until_complete(main())
