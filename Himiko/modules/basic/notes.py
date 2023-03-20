from asyncio import sleep
from pyrogram import Client, filters
from UbotSin.helpers.notes_sql import add_note, get_note, get_notes, rm_note
from pyrogram.types import Message

from Himiko.helpers.tools import get_arg
from config import CMD_HANDLER as cmd

from .help import add_command_help


@Client.on_message(filters.command(["notes"], "") & filters.me)
async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("No such note.")
    msg = f"List saved notes:\n"
    for note in notes:
        msg += f"- {note.keyword}\n"
    await message.reply(msg)


@Client.on_message(filters.command(["delete"], "") & filters.me)
async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(
            "No such note {}".format(notename)
        )
    return await message.reply("Delete note {} succesfully.".format(notename))

cmdb = [".", "*", "!", "?", "s"]

@Client.on_message(filters.command(["save"], "") & filters.me)
async def simpan_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("Reply to message.")
    anu = await msg.forward(client.me.id)
    msg_id = anu.id
    await client.send_message(client.me.id,
        f"Notes\nKeyword: {keyword}"
        "\n\nThe following messages are stored as log reply data for chats, please DON'T delete it.",
    )
    await sleep(1)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"**Saved note** {keyword}.")

cmdp = [".", "*", "!", "?", "g"]

@Client.on_message(filters.command(["get"], "") & filters.me)
async def panggil_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("No such note.")
    msg_o = await client.get_messages(client.me.id, int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)

add_command_help(
    "notes",
    [
        [f"save [note name or reply]", "Add a notes"],
        [f"get [note name]", "Get a notes"],
        [f"delete [note name]", "Delete a notes"],
        [f"notes", "Get all list notes"],
    ],
)
