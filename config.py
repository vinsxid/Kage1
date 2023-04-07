from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

PREFIX = ["^", "?", "-", "+"]

cmd = [".", "-", "!", "("] # cmd custom


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
BOT_TOKEN = getenv("BOT_TOKEN", "6170088059:AAE_bwXtuaMKL_kqtnjfti5mcW1HxSgI1bE")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "kagestore69")
DB_URL = getenv("DATABASE_URL", "postgres://yyvynghu:MQmRAJ8K0hHq67YADVoapvWekPgNNZwj@jelani.db.elephantsql.com/yyvynghu")
GIT_TOKEN = getenv("GIT_TOKEN", "")
        
GROUP = getenv("GROUP", "userbotkage")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
REPO_URL = getenv("REPO_URL", "https://github.com/Rohidkage/Kage")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDiC5kAg-RyH-0rKdOj8ue1JjejzvlK6p3V7MwPDo01m4lxn6my-SO4I20MUH6jfQV62ty5dQta7xDztHRnEw51UNcxbTRAJxmlENKG8Bqu4d3ICImYt5WwOOhuCMOHJ6NrtR0xJkwbgC_izFQ97o3FAMhWOP4P1EI3QvHjubHXr_MzFuwZ6HxM5QoXUpL7t36rak_ssZiQ7H0dzxrbqc5rs73sQWjLqwtfcx44iXx8i6RREjiEOaJsRVez1Tonby929HfXfra5mtrjRCoW9fjBTee8D-XQGKNMxYUnQx4SMt5CLvX2BGeYaaYusHwA8psuH6Yt-oimK97chbz2oB19HshQSAAAAABc0L8dAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQFBAKEAfZIvmhALRbXUsUF5ioXChziv3siyisaY6DBYApdOcc4jac3xuyJAJtk4u3RIrdHqNrlzsbUuFSDm9GInwr5h92TiBQOE3S6232V56Ug-EFGhg7LVgi3KRAL9_W6THReOpqLXIyAyE0Wcfj2zwqMXnhiUdVWF8Gmhweuy5j2J98X_YVQ79jKoDOcCDN4CxsYDmXmZx5Csfp_nUW1LYdsp-_0VPSYHzn99nDgNqDPqf4HbLGQBrAsaz7LflBQUN4stmLw2b21_V9VHEHzFPR1d_J5-XihK9VPTOtcsVLTJD2vFWkRXfycAAdLbg598_6EjLxpYpx1au8YLOf-o5U-LsAAAAABvpzMoAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQG0iGwALOEDukL7KPPUskNgIq5a4PUQYKa8BH45LRpGrMbPwvZVv7bopKIEV_5WI3mHkfsd3rd5Bq-9DOt-tSje7RoNaZ-ODTW0FWpSn3ff9DPXOMiaB_O4urRwzG4XU1oymbSnY9H1r2zzuZWndep83r3BI0YLJEk34KC1436CRymjkUVLqRyrvE_s5OpPfADNEdKO8Hp7ergx0fEhaCvstqSj61lATqGa5UmlyYch63d_vFA-UDRA5JE0vBRbYiaDeQJ5u8GIWDYz6tBckX67C1fOJkBZVwKA6c4Sllk8wtcQo_cpFGUAn84NhVK1ep7bNne-cAIGga_h_THUOeTSCWLPMAAAAAB6GShkAA")
STRING_SESSION4 = getenv("STRING_SESSION4", "BQFTK-sAJn6EL6JoPCpN8LXXmQsgZKmcMNYeQIR0NBCHfKTAYUpqqprYJscoD0nYqMoEdgzg_o4Or20PQJpvtyy79uwj03dtaFnOchXpFq1NI6GLLmXJTMI9vAY4ZvKPMqvhKDn0luwJkcDIDEcBy0zyuUVRTZHc-c3JChI1Ly6G16bHnbpskUEr3TYsnGCzv9soFRSGyqAk5oFDognU4Jkd3dH0GbcxEgYSGWNy6Y5XtcBL7Aa4gtk1gXD6vslxGFDEEk9TAYaP_MMaduBEYOUBT9gU-g4vYQZWkW2ufvNB8vK3Ul4rbRBi9e61dDbvFoaalvcSOtTC5BqDldp5ZbecXTUt6AAAAABUIzIWAA")
STRING_SESSION5 = getenv("STRING_SESSION5", "BQGg6W0AeG2jIptd8diopVwlT42pK9c7Ee1WBmmzKo6Tp5oNpLPmELj6pdMAHZY7RQBJTeQ6jjdCFknnJ05Zh8l6QSwk2criru3d8SMzbv4IwiLjlzkHjkUaaED4MXU4UU8PRKZDPUIWC7M-yFMxMcs02jNTQZ9JjZ2HnlShohksoD-0qLhq5EFz50-9UNHNxAdupjg-AyyqTrPVm-us_IWZgHh4FTxQrs1kVy6j4WuLi1VVjggSPUkRc3d3EjAKVYbwxvP61wRCCnlVgOb0gic4Tnxfv5X3gDd6JNmaSdLLACy0Azw9-iA2EQgEDHrHjVxShb6FfBr29LNLyGq9ghECKHg1iAAAAAA-qgelAA")
STRING_SESSION6 = getenv("STRING_SESSION6", "BQFckqYAAOA3xyFypaQ3yGV79bKsspE4JhwncNaeRWTPTyzC1IcCECUJNOT7qQ5Rgb7AYTOb84--n3ig3e-kPlPUhXaPE6BDamiRTZqHLZV2Lw8MjnvtBXMfHoOJHJQOvuRjVdqR6NWsKfgs8z6JrUpvqCcQ5QOh9CaRDwxhdlWk7HVepXKv3MMsFaehr_uvmKyORMDp3ZXUqcRGKfS1hfhN5BI_VqpVLQAx1gxbbWLetu93Gy8cj0IKRWiTfOW5kQIgHykgtSQPEi-GXK7nPe4tud6CogAnIWGZeWperPM5_vK0WJ183ymkB2irGrDlBxEPT-WTUnqA8txScW_lb5ZrFqYtmQAAAABmMvYOAA")
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
