from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_message(bot, message):
    b_msg = message.reply_to_message
    if not b_msg:
        await message.reply_text("Please reply to a message to broadcast.")
        return
    users = await db.get_all_users()
    total_users = await db.total_users_count()
    start_time = time.time()
    sent = 0
    failed = 0
    for user in users:
        user_id = int(user['id'])
        try:
            await b_msg.copy(user_id)
            sent += 1
        except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")
            failed += 1
        if sent % 20 == 0:
            await message.reply_text(f"Sent to {sent}/{total_users} users.")
        await asyncio.sleep(2)
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await message.reply_text(f"Broadcast completed in {time_taken}. Sent to {sent}/{total_users} users. Failed for {failed} users.")
