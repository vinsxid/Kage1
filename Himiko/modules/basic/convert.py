import os
import asyncio
import time
from pyrogram import Client, filters, enums
from pyrogram.types import *
from pyrogram.raw.functions.messages import DeleteHistory
from config import CMD_HANDLER as cmd
from Himiko.helpers.tools import run_cmd
from Himiko.modules.basic import add_command_help


@Client.on_message(filters.command(["toanime"], "") & filters.me)
async def convert_image(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("`Reply to photo to turn into anime.`")
    bot = "qq_neural_anime_bot"
    if message.reply_to_message:
        HUNTER = await message.reply("`Processing...`")
        await client.unblock_user(bot)
        AA = await message.reply_to_message.forward(bot)
        await asyncio.sleep(30)
        await AA.delete()
        await HUNTER.delete()
        get_photo = []
        async for Toanime in client.search_messages(
            bot, filter=enums.MessagesFilter.PHOTO
        ):
            get_photo.append(InputMediaPhoto(Toanime.photo.file_id))
        await client.send_media_group(
            message.chat.id,
            media=get_photo,
            reply_to_message_id=message.id,
        )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))

@Client.on_message(filters.command(["toaudio"], "") & filters.me)
async def extract_all_aud(client: Client, message: Message):
    replied_msg = message.reply_to_message
    geez = await message.reply("`Downloading...`")
    ext_out_path = os.getcwd() + "/" + "basic/py_extract/audios"
    if not replied_msg:
        await geez.edit("`Please Reply To Video.`")
        return
    if not replied_msg.video:
        await geez.edit("`Please Reply To Video.`")
        return
    if os.path.exists(ext_out_path):
        await geez.edit("Processing.....")
        return
    replied_video = replied_msg.video
    try:
        await geez.edit("`Downloading...`")
        ext_video = await client.download_media(message=replied_video)
        await geez.edit("`Extracting Audio(s)...`")
        exted_aud = Video_tools.extract_all_audio(input_file=ext_video, output_path=ext_out_path)
        await geez.edit("`Uploading...`")
        for nexa_aud in exted_aud:
            await message.reply_audio(audio=nexa_aud, caption=f"`Extracted by` {(await client.get_me()).mention}")
        await geez.edit("`Extracting Finished!`")
        shutil.rmtree(ext_out_path)
    except Exception as e:
        await geez.edit(f"**Error:** `{e}`")
       
          
@Client.on_message(filters.command(["togif"], "") & filters.me)
async def togif(client: Client, message: Message):
    TM = await message.reply("<b>Processing...</b>")
    if not message.reply_to_message:
        return await TM.edit("<b>Reply to Sticker...</b>")
    await TM.edit("<b>Downloading...</b>")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_Tomi_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except Exception as error:
        await TM.edit(error)
