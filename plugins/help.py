from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = """do you need help❤
    
1.🔹 <b> I can download the your Online class.</b> \n
2.🔹 <b> Go to your MBPU COLLEGE APP.</b> \n
3.🔹 <b> Copy the link of your video.</b> \n
4.🔹 <b> And paste it here.</b>   \n
5.🔹 <b> And I'll Upload It Into Telegram </b> \n \n <b>Made With Love By: @masterpice38 </b> 
             
             💕HAPPY LEARNING💕 </b>"""
    await message.reply_text(helptxt)
