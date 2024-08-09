import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from Spotify_Music import app


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ"
        )
    try:
        text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")

        async def progress(current, total):
            await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")

        try:
            local_path = await message.reply_to_message.download( progress=progress
            )
            await text.edit_text("📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"🌐 | [ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            try:
                os.remove(local_path)
            except Exception:
               pass
        except Exception as e:
            await text.edit_text(f"❌ |ғɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ \n\n<i>ʀᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
               pass
            return
    except Exception:
        pass

__HELP__ = """
**ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

- `/tgm`: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.
- `/tgt`: sᴀᴍᴇ ᴀs `/tgm`.
- `/telegraph`: sᴀᴍᴇ ᴀs `/tgm`.
- `/tl`: sᴀᴍᴇ ᴀs `/tgm`.

**ᴇxᴀᴍᴘʟᴇ:**
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ `/tgm` ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

**ɴᴏᴛᴇ:**
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""

__MODULE__ = "Tᴇʟᴇɢʀᴀᴘʜ"

#id#

from Spotify_Music import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"User {reply.from_user.first_name} ID is : {reply.from_user.id}",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"ᴛʜɪs ɢʀᴏᴜᴩ's ɪᴅ ɪs: {message.chat.id}",
           reply_markup=markup
        )
        
