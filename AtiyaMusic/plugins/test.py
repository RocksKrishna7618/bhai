imimport asyncio

from AtiyaMusic import app
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message

@app.on_message(filters.command(["test"]) & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_text(
        text=f"💔 ᴏᴡɴᴇʀs:\n1➤ [˹ᴋʀɪsʜɴᴀ˼](https://t.me/itz_rocks_krishna)",
    )
