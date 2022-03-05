# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from userbot import BOTLOG_CHATID, BOT_USERNAME, BOT_TOKEN, BOT_VER, LOGS, ALIVE_NAME, ALIVE_LOGO
from userbot import call_py, kyyblacklist, bot
from userbot.modules import ALL_MODULES
from userbot.utils import autobot

try:
    bot.start()
    user = bot.get_me()
    kyyblacklist = requests.get(
        "https://raw.githubusercontent.com/muhammadrizky16/Kyyblack/master/kyyblacklist.json"
    ).json()
    if user.id in kyyblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE ORANG KEK LU.\nCredits: @IDnyaKosong"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/NastySupportt")
LOGS.info(
    f"✨Kyy-Userbot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"✨ **Kyy Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@Kyy-Userbot\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @NastyProject ")
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
