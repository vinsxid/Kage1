from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

PREFIX = ["^", "?", "-", "+"]

cmd = [".", "?", "!", "("] # cmd custom


API_HASH = getenv("API_HASH", "e2432085a412bbc89e1d5bbcd72a7f0d")
API_ID = int(getenv("API_ID", "9317779"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001599474353, -1001473548283, -1001578091827, -1001687155877, -1001812143750, -1001704645461]
BLACKLIST_GCAST = list(
    map(
        int,
        getenv(
            "BLACKLIST_GCAST",
            "-1001599474353 -1001473548283 -1001578091827 -1001687155877 -1001812143750 -1001704645461",
        ).split(),
    )
)
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001599474353"))
BOT_VER = "2.1.5"
BRANCH = getenv("BRANCH", "master") #don't change
CMD_HANDLER = [".", "?", "!", "(", "-"]
CMD_HNDLR = [".", "?", "!", "(", "-"]
OWNER_ID = getenv("OWNER_ID", "1725671304")
BOT_TOKEN = getenv("BOT_TOKEN", "6138886907:AAHgrhiYq_xJYCE9c3C8baeASq3fuOSd-cU")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "diarydam")
DB_URL = getenv("DATABASE_URL", "postgres://mvedakyh:dIjsnpYu5cWqD_4Bkyjqi2r-MZTf4FQh@tyke.db.elephantsql.com/mvedakyh")
GIT_TOKEN = getenv("GIT_TOKEN", "")
        
GROUP = getenv("GROUP", "HimikoSupportChat")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
REPO_URL = getenv("REPO_URL", "https://github.com/d4msy/HimikoUbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQE2rfMApO37BeeLudbtb8BvSAwFUzXEWoO4-NtRlxBSoLYd7886sRQ_Vod_TDCnlK4EcZXomr23l__EYa0ijYZkEKg66JzFdUxMYKkTDIFp0zwLfIG31miqkXNRizW0J6MyAJQbGQdD-CJdhRlv8-j6QO7NoZDh7YmyYrgilvoOxiGSRtru8DmCs1ds_kXv8FS5hhxxQl17KLz24dsLSXyl0HN8D3yFIbjGbNc0_1pmeZgPGAj_ML3-7ZZqJQg8sRDxkOkxVD121HF_VEpaBbMiQ9U9s4sBOMHbiWWiq0ESNCrVzX2H2EEXQPMGfT_JoAcnBW0Fw5RrTrwiewBlgGZtf59RXwAAAABm26eIAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION16", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
STRING_SESSION21 = getenv("STRING_SESSION21", "")
STRING_SESSION22 = getenv("STRING_SESSION22", "")
STRING_SESSION23 = getenv("STRING_SESSION23", "")
STRING_SESSION24 = getenv("STRING_SESSION24", "")
STRING_SESSION25 = getenv("STRING_SESSION25", "")
STRING_SESSION26 = getenv("STRING_SESSION26", "")
STRING_SESSION27 = getenv("STRING_SESSION27", "")
STRING_SESSION28 = getenv("STRING_SESSION28", "")
STRING_SESSION29 = getenv("STRING_SESSION29", "")
STRING_SESSION30 = getenv("STRING_SESSION30", "")
STRING_SESSION31 = getenv("STRING_SESSION31", "")
STRING_SESSION32 = getenv("STRING_SESSION32", "")
STRING_SESSION33 = getenv("STRING_SESSION33", "")
STRING_SESSION34 = getenv("STRING_SESSION34", "")
STRING_SESSION35 = getenv("STRING_SESSION35", "")
STRING_SESSION36 = getenv("STRING_SESSION36", "")
STRING_SESSION37 = getenv("STRING_SESSION37", "")
STRING_SESSION38 = getenv("STRING_SESSION38", "")
STRING_SESSION39 = getenv("STRING_SESSION39", "")
STRING_SESSION40 = getenv("STRING_SESSION40", "")
STRING_SESSION41 = getenv("STRING_SESSION41", "")
STRING_SESSION42 = getenv("STRING_SESSION42", "")
STRING_SESSION43 = getenv("STRING_SESSION43", "")
STRING_SESSION44 = getenv("STRING_SESSION44", "")
STRING_SESSION45 = getenv("STRING_SESSION45", "")
STRING_SESSION46 = getenv("STRING_SESSION46", "")
STRING_SESSION47 = getenv("STRING_SESSION47", "")
STRING_SESSION48 = getenv("STRING_SESSION48", "")
STRING_SESSION49 = getenv("STRING_SESSION49", "")
STRING_SESSION50 = getenv("STRING_SESSION50", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
