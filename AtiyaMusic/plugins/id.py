from AtiyaMusic import app
from strings import get_command
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID_COMMAND = get_command("ID_COMMAND")

@app.on_message(filters.command(ID_COMMAND)
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"**User {reply.from_user.first_name} ID is **: `{reply.from_user.id}`",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"**This chat's ID is**: `{message.chat.id}`",
           reply_markup=markup
        )
