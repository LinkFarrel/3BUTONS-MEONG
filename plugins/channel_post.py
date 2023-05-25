# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode


@Bot.on_message(
    filters.private
    & filters.user(ADMINS)
    & ~filters.command(
        ["start", "users", "broadcast", "ping", "uptime", "batch", "genlink"]
    )
)
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("<code>𝚃𝚞𝚗𝚐𝚐𝚞 𝚍𝚞𝚕𝚞 𝚌𝚘𝚔𝚔...</code>", quote=True)
    try:
        post_message = await message.copy(
            chat_id=client.db_channel.id, disable_notification=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(
            chat_id=client.db_channel.id, disable_notification=True
        )
    except Exception as e:
        print(e)
        await reply_text.edit_text("<b>𝚃𝙴𝚁𝙻𝙰𝙷 𝚃𝙴𝚁𝙹𝙰𝙳𝙸 𝙴𝚁𝚁𝙾𝚁 𝙽𝙸...</b>")
        return
    converted_id = post_message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✪ 𝚂𝙴𝙱𝙰𝚁 𝙱𝙾𝙺𝙴𝙿", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )

    await reply_text.edit(
        f"<b>𝙻𝙸𝙽𝙺 𝙱𝙾𝙺𝙴𝙿 𝚂𝚄𝙳𝙰𝙷 𝙱𝙴𝚁𝙷𝙰𝚂𝙸𝙻 𝙳𝙸 𝙱𝚄𝙰𝚃 :</b>\n\n{link}",
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)


@Bot.on_message(
    filters.channel & filters.incoming & filters.chat(CHANNEL_ID) & ~filters.edited
)
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✪ 𝚂𝙴𝙱𝙰𝚁 𝙱𝙾𝙺𝙴𝙿", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
