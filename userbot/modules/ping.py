# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
import redis

from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd, CMD_HELP, StartTime
from userbot.events import register
from userbot.utils import edit_or_reply, kyy_cmd

absen = [
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak** 😉",
    "**Hadir bang** 😁",
    "**Hadir kak maap telat** 🥺",
]

pacar = [
    "**Saya Hadir Untuk Membasmi Para Jamet Telegram** 😎 ",
    "**Iya Bang kenapa?**",
    "**Uuyy Bang**",
    "**Hadir uyy** 😁",
    "**Saya Hadir Untuk Melindungi Cewe Dari Laki Laki Sangean** 😎",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1663258664, pattern=r"^.absen$")
async def _(kyy):
    await kyy.reply(random.choice(absen))


@register(incoming=True, from_users=1663258664, pattern=r"^.kyy$")
async def _(kyy):
    await kyy.reply(random.choice(pacar))


@kyy_cmd(pattern="sping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(pong, "**✲**")
    await xx.edit("**✲✲**")
    await xx.edit("**✲✲✲**")
    await xx.edit("__DUAR__")
    await xx.edit("🔥")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await xx.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) **        \n"
        f"**➾Kecepatan : ** '%sms'  \n"
        f"**➾Branch : ** 'Kyy-Userbot` \n" % (duration)
    )


@kyy_cmd(pattern="lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(pong, "`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await lping.edit(
        f"** [{user.first_name}](tg://user?id={user.id}) **\n"
        f"✧ **-ꜱɪɢɴᴀʟ- :** "
        f"`%sms` \n"
        f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
        f"`{uptime}` \n" % (duration)
    )


@kyy_cmd(pattern="xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(pong, "__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat...__")
    await xping.edit("__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat...__")
    await xping.edit("__Sedang Memuat.__")
    await xping.edit("__Sedang Memuat..__")
    await xping.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**✨ҡʏʏ-υѕєявσт✨**\n"
        f"➾ __Signal__    __:__ "
        f"`%sms` \n"
        f"➾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@kyy_cmd(pattern="sinyal$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sinyal = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await sinyal.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await sinyal.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await sinyal.edit("**40% ████▒▒▒▒▒▒**")
    await sinyal.edit("**60% ██████▒▒▒▒**")
    await sinyal.edit("**80% ████████▒▒**")
    await sinyal.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await sinyal.edit(
        f"**✨ ҡʏʏ-υѕєявσт ✨**\n\n"
        f"** ▹  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ▹  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ▹  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id}) \n" % (duration)
    )


@kyy_cmd(pattern="ping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await edit_or_reply(pong, "**✣**")
    await ping.edit("**✣✣**")
    await ping.edit("**✣✣✣**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ping.edit(
        f"**PONG!!!🏓**\n"
        f"• **Pɪɴɢᴇʀ** = "
        f"`%sms` \n"
        f"• **Uᴘᴛɪᴍᴇ** = "
        f"`{uptime}` \n" % (duration)
    )


@kyy_cmd(pattern="kecepatan$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    kecepatan = await edit_or_reply(spd, "**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await kecepatan.edit(
        "**Kecepatan Jaringan:\n**"
        " ━━━━━━━━━━━━━━━━━ \n"
        f"✧ **Dimulai Pada :**  \n"
        f"`{result['timestamp']}` \n"
        "✧ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "✧ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "✧ **Signal:** "
        f"`{result['ping']}` \n"
        "✧ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "✧ **BOT:** ✨ҡʏʏ-υѕєявσт✨"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@kyy_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    pong = await edit_or_reply(pong, "**◕‿- PONG!!🏓**")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    user = await pong.client.get_me()
    await pong.edit(f"**✨KyyName : [{user.first_name}](tg://user?id={user.id}) **\n📗 `%sms`" % (duration))


@kyy_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pink = await edit_or_reply(pong, "8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8===✊D💦")
    await pink.edit("8====D💦💦")
    await pink.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**BABI!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


CMD_HELP.update(
    {
        "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` | `{cmd}lping` | `{cmd}xping` | `{cmd}sinyal` | `{cmd}sping` | `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)
