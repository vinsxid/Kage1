import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict


from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client
from pytgcalls import GroupCallFactory


from config import (
    API_HASH,
    API_ID,
    DB_URL,
    BOTLOG_CHATID,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10,
    STRING_SESSION11,
    STRING_SESSION12,
    STRING_SESSION13,
    STRING_SESSION14,
    STRING_SESSION15,
    STRING_SESSION16,
    STRING_SESSION17,
    STRING_SESSION18,
    STRING_SESSION19,
    STRING_SESSION20,
    STRING_SESSION21,
    STRING_SESSION22,
    STRING_SESSION23,
    STRING_SESSION24,
    STRING_SESSION25,
    STRING_SESSION26,
    STRING_SESSION27,
    STRING_SESSION28,
    STRING_SESSION29,
    STRING_SESSION30,
    STRING_SESSION31,
    STRING_SESSION32,
    STRING_SESSION33,
    STRING_SESSION34,
    STRING_SESSION35,
    STRING_SESSION36,
    STRING_SESSION37,
    STRING_SESSION38,
    STRING_SESSION39,
    STRING_SESSION40,
    STRING_SESSION41,
    STRING_SESSION42,
    STRING_SESSION43,
    STRING_SESSION44,
    STRING_SESSION45,
    STRING_SESSION46,
    STRING_SESSION47,
    STRING_SESSION48,
    STRING_SESSION49,
    STRING_SESSION50,
    SUDO_USERS,
    BOT_TOKEN,
    GIT_TOKEN
)
DATABASE_URL = DB_URL
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []
LOG_FILE_NAME = "Himiko.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)


LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


if (
    not STRING_SESSION1
    and not STRING_SESSION2
    and not STRING_SESSION3
    and not STRING_SESSION4
    and not STRING_SESSION5
):
    LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
    sys.exit()

if API_ID:
   API_ID = API_ID
else:
   LOGGER(__name__).warning("WARNING: MEMULAI BOT TANPA API ID")
   API_ID = "9317779"

if API_HASH:
   API_HASH = API_HASH
else:
   LOGGER(__name__).warning("WARNING: MEMULAI BOT TANPA API HASH")   
   API_HASH = "e2432085a412bbc89e1d5bbcd72a7f0d"

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit

if BOTLOG_CHATID:
   BOTLOG_CHATID = BOTLOG_CHATID
else:
   BOTLOG_CHATID = "me"

LOOP = asyncio.get_event_loop()

trl = Translator()

aiosession = ClientSession()

CMD_HELP = {}

scheduler = AsyncIOScheduler()

StartTime = time.time()

START_TIME = datetime.now()

TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Himiko/modules"),
    in_memory=True,
)

bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION1,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION2,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION3,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION4,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION5,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION5
    else None
)

bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION6,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION6
    else None
)

bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION7,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION7
    else None
)

bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION8,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION8
    else None
)

bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION9,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION9
    else None
)

bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION10,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION10
    else None
)

bot11 = (
    Client(
        name="bot11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION11,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION11
    else None
)

bot12 = (
    Client(
        name="bot12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION12,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION12
    else None
)

bot13 = (
    Client(
        name="bot13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION13,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION13
    else None
)

bot14 = (
    Client(
        name="bot14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION14,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION4
    else None
)

bot15 = (
    Client(
        name="bot15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION15,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION15
    else None
)

bot16 = (
    Client(
        name="bot16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION16,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION16
    else None
)

bot17 = (
    Client(
        name="bot17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION17,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION17
    else None
)

bot18 = (
    Client(
        name="bot18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION18,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION18
    else None
)

bot19 = (
    Client(
        name="bot19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION19,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION19
    else None
)

bot20 = (
    Client(
        name="bot20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION20,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION20
    else None
)
bot21 = (
    Client(
        name="bot21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION21,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION21
    else None
)

bot22 = (
    Client(
        name="bot22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION22,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION22
    else None
)

bot23 = (
    Client(
        name="bot23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION23,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION23
    else None
)

bot24 = (
    Client(
        name="bot24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION24,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION24
    else None
)

bot25 = (
    Client(
        name="bot25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION25,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION25
    else None
)

bot26 = (
    Client(
        name="bot26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION26,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION26
    else None
)

bot27 = (
    Client(
        name="bot27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION27,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION27
    else None
)

bot28 = (
    Client(
        name="bot28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION28,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION28
    else None
)

bot29 = (
    Client(
        name="bot29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION29,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION29
    else None
)

bot30 = (
    Client(
        name="bot30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION30,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION30
    else None
)

bot31 = (
    Client(
        name="bot31",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION31,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION31
    else None
)

bot32 = (
    Client(
        name="bot32",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION32,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION32
    else None
)

bot33 = (
    Client(
        name="bot33",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION33,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION33
    else None
)

bot34 = (
    Client(
        name="bot34",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION34,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION34
    else None
)

bot35 = (
    Client(
        name="bot35",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION35,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION35
    else None
)

bot36 = (
    Client(
        name="bot36",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION36,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION36
    else None
)

bot37 = (
    Client(
        name="bot37",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION37,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION37
    else None
)

bot38 = (
    Client(
        name="bot38",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION38,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION38
    else None
)

bot39 = (
    Client(
        name="bot39",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION39,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION39
    else None
)

bot40 = (
    Client(
        name="bot40",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION40,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION40
    else None
)

bot41 = (
    Client(
        name="bot41",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION41,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION41
    else None
)

bot42 = (
    Client(
        name="bot42",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION42,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION42
    else None
)

bot43 = (
    Client(
        name="bot43",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION43,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION43
    else None
)

bot44 = (
    Client(
        name="bot44",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION44,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION44
    else None
)

bot45 = (
    Client(
        name="bot45",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION45,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION45
    else None
)
bot46 = (
    Client(
        name="bot46",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION46,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION46
    else None
)

bot47 = (
    Client(
        name="bot47",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION47,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION47
    else None
)

bot48 = (
    Client(
        name="bot48",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION48,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION48
    else None
)

bot49 = (
    Client(
        name="bot49",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION49,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION49
    else None
)

bot50 = (
    Client(
        name="bot50",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION50,
        plugins=dict(root="Himiko/modules"),
    )
    if STRING_SESSION50
    else None
)

bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30, bot31, bot32, bot33, bot34, bot35, bot36, bot37, bot38, bot39, bot40, bot41, bot42, bot43, bot44, bot45, bot46, bot47, bot48, bot49, bot50] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
