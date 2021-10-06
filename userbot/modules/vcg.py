# from Ultroid
# Ported By Kyy @IDnyaKosong
# Copyright (c) 2021 Kyy-userbot
# Thanks Ultroid

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin!"


async def get_call(event):
    kyy = await event.client(getchat(event.chat_id))
    user = await event.client(getvc(kyy.full_chat.call))
    return user.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, groups_only=True, pattern=r"^\.startvc$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Memulai Obrolan Suara...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Menghentikan Obrolan Suara...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.vcinvite")
async def _(c):
    await c.edit("`Mengundang Member Ke Obrolan Suara...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"`{z}`Berhasil Mengundang Member ke VCG")


CMD_HELP.update(
    {
        "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara di Grup.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Mematikan Obrolan Suara di Grup.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Mengundang Member Grup ke Obrolan Suara. (Kamu harus Bergabung)."
    }
)
