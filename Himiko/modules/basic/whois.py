from asyncio import gather
from os import remove

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import ReplyCheck
from Himiko.utils import extract_user

from .help import add_command_help


@Client.on_message(filters.command(["whois", "info"], cmd) & filters.me)
async def who_is(client: Client, message: Message):
    user_id = await extract_user(message)
    ex = await message.edit_text("**Processing . . .**")
    if not user_id:
        return await ex.edit(
            "**Provide User ID/Username or Reply to get that user's info.**"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""<b>**USER INFORMATION**</b>
 <b>**User ID**:</b> <code>{user.id}</code>
 <b>**First Name**:</b> {first_name}
 <b>**Last Name**:</b> {last_name}
 <b>**Username**:</b> {username}
 <b>**DC ID**:</b> <code>{dc_id}</code>
 <b>**Verified**:</b> <code>{user.is_verified}</code>
 <b>**Premium**:</b> <code>{user.is_premium}</code>
 <b>**Same groups seen**:</b> {len(common)}
 <b>**Last Seen**:</b> <code>{status}</code>
 <b>**User permanent link**:</b> <a href='tg://user?id={user.id}'>{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                ex.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await ex.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await ex.edit(f"**INFO:** `{e}`")

add_command_help(
    "info",
    [
        ["info <username/userid/reply>",
        "Get user info with full description.",
       ],
    ],
)
