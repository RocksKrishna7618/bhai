from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AtiyaMusic import app
from AtiyaMusic.core.call import AtiyaMusic
from AtiyaMusic.utils.database import is_music_playing, music_on
from AtiyaMusic.utils.decorators import AdminRightsCheck
from AtiyaMusic.utils.inline.play import close_keyboard
from pyrogram.types import InputMediaPhoto

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await AtiyaMusic.resume_stream(chat_id)
    photo_url = "https://te.legra.ph/file/fe3a7d18884ab806d8a0f.jpg" # Replace with the URL of the photo you want to send
    caption = _["admin_4"].format(message.from_user.first_name)
    await message.reply_photo(
        photo=photo_url,
        caption=caption,
        reply_markup=close_keyboard,
    )
