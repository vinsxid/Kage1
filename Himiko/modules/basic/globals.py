from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from pyrogram import Client 
from pyrogram.enums import ChatType

from config import CMD_HANDLER as cmd
from Himiko import *
from Himiko.helpers.adminHelpers import DEVS, WHITELIST
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import get_ub_chats
from Himiko.utils import extract_user, extract_user_and_reason

from .help import add_command_help



@Client.on_message(
    filters.command("gban", ["c"]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.me & filters.command(["gban", "ungban"], ""))
async def _(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("Processing...")
    if not user_id:
        return await Tm.edit("<b>I can't find that user.</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = [
        "<b>Globally Ban</b>\n\n<b>Done in {} chats</b>\n<b>error in {} chat(s)</b>\n<b>User: <a href='tg://user?id={}'>{} {}</a></b>",
        "<b>Globally Unban</b>\n\n<b>Done in {} chats</b>\n<b>error in {} chat(s)</b>\n<b>User: <a href='tg://user?id={}'>{} {}</a></b>",
    ]
    if message.command[0] == "gban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == WHITELIST:
                    return await Tm.edit(
                        "I can't Globally Ban my developer."
                    )
                elif not user.id == WHITELIST:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await asyncio.sleep(0.1)
                    except:
                        failed += 1
                        await asyncio.sleep(0.1)
        await Tm.delete()
        return await message.reply(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "ungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
        await Tm.delete()
        return await message.reply(
            text[1].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "cgban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == 1725671304:
                    return await Tm.edit(
                        "I can't Globally Ban my developer."
                    )
                elif not user.id == WHITELIST:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await asyncio.sleep(0.1)
                    except:
                        failed += 1
                        await asyncio.sleep(0.1)
        await Tm.delete()
        return await message.reply(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    
add_command_help(
    "globals",
    [
        [
            "gban <reply/username/userid>",
            "Globally Ban An User",
        ],
        ["ungban <reply/username/userid>", "Globally Unban An User."],
    ],
)
