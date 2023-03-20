import asyncio
import os

from asyncio import sleep
from pyrogram import Client, enums, filters, raw
from pyrogram.types import Message

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from config import CMD_HANDLER as cmd
from Himiko import *
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import ReplyCheck
from Himiko.helpers.tools import get_arg
from Himiko.utils import s_paste

from .help import *


@Client.on_message(filters.command(["limited"], "") & filters.me)
async def _(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply("<code>Processing . . .</code>")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await msg.edit(status.text)
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))



@Client.on_message(filters.command(["webshot", "ss"], "") & filters.me)
async def webshot(client: Client, message: Message):
    Man = await message.reply("`Processing...`")
    try:
        user_link = message.command[1]
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        except Exception as dontload:
            await message.edit(f"Error! {dontload}\nTrying again create screenshot...")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        await Man.delete()
    except Exception as error:
        await Man.delete()
        await client.send_message(
            message.chat.id, f"**Something went wrong\nLog:{error}...**"
        )


@Client.on_message(filters.command(["type"], "") & filters.me)
async def types(client: Client, message: Message):
    orig_text = message.text.split(prefix + "type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while tbp != orig_text:
        await message.edit(str(tbp + typing_symbol))
        await asyncio.sleep(0.10)
        tbp = tbp + text[0]
        text = text[1:]
        await message.edit(str(tbp))
        await asyncio.sleep(0.10)


@Client.on_message(filters.command(["duck"], "") & filters.me)
async def duckgo(client: Client, message: Message):
    input_str = " ".join(message.command[1:])
    Man = await message.reply(message, "`Processing...`")
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await Man.edit_text(
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link)
        )
    else:
        await Man.edit_text("something is wrong. please try again later.")


@Client.on_message(filters.command(["open"], "") & filters.me)
async def open_file(client: Client, message: Message):
    xd = await message.reply("`Reading File!`")
    f = await client.download_media(message.reply)
    if f:
        _error = open(f, "r")
        _error_ = _error.read()
        _error.close()
        if len(_error_) >= 4096:
            await xd.edit("`Pasting to Spacebin!`")
            ext = "py"
            x = await s_paste(_error_, ext)
            s_link = x["url"]
            s_raw = x["raw"]
            pasted = f"**Pasted to Spacebin**\n**Link:** [Spacebin]({s_link})\n**Raw Link:** [Raw]({s_raw})"
            return await xd.edit(pasted, disable_web_page_preview=True)
        else:
            await xd.edit(f"**Output:**\n```{_error_}```")
    else:
        await edit_or_reply(m, "Balas ke File untuk membukanya!")
        os.remove(f)


@Client.on_message(filters.command(["ig", "ytb", "twitter", "fb", "tt"], "") & filters.me)
async def sosmed(client: Client, message: Message):
    Man = await message.reply("**Processing . . .**")
    link = get_arg(message)
    bot = "thisvidbot"
    if link:
        try:
            xnxx = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            xnxx = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
    async for sosmed in client.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            Man.delete(),
            client.send_video(
                message.chat.id,
                sosmed.video.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)



add_command_help(
    "misc",
    [
        ["limited", "Check you are limited or not."],
        ["duck", "To get Link from DuckDuckGo."],
        [
            "open",
            "To view the contents of the file as text which is sent as a telegram message.",
        ],
    ],
)


add_command_help(
    "webshot",
    [
        [
            f"webshot <link> `atau` ss <link>",
            "To screenshot a given web page.",
        ],
    ],
)


add_command_help(
    "sosmed",
    [
        [
            f"ig <link>",
            "To Download Media From Instagram.",
        ],
        [
            f"tt <link>",
            "To Download Media From Tiktok.",
        ],
        [
            f"ytb <link>",
            "To Download Media From YouTube.",
        ],
        [
            f"fb <link>",
            "To Download Media From Facebook.",
        ],
        [
            f"twitter <link>",
            "To Download Media From Twitter.",
        ],
    ],
)
