from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram.errors import MessageNotModified
from Himiko.helpers.basic import *
from Himiko.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER as cmd
from Himiko.core.ai import OpenAi
from Himiko.utils import *
from .help import add_command_help


OPENAI_API_KEY = "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"

@Client.on_message(filters.command(["cai"], "") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["ai"], "") & filters.me)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Type <code>.{message.command[0]} [question]</code> Question to use OpenAI")
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await message.reply("`Processing...`")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("There is an error!!\nYou have not entered OPENAI_API_KEY")
    
@Client.on_message(filters.command(["img"], "") & filters.me)
async def _(client, message):
    Tm = await message.reply("<code>Processing...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [query]</b>")
    try:
        response = OpenAi.Photo(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()
    
add_command_help(
    "openai",
    [
        ["ai [query]",
            "Generate or manipulate text"],
        ["img [query]",
            "Generate or manipulate images"],
    ],
)

add_command_help(
    "convert",
    [
        [
          f"toanime",
          "Convert media into an anime pictures"
          ],
         [
          f"toimg",
          "Convert to image conversion"
          ],
         [
          f"toaudio",
          "Convert mp4 to audio"
          ],
          [
          f"togif",
          "Convert media to gif"
          ],
    ],
)
