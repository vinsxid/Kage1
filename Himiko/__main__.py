import importlib
from pyrogram import idle
from uvloop import install


from Himiko.modules import ALL_MODULES
from Himiko import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Himiko.modules.basic import join
from pyrogram import __version__ as pyrover
from platform import python_version as y

BOT_VER = "7.2.5"
CMD_HANDLER = "2.0.100"
BOTLOG_CHAT = "-1001557500960"
MSG_BT = """
**Kage-Ubot Activated!**
   **Versi**: `{}`
   **Python**: `{}`
   **Pyrogram**: `{}`
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Himiko.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHAT, MSG_BOT.format(BOT_VER, y(), pyrover, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("KageUbot").info("Ubot Activated")
    install()
    LOOP.run_until_complete(main())
