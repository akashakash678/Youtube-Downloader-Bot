from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/testytbotchannel")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/masterpice38")],
        [InlineKeyboardButton("Made by💕", url="https://t.me/masterpice38")]
    ])
    welcomed = f"""Hi <b>{message.from_user.first_name}</b> 
 
IMPORTANT NOTE FOR OTGER USERS (except MBPU students)
This bot is only made for MBPU students

If  you want to use then plz contact my owner @masterpice38

Dear <b>{message.from_user.first_name}</b> plz join our channel and group

I can download your online class videos.

/help for More info
    
    
💕HAPPY LEARNING💕
   
   
    https://telegra.ph/file/590aa8344b6642bfa8478.jpg"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
