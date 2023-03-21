from base64 import b64decode
from io import BytesIO
from re import sub

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER as cmd


api_key = "WARYRD-YMKRHB-CZVXRU-WMVIAD-ARQ"


async def generate_sticker(messages):
    if not isinstance(messages, list):
        messages = [messages]
    headers = {"X-API-Key": api_key}
    payload = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#1b1429",
        "messages": [
            {
                "entities": [
                    {
                        "type": entity.type,
                        "offset": entity.offset,
                        "length": entity.length,
                    }
                    for entity in message.entities
                ]
                if message.entities
                else [],
                "chatId": message.forward_from.id
                if message.forward_from
                else message.from_user.id,
                "avatar": True,
                "from": {
                    "id": message.forward_from.id,
                    "username": message.forward_from.username or "",
                    "photo": {
                        "small_file_id": message.forward_from.photo.small_file_id,
                        "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                        "big_file_id": message.forward_from.photo.big_file_id,
                        "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                    }
                    if message.forward_from.photo
                    else "",
                    "name": f"{message.forward_from.first_name} {message.forward_from.last_name or ''}".rstrip(),
                }
                if message.forward_from
                else {
                    "id": message.from_user.id,
                    "username": message.from_user.username or "",
                    "photo": {
                        "small_file_id": message.from_user.photo.small_file_id,
                        "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
                        "big_file_id": message.from_user.photo.big_file_id,
                        "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
                    }
                    if message.from_user.photo
                    else "",
                    "name": f"{message.from_user.first_name} {message.from_user.last_name or ''}".rstrip(),
                },
                "text": message.text or "",
                "replyMessage": (
                    {
                        "name": f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''}".rstrip(),
                        "text": message.reply_to_message.text,
                        "chatId": message.reply_to_message.from_user.id,
                    }
                    if message.reply_to_message
                    else {}
                )
                if len(messages) == 1
                else {},
            }
            for message in messages
        ],
    }
    resp = requests.post(
        "https://arq.hamker.in/quotly",
        headers=headers,
        params={"payload": str(payload)},
    )
    resp = resp.json()
    if resp["ok"]:
        resp["result"] = b64decode(sub(r"data:image/png;base64,", "", resp["result"]))
        io_bytes = BytesIO(resp["result"])
        io_bytes.name = "sticker.webp"
        return io_bytes
    else:
        return None


@Client.on_message(filters.me & filters.command(["qq"], cmd))
async def quotly_handler(c, m: Message):
    cmd = m.command
    if not (r := m.reply_to_message) and not r.text:
        return await m.reply_text("Reply to a text message to quote it.")
    _q = await m.reply("Processing...")
    if len(cmd) <= 1:
        msg = [r]
    elif len(cmd) == 2:
        if cmd[1].isdigit():
            count = int(cmd[1])
            if 2 <= count <= 10:
                msg = await c.get_messages(
                    m.chat.id,
                    list(
                        range(
                            r.id,
                            r.id + count,
                        )
                    ),
                    replies=0,
                )
            else:
                return await m.reply_text("Count must be between 2 and 10.")
        else:
            msg = [await c.get_messages(m.chat.id, r.id, replies=1)]
    else:
        return await m.reply_text("Invalid command.")
    if not msg:
        await _q.delete()
        return await m.reply_text("No messages found.")
    sticker = generate_sticker(msg)
    if not sticker:
        await _q.delete()
        return await m.reply_text("Failed to generate sticker.")
    await m.reply_sticker(sticker)
    await m.delete()
    await _q.delete()
