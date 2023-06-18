# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode now By @thisrama
# t.me/ramsupportt & t.me/userbotch

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Informasi.\n\n • 𝙿𝙴𝙼𝙸𝙻𝙸𝙺 𝚁𝙴𝙿𝙾 : @thisrama\n • 𝙵𝙾𝚁𝙺 : @meongsukanakal\n • 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : <a href='https://t.me/asupanmilikmu'>JOIN</a>\n • 𝙶𝚁𝙾𝚄𝙿 : <a href='https://t.me/+vZYDHWVXeS5mYzRl'>JOIN</a>\n\n Support @userbotch</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
