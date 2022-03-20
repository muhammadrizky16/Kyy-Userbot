from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import CMD_HELP, DEVS, bot
from userbot import CMD_HANDLER as cmd
from userbot.events import register
from userbot.utils import edit_or_reply, kyy_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Ini Tidak Mungkin Tanpa ID Pengguna`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(
                    probable_user_mention_entity,
                    MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit(
                "`Terjadi Kesalahan... Mohon Lapor Ke` @IDnyaKosong", str(err)
            )
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"**Pengguna Gban Telah Bergabung** \n"
                                f"**Pengguna**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Aksi**  : `Banned`"
                            )
                        except BaseException:
                            return


@kyy_cmd(pattern="gban(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cgban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    user = await userbot.client.get_me()
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        gbun = await dc.reply("`Ingin Mengaktifkan Perintah Global Banned!`")
    else:
        gbun = await edit_or_reply(userbot, "`Memproses Global Banned Pengguna Ini!!`")
    me = await userbot.client.get_me()
    await gbun.edit(f"`Global Banned Akan Segera Aktif!!!`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await gbun.edit(f"`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await gbun.edit(
                f"`Anda Tidak Bisa Melakukan Global Banned, Karena dia pembuatku🤪`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await gbun.edit(f"`Global Banned Aktif ✅`")
            except BaseException:
                b += 1
    else:
        await gbun.edit(f"`Mohon Balas Ke Pesan`")
    try:
        if gmute(user.id) is False:
            return await gbun.edit(
                f"**Kesalahan! Pengguna Ini Sudah Kena Perintah Global Banned.**"
            )
    except BaseException:
        pass
    return await gbun.edit(
        f"**Perintah:** [{user.first_name}](tg://user?id={user.id})\n**Pengguna:** [{user.first_name}](tg://user?id={user.id})\n**Aksi:** `Global Banned`"
    )


@kyy_cmd(pattern="ungban(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    user = await userbot.client.get_me()
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        ungbun = await dc.reply("`Membatalkan Perintah Global Banned Pengguna Ini`")
    else:
        ungbun = await edit_or_reply(userbot, "`Membatalkan Perintah Global Banned`")
    me = await userbot.client.get_me()
    await ungbun.edit(
        f"`Memulai Membatalkan Perintah Global Banned, Pengguna Ini Akan Dapat Bergabung Ke Grup Anda`"
    )
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await ungbun.edit("`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await ungbun.edit(
                "**Pengguna Ini tidak bisa di Blacklist, Karna Dia adalah pembuatku🤪**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await ungbun.edit(f"`Membatalkan Global Banned... Memproses... `")
            except BaseException:
                b += 1
    else:
        await ungbun.edit("`Harap Balas Ke Pesan Pengguna`")
    try:
        if ungmute(user.id) is False:
            return await ungbun.edit(
                "**Kesalahan! Pengguna Sedang Tidak Di Global Banned.**"
            )
    except BaseException:
        pass
    return await ungbun.edit(
        f"**Perintah :** [{user.first_name}](tg://user?id={user.id})\n**Pengguna:** [{user.first_name}](tg://user?id={user.id})\n**Aksi:** `Membatalkan Global Banned`"
    )


CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
      \n\n  •  **Syntax :** `{cmd}gban`\
      \n  •  **Function :** Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin.\
      \n\n  •  **Syntax :** `{cmd}ungban`\
      \n  •  **Function :** membatalkan global banned.\
      "
    }
)
