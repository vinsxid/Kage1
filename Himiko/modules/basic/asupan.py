from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply
from Himiko.helpers.PyroHelpers import ReplyCheck
from Himiko import CMD_HELP, app 
from .help import add_command_help


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Searching...`")
    await gather(
        Man.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(filters.command(["ppanime", "anim"], cmd) & filters.me)
async def ppanime(client: Client, message: Message):
    yanto = await message.reply("`Processing...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Pp anime for you.",
    )

    await yanto.delete()

add_command_help(
    "asupan",
    [
        ["asupan or ptl",
            "Get tiktok videos randomly"],
        ["ppanime or anim",
            "Get random anime pp"],
    ],
)
