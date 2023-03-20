from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(filters.command(["create"], "") & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"**Type** `.help create` **if you need help**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Man = await message.reply("`Processing...`")
    desc = "Welcome to my " + ("Group" if group_type == "group" else "Channel")
    if group_type == "group":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Successfully created a group: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Successfully created a channel: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        ["create channel", "Create A Channels"],
        ["create group", "Create A Groups"],
    ],
)
