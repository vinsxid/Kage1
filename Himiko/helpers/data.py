from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**Help modules**\n  **Prefixes:** `. ( ? ! -`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
