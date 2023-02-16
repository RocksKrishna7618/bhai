from AtiyaMusic import app
from pyrogram import filters
from config import OWNER_ID

@app.on_message(filters.command("test"))
def tests(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"💔 ᴏᴡɴᴇʀs:\n1➤ {OWNER_ID}"
        )
