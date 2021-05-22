from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"☆ This bot is made by AKASH GV"
               "☆ You can download all ONLINE CLASS"
               "☆ Just send me the link copied in MBPU COLLEGE APP"
    await message.reply_text(helptxt)
