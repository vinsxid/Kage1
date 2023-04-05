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

OWNER_ID = [1557184285, 1725671304]

SUDO_ID = [1725671304, 1546078624]


@Client.on_message(filters.command(["alive"], cmd) & filters.me)
async def himiko_xnxx(client: Client, message: Message):
    bot_username = (await app.get_me()).username
    try:
        himiko = await client.get_inline_bot_results(bot=bot_username, query=f"alive {id(message)}")
        await asyncio.gather(
            client.send_inline_bot_result(
                message.chat.id, himiko.query_id, himiko.results[0].id, reply_to_message_id=message.id
            )
        )
    except Exception as e:
        await message.reply(e)
