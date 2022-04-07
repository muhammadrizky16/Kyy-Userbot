# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, KYY2, KYY3, KYY4, KYY5):
    user_ids = list(SUDO_USERS) or []
    kyy_id = await bot.get_me()
    user_ids.append(kyy_id.id)

    try:
        if KYY2 is not None:
            id2 = await KYY2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if KYY3 is not None:
            id3 = await KYY3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if KYY4 is not None:
            id4 = await KYY4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if KYY5 is not None:
            id5 = await KYY5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTY2MzI1ODY2NA==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        KYY_CLIENT = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        KYY_CLIENT = client.first_name
    kyy_rpk = f"[{KYY_CLIENT}](tg://user?id={OWNER_ID})"
    return OWNER_ID, KYY_CLIENT, kyy_rpk
