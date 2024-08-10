import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from Spotify_Music import app  

photo = [
     "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
     "https://telegra.ph/file/a20ce93f9413d7b6da73f.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "🌸ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ🌸"
msg = (
                f"💥 ɴᴇᴡ ɢʀᴏᴜᴘ \n\n"
                f"🤡ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"✏️ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"📝ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{username}\n"
                f"📈ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ: {count}\n"
                f"🪅ᴀᴅᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🦋ᴀᴅᴅ ᴍᴇ ɪɴ ᴍᴏʀᴇ🦋", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#ʟᴇғᴛ_ɢʀᴏᴜᴘ</u></b> ✫\n\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\n\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remove_by}\n\nʙᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)


