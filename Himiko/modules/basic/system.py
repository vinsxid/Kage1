import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from Himiko import app
from pyrogram import filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko import BOTLOG_CHATID, LOGGER
from Himiko.helpers.adminHelpers import DEVS
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help

HAPP = None


@app.on_message(filters.command("control") & filters.user(DEVS) & ~filters.via_bot
)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply("**Restarting bot...**")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot was restarted!**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Himiko"]
        execle(sys.executable, *args, environ)
