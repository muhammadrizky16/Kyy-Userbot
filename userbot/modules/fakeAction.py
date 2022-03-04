# Port By @IDnyaKosong From Kyy-Userbot
# # Copyright (C) 2021 Kyy-Userbot

from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd
import asyncio


@kyy_cmd(pattern="ftyping(?: |$)(.*)")
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
                return await edit_delete(event, "`Incorrect Format`")
    await edit_or_reply(event, f"`Memulai Pengetikan Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="faudio(?: |$)(.*)")
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
                return await edit_delete(event, "`Incorrect Format`")
    await edit_or_reply(event, f"`Memulai merekam audio palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fvideo(?: |$)(.*)")
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
                return await edit_delete(event, "`Incorrect Format`")
    await edit_or_reply(event, f"`Memulai merekam video palsu selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fgame(?: |$)(.*)")
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
                return await edit_delete(event, "`Incorrect Format`")
    await edit_or_reply(event, f"`Memulai Bermain Game Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fround(?: |$)(.*)")
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
                return await edit_delete(event, "`Masukan jumlah detik yang benar`")
    xx = await edit_delete(event, f"`Memulai merekam video message palsu Selama {t} sec.`")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "record-round"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fphoto(?: |$)(.*)")
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
                return await edit_delete(event, "`Masukan jumlah detik yang benar`")
    xx = await edit_or_reply(event, f"`Memulai Mengirim Photo Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "photo"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fdocument(?: |$)(.*)")
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
                return await edit_delete(event, "`Masukan jumlah detik yang benar`")
    xx = edit_or_reply(
        event, f"`Memulai Mengirim Document Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "document"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="flocation(?: |$)(.*)")
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
                return await edit_delete(event, "`Masukan jumlah detik yang benar`")
    xx = await edit_or_reply(event, f"`Memulai Share Lokasi Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "location"):
        await asyncio.sleep(t)


@kyy_cmd(pattern="fcontact(?: |$)(.*)")
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
                return await edit_delete(event, "`Masukan jumlah detik yang benar`")
    xx = await edit_or_reply(event, f"`Memulai Mengirim Contact Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "contact"):
        await asyncio.sleep(t)


CMD_HELP.update({
    "fakeaction":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ftyping` <jumlah teks>\
   \nUsage : Seakan akan sedang mengetik padahal tidak\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}faudio` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}video` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake video\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fgame` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fphoto` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake foto\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fdocument` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake document\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}flocation` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake location\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fcontact` <jumlah teks>\
   \nUsage : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake contact"
})
