from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

PREFIX = ["^", "?", "-", "+"]

cmd = [".", "?", "!", "("] # cmd custom


API_HASH = getenv("API_HASH", "ed14750e0b09ba61089d8353fe4e9815")
API_ID = int(getenv("API_ID", "14814105"))
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
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001922757411"))
BOT_VER = "2.1.5"
BRANCH = getenv("BRANCH", "master") #don't change
CMD_HANDLER = [".", "?", "!", "(", "-"]
CMD_HNDLR = [".", "?", "!", "(", "-"]
OWNER_ID = getenv("OWNER_ID", "1557184285")
BOT_TOKEN = getenv("BOT_TOKEN", "6227436957:AAGU9X_GuR_l7Eawj2nzlsr_dUJsiK1Pt4I")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "kagestore69")
DB_URL = getenv("DATABASE_URL", "postgres://mvedakyh:dIjsnpYu5cWqD_4Bkyjqi2r-MZTf4FQh@tyke.db.elephantsql.com/mvedakyh")
GIT_TOKEN = getenv("GIT_TOKEN", "")
        
GROUP = getenv("GROUP", "userbotkage")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
REPO_URL = getenv("REPO_URL", "https://github.com/Rohidkage/Kage")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDiC5kASyy4pyG3qH_K2j7pUHKsPJ7icFZqw9iU757fyFTdAt4RGWpXF7ks76_3H9HTUI4yAiz4kOx6tT_XjZ7yAQwA-I7buceNZdXeE7XxHUoN0-i6vIg1FWkKJr9rtAAUrCTE3DpxK0Jz7q9bfuLjHMVYt7SZOqzAha3gOvCNrat5r4ZsnKPktL75nn7JX12HwpzlrN5lq4q3FZHe38KX3cTgvdGefrgo7rWD4susqBTvYTjQKojGdm0pzaNhHUw2mbBys3s5qH_Nf6gH0pjx1ttloKnaa_KtaX-dgkWJzQHMKg8xdUcSJFxk39TZLJtEPYtLSwz81L8YyqH68lvIiERmAgAAAABc0L8dAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQFBAKEAfZIvmhALRbXUsUF5ioXChziv3siyisaY6DBYApdOcc4jac3xuyJAJtk4u3RIrdHqNrlzsbUuFSDm9GInwr5h92TiBQOE3S6232V56Ug-EFGhg7LVgi3KRAL9_W6THReOpqLXIyAyE0Wcfj2zwqMXnhiUdVWF8Gmhweuy5j2J98X_YVQ79jKoDOcCDN4CxsYDmXmZx5Csfp_nUW1LYdsp-_0VPSYHzn99nDgNqDPqf4HbLGQBrAsaz7LflBQUN4stmLw2b21_V9VHEHzFPR1d_J5-XihK9VPTOtcsVLTJD2vFWkRXfycAAdLbg598_6EjLxpYpx1au8YLOf-o5U-LsAAAAABvpzMoAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQG0iGwALOEDukL7KPPUskNgIq5a4PUQYKa8BH45LRpGrMbPwvZVv7bopKIEV_5WI3mHkfsd3rd5Bq-9DOt-tSje7RoNaZ-ODTW0FWpSn3ff9DPXOMiaB_O4urRwzG4XU1oymbSnY9H1r2zzuZWndep83r3BI0YLJEk34KC1436CRymjkUVLqRyrvE_s5OpPfADNEdKO8Hp7ergx0fEhaCvstqSj61lATqGa5UmlyYch63d_vFA-UDRA5JE0vBRbYiaDeQJ5u8GIWDYz6tBckX67C1fOJkBZVwKA6c4Sllk8wtcQo_cpFGUAn84NhVK1ep7bNne-cAIGga_h_THUOeTSCWLPMAAAAAB6GShkAA")
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
