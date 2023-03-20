import time
import random
import speedtest
import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime
from Himiko.helpers.adminHelpers import DEVS
from Himiko import *
from Himiko.utils import get_readable_time
from Himiko.utils.misc import *
from Himiko.utils.tools import *
from Himiko.modules.bot.inline import *
from Himiko import *
from Himiko.modules.basic import *

from .help import add_command_help

modules = CMD_HELP

cmds = [".", "*", "!", "?", "p"]

@Client.on_message(
    filters.command("ping", ["c"]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], "") & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"**Pong!**\n`%sms`\n" % (duration)
        )
    await ping_.delete()
