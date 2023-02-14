
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import *

from AtiyaMusic import app, userbot
from config import OWNER_ID

USER_ONE = userbot.one
USER_TWO = userbot.two
USER_THREE = userbot.three 
USER_FOUR = userbot.four 
USER_FIVE = userbot.five 

@app.on_message(filters.command(["setpfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
		img = await message.reply_to_message.download()
		try:
			await USER_ONE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
		except:
			return await replytext.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢɪɴɢ ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	else:
		await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")

@app.on_message(filters.command(["setpfp2"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
		img = await message.reply_to_message.download()
		try:
			await USER_TWO.set_profile_photo(photo=img)
			return await replytext.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ 2.")
		except:
			return await replytext.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢɪɴɢ ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
	else:
		await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["setpfp3"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
		img = await message.reply_to_message.download()
		try:
			await USER_THREE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ 3.")
		except:
			return await replytext.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
	else:
		await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["setpfp4"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
		img = await message.reply_to_message.download()
		try:
			await USER_FOUR.set_profile_photo(photo=img)
			return await replytext.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ 4.")
		except:
			return await replytext.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
	else:
		await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["setpfp5"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
		img = await message.reply_to_message.download()
		try:
			await USER_FIVE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄ 5.")
		except:
			return await replytext.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
	else:
		await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["delpfp"]) & filters.user(OWNER_ID))
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_ONE.get_chat_photos("me")]
		await USER_ONE.delete_profile_photo(pfp[0].file_id)
		return await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	except Exception:
		await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["delpfp2"]) & filters.user(OWNER_ID))
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_TWO.get_chat_photos("me")]
		await USER_TWO.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	except Exception as atiya:
		print(atiya)
		await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["delpfp3"]) & filters.user(OWNER_ID))
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_THREE.get_chat_photos("me")]
		await USER_THREE.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	except Exception as atiya:
		print(atiya)
		await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")

@app.on_message(filters.command(["delpfp4"]) & filters.user(OWNER_ID))
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_FOUR.get_chat_photos("me")]
		await USER_FOUR.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	except Exception as atiya:
		print(atiya)
		await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")


@app.on_message(filters.command(["delpfp5"]) & filters.user(OWNER_ID))
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_FIVE.get_chat_photos("me")]
		await USER_FIVE.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
	except Exception as atiya:
		print(atiya)
		await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ")
