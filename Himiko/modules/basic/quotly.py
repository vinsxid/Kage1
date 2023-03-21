import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.tools import get_arg
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(filters.me & filters.command(["q", "quotly"], cmd))
async def _(client, message):
    if message.reply_to_message:
        await client.unblock_user("@QuotLyBot")
        sg_m = await message.reply_to_message.forward("@QuotLyBot")
    else:
        if len(message.command) < 2:
            return await message.reply("Provide text or reply to the message.")
        else:
            await client.unblock_user("@QuotLyBot")
            sg_m = await client.send_message(
                "@QuotLyBot", message.text.split(None, 1)[1]
            )
    sg_i = await message.reply("<b>Processing....</b>")
    await sg_m.delete()
    await asyncio.sleep(6)
    async for msg in client.get_chat_history("@QuotLyBot", limit=1):
        if msg.sticker:
            dl = await msg.download()
            await sg_i.delete()
            await message.reply_sticker(dl)
        elif msg.text:
            await sg_i.delete()
            await message.reply("Failed to create a quote.")
        user_info = await client.resolve_peer("@QuotLyBot")
        await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))



add_command_help(
    "quotly",
    [
        [
            f"q/quotly <integer>",
            "Make messages into stickers.",
        ],
    ],
)
