import asyncio

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Himiko import app, CMD_HELP
from Himiko.helpers.cmd import *
from Himiko.helpers.PyroHelpers import ReplyCheck
from Himiko.helpers.utility import split_list


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)

cmdh = [".", "*", "!", "?", "h"]

@Client.on_message(filters.command(["help"], "") & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="helper")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            await message.reply(e)
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"**Help Menu For {str(help_arg).upper()}**\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "© @HimikoSupportChat"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
