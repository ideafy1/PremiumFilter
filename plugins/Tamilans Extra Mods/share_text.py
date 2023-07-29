import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext",]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**𝗡𝗢𝗧𝗜𝗖𝗘:**\n\n1. REPLY TO ANY MESSAGE.\n2. NO MEDIA SUPPORT ﹝ SUPPORTS ONLY TEXT ﹞\n\n**𝘠𝘰𝘶'𝘭𝘭 𝘮𝘪𝘴𝘴 𝘢 𝘭𝘰𝘵, 𝘪𝘧 𝘺𝘰𝘶 𝘮𝘪𝘴𝘴 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 🤞**",                
            reply_to_message_id=reply_id,               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🙌 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 💥", url=f"https://t.me/yedekho_in")]])
            )                                                   
        return
    await message.reply_text(
        text=f"**𝗛𝗘𝗥𝗘 𝗜𝗦 𝗬𝗢𝗨𝗥 𝗦𝗛𝗔𝗥𝗜𝗡𝗚 𝗧𝗘𝗫𝗧 👇🏻**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_to_message_id=reply_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Sʜᴀʀᴇ ", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )
