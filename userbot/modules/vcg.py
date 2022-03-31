# Thanks Full To Team Ultroid
# Fiks By Kyy @IDnyaKosong


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl import types
from telethon.utils import get_display_name

from userbot import owner
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_delete, edit_or_reply, kyy_cmd
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(kyy):
    kyy = await kyy.client(getchat(kyy.chat_id))
    await kyy.client(getvc(kyy.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@kyy_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Memulai Obrolan Suara`")
    except Exception as ex:
        await edit_or_reply(c, f"**ERROR:** `{ex}`")


@kyy_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Mematikan Obrolan Suara`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@kyy_cmd(pattern="vcinvite")
async def _(kyy):
    await edit_or_reply(kyy, "`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in kyy.client.iter_participants(kyy.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await kyy.client(invitetovc(call=await get_call(kyy), users=p))
            z += 6
        except BaseException:
            pass
    await edit_or_reply(kyy, f"`Menginvite {z} Member`")


@kyy_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vctittle <tittle vcg>`\
         \n↳ : `Mengubah tittle/judul Obrolan Suara.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite semua member yang berada di group."
    }
)
