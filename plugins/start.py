from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel" , "Adding soon")],
        [InlineKeyboardButton("Report Bugs 😊", "Adding soon")]
        [InlineKeyboardButton("Owner" , url="https://t.me/masterpice38")],
    
    
    ])
    welcomed = f"Hi <b>{message.from_user.first_name}</b>\nI can download your online class</b>\nIf you don't know how to use me</b>\nThen type /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
