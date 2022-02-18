# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import BOTLOG_CHATID, BOT_USERNAME, BOT_TOKEN, BOT_VER, LOGS, ALIVE_NAME, bot

from userbot.modules import ALL_MODULES
from userbot.utils import autobot


try:
    bot.start()
except PhoneNumberInvalidError:
    print("The phone number is incorrect!")
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

# bot.loop.run_until_complete(checking())
LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/NastySupportt")
LOGS.info(
    f"✨Kyy-Userbot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "✨ **Kyy Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @NastyProject ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
