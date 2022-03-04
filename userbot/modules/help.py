# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@kyy_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, "`Command` **Tidak Valid**")
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ✗  "
        await edit_or_reply(event, "**✨ҡʏʏ-υѕєявσт✨**\n\n"
                         f"**◉ Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◉ Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"◉ {string}◉\n\n☞  ᴘʀᴏᴊᴇᴄᴛ : @NastyProject")
        await event.reply(
            f"\n**Contoh Ketik** `{cmd}help animasi` **Untuk Melihat Informasi Module**"
        )
