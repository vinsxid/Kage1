import os
from asyncio import sleep
import sys
from re import sub

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import ReplyCheck
from Himiko.utils.misc import extract_user

from .help import add_command_help


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

@Client.on_message(
    filters.command(["unblock"], "") & (filters.me)
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Provide a username or reply to a message to unblock."
        )
    if user_id == client.me.id:
        return await tex.edit("Done.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Successfully unblocked** {umention}")


@Client.on_message(
    filters.command(["block"], "") & (filters.me)
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await tex.edit_text(
            "Give a username to blocked."
        )
    if user_id == client.me.id:
        return await tex.edit_text("Done.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Successfully Blocked** {umention}")


@Client.on_message(
    filters.command(["setname"], "") & (filters.me)
)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("Processing....")
    if len(message.command) == 1:
        return await tex.edit(
            "Provide text to set as your name."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**Successfully Changed Names To** `{name}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit(
            "Provide text to set as your name."
        )


@Client.on_message(
    filters.command(["setbio"], "") & (filters.me)
)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`Processing...`")
    if len(message.command) == 1:
        return await tex.edit("Provide text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**Successfully Changed Bio To** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit("Provide text to set as bio.")


@Client.on_message(
    filters.command(["setpfp"], "") & (filters.me)
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("Profile photo successfully changed.")
    else:
        await message.reply_text(
            "Reply to media to set as profile photo."
        )
        await sleep(3)
        await message.delete()


@Client.on_message(
    filters.command(["vpfp"], "") & (filters.me)
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.reply_text("No such photo profile.")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "profile",
    [
        ["block", "To block telegram users"],
        ["unblock", "To open the user you have blocked"],
        ["setname", "To Rename Telegram."],
        ["setbio", "To Change Telegram Bio."],
        [
            "setpfp",
            f"Reply To Image To Change Telegram Profile Photo.",
        ],
        ["vpfp", "To view the current user's profile photo."],
    ],
)
