# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
"""Userbot module for keeping control who PM you."""

# Credits: @xditya
# Recode by @xflskyy & @farizjs
# FROM Kyy-Userbot <https://github.com/muhammadrizky16/Kyy-Userbot>
# t.me/NastyProject

from sqlalchemy.exc import IntegrityError
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import User
from telethon import events
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
import userbot.modules.sql_helper.pm_permit_sql as pmpermit_sql
from userbot import CMD_HANDLER as cmd
from userbot import (
    BOTLOG,
    BOTLOG_CHATID,
    BOT_USERNAME,
    CMD_HELP,
    PM_AUTO_BAN,
    PM_LIMIT,
    DEVS,
    owner,
    bot,
)

# ========================= CONSTANTS ===========================

user = bot.get_me()
myid = user.id
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

DEF_UNAPPROVED_MSG = (
    "╔═════════════════════════╗\n"
    " 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗧𝗛𝗘 𝗣𝗥𝗜𝗩𝗔𝗖𝗬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 \n"
    "╚═════════════════════════╝\n"
    "**Dimohon Untuk Tidak Melakukan Spam Ke Room Chat ini!** \n"
    f"**Karena bisa menggangu** {owner} \n"
    f"**Jika Anda Melakukan Spamming, Anda Akan Terblokir Otomatis!**\n"
    "╔═════════════════════╗\n"
    f"➠ 𝗢𝘄𝗻𝗲𝗿 : {owner} \n"
    f"➠ 𝗣𝗲𝘀𝗮𝗻 𝗢𝘁𝗼𝗺𝗮𝘁𝗶𝘀 𝗯𝘆 𝗞𝘆𝘆-𝗨𝘀𝗲𝗿𝗯𝗼𝘁\n"
    "╚═════════════════════╝")
# =================================================================


@bot.on(events.NewMessage(incoming=True))
async def on_new_private_message(event):
    if event.sender_id == myid:
        return

    if BOTLOG_CHATID is None:
        return

    if not event.is_private:
        return

    message_text = event.message.message
    chat_id = event.sender_id

    message_text.lower()
    if DEF_UNAPPROVED_MSG == message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return
    sender = await bot.get_entity(chat_id)

    if chat_id == user.id:

        # don't log Saved Messages

        return

    if sender.bot:

        # don't log bots

        return

    if sender.verified:

        # don't log verified accounts

        return

    if not pmpermit_sql.is_approved(chat_id):
        # pm permit
        await do_pm_permit_action(chat_id, event)


async def do_pm_permit_action(chat_id, event):
    if not PM_AUTO_BAN:
        return
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == PM_LIMIT:
        r = await event.reply(DEF_UNAPPROVED_MSG)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=BOTLOG_CHATID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return
    # inline pmpermit menu
    mybot = BOT_USERNAME
    tele = await bot.inline_query(mybot, "pmpermit")
    r = await tele[0].click(event.chat_id, hide_via=True)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r


@bot.on(events.NewMessage(outgoing=True))
async def auto_accept(event):
    """Will approve automatically if you texted them first."""
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if (
        event.is_private
        and event.chat_id != 777000
        and event.chat_id != self_user.id
        and not (await event.get_sender()).bot
    ):
        try:
            from userbot.modules.sql_helper.globals import gvarstatus
            from userbot.modules.sql_helper.pm_permit_sql import approve, is_approved
        except AttributeError:
            return

        # Use user custom unapproved message
        get_message = gvarstatus("unapproved_msg")
        if get_message is not None:
            UNAPPROVED_MSG = get_message
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(
                event.chat_id, reverse=True, limit=1
            ):
                if (
                    message.text is not UNAPPROVED_MSG
                    and message.from_id == self_user.id
                ):
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#AUTO-APPROVED\n"
                        + "Pengguna 👤: "
                        + f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@kyy_cmd(pattern="notifoff$")
