from Himiko import app
import os
import time
import re
import asyncio
import math
import shutil
import sys
from pyrogram import Client, enums, filters
from os import environ, execle, path
from Himiko import *
from Himiko.utils.misc import *
from pyrogram import *
from platform import python_version as py
from pyrogram import __version__ as pyro
from pyrogram.types import * 
from config import *
from Himiko import ids

ADMIN1 = [1725671304]
ADMIN2 = [1557184285]
APP_VERSION = "7.0.0"


@app.on_message(filters.command(["alive"]))
async def module_help(client: Client, message: Message):
    served_users = len(ids)
    await message.reply_text(
      f"""
 **Kage-Ubot**
   **Status** : **ROBOT**
     **Users** : `{served_users}`
     **Versi** : `{APP_VERSION}`
     **Python** : `{py()}`
     **Pyrogram** : `{pyro}`
""",
    reply_markup=InlineKeyboardMarkup(
      [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ​", url=f"https://t.me/userbotkage"),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/kagestore69"),
        ],
      ]
      ),
      disable_web_page_preview=True,
    )

@app.on_message(filters.command(["start"]) & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 **Hallo {message.from_user.first_name}** \n
💭 **Is there anything I can help? **
💡 **If you want to make a bot\nYou can Contact @KageBunshiiin.**
</b>""",
    )
