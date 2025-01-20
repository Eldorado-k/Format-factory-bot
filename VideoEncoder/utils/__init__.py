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

from pyrogram import Client, filters
from pyrogram.errors import RPCError
from .. import LOGGER
from . import ( display_progress, ffmpeg, helper,
               settings, tasks) # direct_link_generator,

LOGGER.info('Imported Utils!')

sauce = '''<b>VideoEncoder - un bot Telegram pour compresser/encoder des vidéos au format H.264.</b>
Copyright (c) 2021 <a href='https://github.com/WeebTime/Video-Encoder-Bot'>WeebTime/Video-Encoder-Bot</a>
Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le modifier 
selon les termes de la licence GNU Affero General Public License publiée 
par la Free Software Foundation, soit la version 3 de la licence, soit 
(selon votre choix) toute version ultérieure.
Ce programme est distribué dans l'espoir qu'il sera utile, 
mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de 
QUALITÉ MARCHANDE ou D'ADÉQUATION À UN USAGE PARTICULIER. Voir la 
licence GNU Affero General Public License pour plus de détails.
Vous devriez avoir reçu une copie de la licence GNU Affero General Public License 
avec ce programme. Dans le cas contraire, consultez .'''


@Client.on_message(filters.command('so' 'ur' 'ce'))
async def g_s(_, message):
    try:
        await message.reply(text=sauce, reply_markup=helper.output, disable_web_page_preview=True)
    except RPCError:
        pass