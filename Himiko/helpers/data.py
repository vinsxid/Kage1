from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**Kage modules**\n  **Prefixes:** `. ( ? ! -`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
