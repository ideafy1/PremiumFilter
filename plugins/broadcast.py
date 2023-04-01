import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

@Client.on_message(filters.command('broadcast') & filters.private & filters.user("your_username_here"))
async def broadcast(client, message):
    try:
        sent = 0
        failed = 0
        chat_list = await client.get_dialogs()
        total = len(chat_list)
        for dialog in chat_list:
            try:
                if dialog.chat.type == "private":
                    await client.send_message(dialog.chat.id, message.text)
                    sent += 1
                    await asyncio.sleep(1)
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except Exception:
                failed += 1
        await message.reply_text(f"Message sent to {sent} chats. {failed} failed.")
    except Exception as e:
        print(e)
        await message.reply_text("An error occurred!")

