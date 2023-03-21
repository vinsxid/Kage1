from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Himiko.helpers.adminHelpers import DEVS
from config import BLACKLIST_CHAT
from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(filters.command("cjoin", cmd) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["join"], cmd) & filters.me)
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("`Processing...`")
    try:
        await xxnx.edit(f"Done Joined in Chat ID `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave", "kickme"], cmd) & filters.me)
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("**This command is not allowed to be used in this group**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group.")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], cmd) & filters.me)
async def kickmeall(client: Client, message: Message):
    Man = await message.reply("**Globally leave from group chats...**")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"Done out in {done} chats, error out in {er} chat(s)q"
    )


@Client.on_message(filters.command(["leaveallch"], cmd) & filters.me)
async def kickmeallch(client: Client, message: Message):
    Man = await message.reply("**Globally leave from group chats...**")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"Done out in {done} channsl, error out in {er} channel"
    )


add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "Leaved group.",
        ],
        ["leaveallgc", "Leave all groups you have joined."],
        ["leaveallch", "Leave all channels you have joined."],
        ["join @username", "To join the group via username."],
        ["leave @username", "To leave the group via username."],
    ],
)
