# VideoEncoder - a telegram bot for compressing/encoding videos in h264/h265 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
