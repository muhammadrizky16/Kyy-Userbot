# Copyright (C) 2021 Kyy - Userbot
# Created by Kyy


""" Userbot module for other small commands. """
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.follow$")
async def usit(e):
    await e.edit(
        "✨ **Kʏʏ-Usᴇʀʙᴏᴛ** ✨ \n"
        "➥ **Teleram :** [ҡʏʏ](t.me/IDnyaKosong)\n"
        "➥ **Repo :** [ɢɪᴛʜᴜʙ](https://github.com/muhammadrizky16/)\n"
        "➥ **Instagram :** [ɪɴsᴛᴀɢʀᴀᴍ](instagram.com/rizkyhamdanii16_)\n"
        "➥ **Groups :** [ɢʀᴏᴜᴘs](https://t.me/sinibrokk)\n"
        "➥ **Channel :** [ᴄʜᴀɴɴᴇʟ](https://t.me/ahhsudahlahhh)")


CMD_HELP.update({
    "followme": "`.follow`\
    \nUsage: Difollow dan Join tod."
})