async def notifoff(noff_event):
    """For .notifoff command, stop getting notifications from unapproved PMs."""
    try:
        from userbot.modules.sql_helper.globals import addgvar
    except AttributeError:
        return await noff_event.edit("`Running on Non-SQL mode!`")
    addgvar("NOTIF_OFF", True)
    await noff_event.edit("`Notifikasi Dari Pesan Pribadi Tidak Disetujui, Telah Dibisukan!`")


@kyy_cmd(pattern="notifon$")
async def notifon(non_event):
    """For .notifoff command, get notifications from unapproved PMs."""
    try:
        from userbot.modules.sql_helper.globals import delgvar
    except AttributeError:
        return await non_event.edit("`Running on Non-SQL mode!`")
    delgvar("NOTIF_OFF")
    await non_event.edit("`Notifikasi Dari Pesan Pribadi Tidak Disetujui, Tidak Lagi Dibisukan!`")


@kyy_cmd(pattern="(?:setuju|ok)\\s?(.)?")
async def approvepm(apprvpm):
    """For .ok command, give someone the permissions to PM you."""
    try:
        from userbot.modules.sql_helper.globals import gvarstatus
        from userbot.modules.sql_helper.pm_permit_sql import approve
    except AttributeError:
        return await edit_delete(apprvpm, "`Running on Non-SQL mode!`")

    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        replied_user = await apprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id

    else:
        aname = await apprvpm.client.get_entity(apprvpm.chat_id)
        name0 = str(aname.first_name)
        uid = apprvpm.chat_id

    # Get user custom msg
    getmsg = gvarstatus("unapproved_msg")
    if getmsg is not None:
        UNAPPROVED_MSG = getmsg
    else:
        UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

    async for message in apprvpm.client.iter_messages(
        apprvpm.chat_id, from_user="me", search=UNAPPROVED_MSG
    ):
        await message.delete()

    try:
        approve(uid)
    except IntegrityError:
        return await edit_delete(apprvpm, "`Oke Pesan Anda Sudah Diterima ツ`")

    await edit_delete(apprvpm, f"`Hai` [{name0}](tg://user?id={uid}) `Pesan Anda Sudah Diterima 😎`")
    await edit_delete(apprvpm, getmsg)
    await message.delete()

    if BOTLOG:
        await apprvpm.client.send_message(
            BOTLOG_CHATID,
            "#DITERIMA\n" + "User: " + f"[{name0}](tg://user?id={uid})"
        )


@kyy_cmd(pattern="(?:tolak|nopm)\\s?(.)?")
async def disapprovepm(disapprvpm):
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
    except BaseException:
        return await edit_delete(disapprvpm, "`Running on Non-SQL mode!`")

    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        replied_user = await disapprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        dissprove(aname)
    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        name0 = str(aname.first_name)

    await edit_or_reply(disapprvpm,
                        f"`Maaf` [{name0}](tg://user?id={disapprvpm.chat_id}) `Pesan Anda Telah Ditolak, Mohon Jangan Melakukan Spam Ke Room Chat!`"
                        )

    if BOTLOG:
        await disapprvpm.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={disapprvpm.chat_id})"
            " `Berhasil Ditolak` !",
        )


@kyy_cmd(pattern="block$")
async def blockpm(block):
    """For .block command, block people from PMing you!"""
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        await block.client(BlockRequest(aname))
        await block.edit(f"`Anda Telah Diblokir Oleh {owner}`")
        uid = replied_user.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        await block.edit(f"`Anda Telah Diblokir Oleh {owner}`")
        name0 = str(aname.first_name)
        uid = block.chat_id

    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove

        dissprove(uid)
    except AttributeError:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            "#BLOKIR\n" + "Pengguna: " + f"[{name0}](tg://user?id={uid})",
        )


