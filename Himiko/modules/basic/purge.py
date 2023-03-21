import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Himiko.helpers.adminHelpers import DEVS
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(
    filters.command("del", ["c"]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command(["del"], cmd) & filters.me)
async def del_msg(client: Client, message: Message):
    msg_src = message.reply_to_message
    if msg_src:
        if msg_src.from_user.id:
            try:
                await client.delete_messages(message.chat.id, msg_src.id)
                await message.delete()
            except BaseException:
                pass
    else:
        await message.delete()


@Client.on_message(
    filters.command("purge", ["c"]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command(["purge"], cmd) & filters.me)
async def purge(client: Client, message: Message):
    Man = await message.reply("Starting To Purge Messages.")
    msg = message.reply_to_message
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await Man.edit("`Reply To Message To Purge.`")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
            return

    done = await Man.edit(
        f"**Fast Purge Completed!**\n**Successfully Delete** `{str(count)}` **Message.**"
    )
    await asyncio.sleep(2)
    await done.delete()


@Client.on_message(
    filters.command("purgeme", ["c"]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command(["purgeme"], cmd) & filters.me)
async def purgeme(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await message.reply("Please enter a number.")
    n = int(n)
    if n < 1:
        return await message.reply("Enter the number of messages you want to delete.")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await message.reply("I can't find that message.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()


add_command_help(
    "purges",
    [
        ["del", "Delete messages, reply to messages"],
        ["purge", "Delete messages, reply to messages"],
        ["purgeme <number>", "Delete the number of your messages."],
    ],
)
