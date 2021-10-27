# Port By @IDnyaKosong From Kyy-Userbot
# # Copyright (C) 2021 Kyy-Userbot
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai Pengetikan Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai merekam audio palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai merekam video palsu selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai Bermain Game Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fround(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai merekam video message palsu Selama {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "record-round"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fphoto(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Photo Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "photo"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fdocument(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Document Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "document"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.flocation(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Share Lokasi Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "location"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fcontact(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Contact Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "contact"):
        await asyncio.sleep(t)


CMD_HELP.update({
    "fakeaction":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping` <jumlah teks>\
   \nUsage : Seakan akan sedang mengetik padahal tidak\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.faudio` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fvideo` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake video\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fgame` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fphoto` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake foto\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fdocument` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake document\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.flocation` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake location\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fcontact` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake contact"
})
