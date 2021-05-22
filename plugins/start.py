from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Source", url="https://github.com/X-Gorn/X-URL-Uploader"
                        ),
                        InlineKeyboardButton("Project Channel", url="https://t.me/xTeamBots"),
                    ],
                    [InlineKeyboardButton("Author", url="https://t.me/xgorn")],
                ]
            ),
    welcomed = """Hi <b>{message.from_user.first_name}I can download your online class</b>\n If you don't know how to use me</b>\n Then type /help"""
    await message.reply_text welcomed, (reply_markup)=joinButton
    raise StopPropagation
