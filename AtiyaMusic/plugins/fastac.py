import asyncio
import math
import os
import shutil
import socket
import traceback
import psutil
import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from pyrogram.types import Message
from AtiyaMusic import app
from AtiyaMusic.utils.database.memorydatabase import (active, activevideo)
from AtiyaMusic.misc import SUDOERS
from AtiyaMusic.utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#


LOGINGG = config.LOGGER_ID


#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
    await message.reply_text(f"乛 𝘽𝙤𝙩'𝙨 𝘼𝙘𝙩𝙞𝙫𝙚 𝙘𝙝𝙖𝙩'𝙨 𝙄𝙣𝙛𝙤 »\n°──────❅────────°\n❄ ᴀᴄᴛɪᴠᴇ ᴀᴜᴅɪᴏ : {ac_audio}\n°──────────°\n💫 ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ  : {ac_video}\n°──────────°\n",quote=True, reply_markup=reply_markup)
    

#--------------------------Clean_Commands------------------------#

@app.on_message(avoice(["/rm"]) & SUDOERS)
async def cleaning(client: Client, message: Message):
    A = 'rm -rf downloads'
    try:
        os.system(A)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Downloads", quote=True)

    
CPU_LOAD = psutil.cpu_percent(interval=0.5)
RAM_LOAD = psutil.virtual_memory().percent
DISK_SPACE = psutil.disk_usage("/").percent
