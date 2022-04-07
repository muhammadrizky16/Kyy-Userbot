# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module
from pytgcalls import idle

from userbot import (
    BOTLOG_CHATID,
    BOT_TOKEN,
    BOT_VER,
    LOGS,
    bot,
)
from userbot.modules import ALL_MODULES
from userbot.clients import kyy_ubot_on, multiclientkyy
from userbot.utils import autobot, autopilot, git

try:
    client = multiclientkyy()
    total = 5 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

bot.loop.run_until_complete(kyy_ubot_on())
if not BOTLOG_CHATID:
    bot.loop.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())
LOGS.info(
    f"Jika Anda Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/NastySupportt")
LOGS.info(
    f"✨Kyy-Userbot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
