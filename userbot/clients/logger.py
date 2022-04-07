# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import KYY2, KYY3, KYY4, KYY5, bot, branch, tgbot
from userbot.utils import kyyscrt

MSG_ON = """
✨**ҡʏʏ-υѕєявσт ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋғᴛɪғᴋᴀɴ**!!
━━━━━━━━━━━━━━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}ping` **untuk Mengecheck Bot**
━━━━━━━━━━━━━━━
➠ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :** @NastyProject
"""


async def kyy_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            KyyUBOT = await tgbot.get_me()
            BOT_USERNAME = KyyUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            KyyUBOT = await tgbot.get_me()
            BOT_USERNAME = KyyUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await kyyscrt(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KYY2:
            await kyyscrt(KYY2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KYY2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KYY3:
            await kyyscrt(KYY3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KYY3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KYY4:
            await kyyscrt(KYY4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KYY4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KYY5:
            await kyyscrt(KYY5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KYY5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
