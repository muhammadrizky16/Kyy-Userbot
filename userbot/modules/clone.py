# imported from github.com/ravana69/PornHub to userbot by @heyworld
# please don't nuke my credits 😓
import requests
import bs4
import os
import asyncio
import time
import html
from justwatch import JustWatch
from telethon import *
from userbot.events import register
from userbot import CMD_HELP, bot, TEMP_DOWNLOAD_DIRECTORY, DEFAULT_BIO, ALIVE_NAME
from telethon import events
from telethon.tl import functions
from urllib.parse import quote
from datetime import datetime
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.errors.rpcerrorlist import YouBlockedUserError


import logging

normiefont = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z']
weebyfont = [
    '卂',
    '乃',
    '匚',
    '刀',
    '乇',
    '下',
    '厶',
    '卄',
    '工',
    '丁',
    '长',
    '乚',
    '从',
    '𠘨',
    '口',
    '尸',
    '㔿',
    '尺',
    '丂',
    '丅',
    '凵',
    'リ',
    '山',
    '乂',
    '丫',
    '乙']


logger = logging.getLogger(__name__)

thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@register(outgoing=True, pattern="^.clonee(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id, TEMP_DOWNLOAD_DIRECTORY)
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # inspired by https://telegram.dog/afsaI181
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await bot(functions.account.UpdateProfileRequest(
        first_name=first_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        last_name=last_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        about=user_bio
    ))
    pfile = await bot.upload_file(profile_pic)  # pylint:disable=E060
    await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
        pfile
    ))
    #message_id_to_reply = event.message.reply_to_msg_id
    # if not message_id_to_reply:
    #    message_id_to_reply = event.message.id
    # await bot.send_message(
    #  event.chat_id,
    #  "Hai, Apa Kabarmu?",
    #  reply_to=message_id_to_reply,
    #  )
    await event.delete()
    await bot.send_message(
        event.chat_id,
        "`Aku adalah kamu dan kamu adalah aku.`",
        reply_to=reply_message
    )


@register(outgoing=True, pattern="^.reclone(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    name = f"{ALIVE_NAME}"
    bio = f"{DEFAULT_BIO}"
    n = 1
    await bot(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n)))
    await bot(functions.account.UpdateProfileRequest(about=bio))
    await bot(functions.account.UpdateProfileRequest(first_name=name))
    await event.edit(f"`{ALIVE_NAME} Berhasil Mengembalikan Akun Anda dari clone`")


CMD_HELP.update(
    {
        "clone": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.clone` <username>.\
        \n↳ : Mulai Mengaktifkan Clonning Ke Seseorang\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `'.rclone' Untuk Mengembalikan\
        \n↳ : Mengembalikan Kloning, Dan Kembali Keakun Utama.\
    "
    }
)