@kyy_cmd(pattern="unblock$")
async def unblockpm(unblock):
    """For .unblock command, let people PMing you again!"""
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit("`Anda Sudah Tidak Diblokir Lagi.`")

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.id})" " Tidak Lagi Diblokir.",
        )


@kyy_cmd(pattern="(set|get|reset) pm_msg(?: |$)(\\w*)")
async def add_pmsg(cust_msg):
    """Set your own Unapproved message"""
    if not PM_AUTO_BAN:
        return await cust_msg.edit("**Anda Harus Menyetel** `PM_AUTO_BAN` **Ke** `True` Atau Ketik `.set var PM_AUTO_BAN True`")
    try:
        import userbot.modules.sql_helper.globals as sql
    except AttributeError:
        await cust_msg.edit("`Running on Non-SQL mode!`")
        return

    await cust_msg.edit("`Sedang Memproses...`")
    conf = cust_msg.pattern_match.group(1)

    custom_message = sql.gvarstatus("unapproved_msg")

    if conf.lower() == "set":
        message = await cust_msg.get_reply_message()
        status = "Pesan"

        # check and clear user unapproved message first
        if custom_message is not None:
            sql.delgvar("unapproved_msg")
            status = "Pesan"

        if message:
            # TODO: allow user to have a custom text formatting
            # eg: bold, underline, striketrough, link
            # for now all text are in monoscape
            msg = message.message  # get the plain text
            sql.addgvar("unapproved_msg", msg)
        else:
            return await cust_msg.edit("`Mohon Balas Ke Pesan`")

        await cust_msg.edit("`Pesan Berhasil Disimpan Ke Room Chat`")

        if BOTLOG:
            await cust_msg.client.send_message(
                BOTLOG_CHATID, f"**{status} PM Yang Tersimpan Dalam Room Chat Anda:** \n\n{msg}"
            )

    if conf.lower() == "reset":
        if custom_message is not None:
            sql.delgvar("unapproved_msg")
            await cust_msg.edit("`Anda Telah Menghapus Pesan Custom PM Ke Default`")
        else:
            await cust_msg.edit("`Pesan PM Anda Sudah Default Sejak Awal`")

    if conf.lower() == "get":
        if custom_message is not None:
            await cust_msg.edit(
                "**Ini Adalah Pesan PM Yang Sekarang Dikirimkan Ke Room Chat Anda:**" f"\n\n{custom_message}"
            )
        else:
            await cust_msg.edit(
                "*Anda Belum Menyetel Pesan PM*\n"
                f"Masih Menggunakan Pesan PM Default: \n\n`{DEF_UNAPPROVED_MSG}`"
            )


@bot.on(events.NewMessage(incoming=True, from_users=(DEVS)))
async def permitpm(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(
                chats.id, f"`Developer Telah Mengirimi Anda Pesan... `")
            await borg.send_message(
                chats, f"**Menerima Pesan!, Pengguna Terdeteksi Adalah Developer saya!**"
            )


CMD_HELP.update(
    {
        "pmpermit": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}setuju | {cmd}ok`"
        "\n↳ : Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}tolak | {cmd}nopm`"
        "\n↳ : Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}block`"
        "\n↳ : Memblokir Orang Di PM."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}unblock`"
        "\n↳ : Membuka Blokir."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}notifoff`"
        "\n↳ : Mematikan notifikasi pesan yang belum diterima."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}notifon`"
        "\n↳ : Menghidupkan notifikasi pesan yang belum diterima."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}set pm_msg` <balas ke pesan>"
        "\n↳ : Menyetel Pesan Pribadimu untuk orang yang pesannya belum diterima"
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}get pm_msg`"
        "\n↳ : Mendapatkan Custom pesan PM mu"
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}reset pm_msg`"
        "\n↳ : Menghapus pesan PM ke default"
        "\n\nPesan Pribadi yang belum diterima saat ini tidak dapat disetel"
        "\nke teks format kaya bold, underline, link, dll."
        "\nPesan akan terkirim normal saja"})
