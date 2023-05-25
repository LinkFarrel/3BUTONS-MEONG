# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/userbotch & t.me/ramsupportt
# Add Code FROM 3-BUTTONS <https://github.com/ramadhani892/3-BUTTONS

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝚂𝙰𝚈𝙰 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙶𝚁𝙾𝚄𝙿", url=client.invitelink2),
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝚂𝙰𝚈𝙰 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝚂𝙰𝚈𝙰 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝚂𝙰𝚈𝙰 •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(tex𝚝="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙶𝚁𝙾𝚄𝙿", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝚂𝙰𝚈𝙰 •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
                InlineKeyboardButton(text="𝙶𝚁𝙾𝚄𝙿 𝙲𝙷𝙰𝚃", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝚄𝚃𝚄𝙿 •", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙶𝚁𝙾𝚄𝙿", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙲𝙾𝙱𝙰 𝙻𝙰𝙶𝙸",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙲𝙾𝙱𝙰 𝙻𝙰𝙶𝙸",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙶𝚁𝙾𝚄𝙿", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙲𝙾𝙱𝙰 𝙻𝙰𝙶𝙸",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink),
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙶𝚁𝙾𝚄𝙿", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙲𝙾𝙱𝙰 𝙻𝙰𝙶𝙸",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
