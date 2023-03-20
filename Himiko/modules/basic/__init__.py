import os
import sys
from Himiko.modules.basic.help import add_command_help


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Himiko"])

async def join(client):
    try:
        await client.join_chat("HimikoSupportChat")
        await client.join_chat("diarydam")
        await client.join_chat("SharingUserbot")
    except BaseException:
        pass
