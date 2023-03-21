import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply
from Himiko.utils import extract_user

from .help import add_command_help


@Client.on_message(filters.command(["sg"], cmd) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.reply("Processing...")
    await lol.delete()
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.reply(f"`Provide the correct user.`")
    bot = "SangMata_BOT"
    try:
        await client.send_message(bot, f"/search_id {user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"/search_id {user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Names", limit=1):
        if not stalk:
            await message.reply_text("**This Person Has Never Changed His Name.**")
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()
          

add_command_help(
    "sangmata",
    [
        [
            f"sg <reply/userid/username>",
            "To Get Username History.",
        ],
    ],
)
