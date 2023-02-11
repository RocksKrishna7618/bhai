import asyncio

from AtiyaMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import BOT_NAME

@app.on_message(filters.command(["alive"]) & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2b1f1ea263f7092937d1f.jpg",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {BOT_NAME}\n━━━━━━━━━━━━━━━━━━\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━\n❄ ᴍʏ ᴏᴡɴᴇʀ : [˹ᴋʀɪsʜɴᴀ˼](https://t.me/itz_rocks_krishna)\n🌸 ᴀʙᴏᴜᴛ ᴍᴇ  : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/incorrect_krishna)\n❤‍🔥 ᴍᴇᴇᴛ ᴍᴇ    : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/frienddd_zoneee\n━━━━━━━━━━━━━━━━━━)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
    )
