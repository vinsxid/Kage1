import time
import asyncio
import os
from gc import get_objects
from datetime import datetime

from config import CMD_HANDLER as cmd
from pyrogram import Client, enums, filters
from pyrogram.types import *


from Himiko import CMD_HELP, StartTime, app, ids
from pyrogram.raw.functions import Ping
from Himiko.utils import get_readable_time
from pyrogram import *
from config import *
from Himiko import *

WHITE = [1557184285]

BLACK = [1725671304, 1546078624]


@Client.on_message(filters.command(["alive"], cmd) & filters.me)
async def dam_xnxx(client: Client, message: Message):
    bot_username = (await app.get_me()).username
    try:
        dam = await client.get_inline_bot_results(bot=bot_username, query=f"alive {id(message)}")
        await asyncio.gather(
            client.send_inline_bot_result(
                message.chat.id, dam.query_id, dam.results[0].id, reply_to_message_id=message.id
            )
        )
    except Exception as e:
        await message.reply(e)
