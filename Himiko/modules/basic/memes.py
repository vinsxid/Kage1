import requests
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import get_text

from .help import *


@Client.on_message(filters.command(["trump"], cmd) & filters.me)
async def trump_tweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.reply(f"**Trump :** ``What Should I Tweet For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Trump Has Tweeted** {text}"
    await message.edit(f"**Trump:** Wait I Am Tweeting Your Text")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()


@Client.on_message(filters.command(["tweet"], cmd) & filters.me)
async def custom_tweet(client: Client, message: Message):
    text = get_text(message)
    input_str = get_text(message)
    if text:
        if ":" in text:
            stark = input_str.split(":", 1)
        else:
            await message.reply("**Usage:** `username:tweet-text`")
            return
    if len(stark) != 2:
        await message.edit("**Usage:** `username:tweet-text`")
        return

    starky = stark[0]
    ipman = stark[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={starky}&text={ipman}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**{starky} Has Tweeted** ``{ipman}``"
    await message.edit(f"**{starky}** : Wait I Am Tweeting Your Texts")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()
    
    
    
# credits Tomi Setiawan > @T0M1_X
@Client.on_message(filters.command(["memes"], cmd) & filters.me)
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply("<code>memes</code> [text]")
    text = f"#{random.randrange(67)} {message.text.split(None, 1)[1]}"
    x = await client.get_inline_bot_results("StickerizerBot", text)
    saved = await client.send_inline_bot_result(
        client.me.id, x.query_id, x.results[0].id
    )
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_sticker(
        message.chat.id, saved.sticker.file_id, reply_to_message_id=message.id
    )
    await saved.delete()



add_command_help(
    "memes",
    [
        ["trump", "make a Quote by Trump."],
        ["tweet", "Twitte by Ur values."],
        ["memes", "make a memes or meme"],
    ],
)
