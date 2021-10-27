# Credits: mrconfused
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon import events

from userbot import BOTLOG, BOTLOG_CHATID
from userbot import CMD_HELP, LOGS, bot
from userbot.events import register
from userbot.modules.sql_helper import no_log_pms_sql
from userbot.modules.sql_helper.globals import addgvar, gvarstatus
from userbot.utils import _format, edit_delete
from userbot.utils.logger import logging
from userbot.utils.tools import media_type

LOGS = logging.getLogger(__name__)


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@register(outgoing=True, incoming=True, func=lambda e: e.mentioned)
async def log_tagged_messages(event):
    hmm = await event.get_chat()

    if BOTLOG_CHATID:
        sender = await event.get_sender()
        await asyncio.sleep(5)
        if not event.is_private and not (await event.get_sender()).bot:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"<b>📮 #TAGS #MENERUSKAN</b> \n<b> • Dari : </b>{sender.first_name}\
			\n<b> • Grup : </b><code>{hmm.title}</code>\
                        \n<b> • 👀 </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'>Lihat Pesan</a>",
                parse_mode="html",
                link_preview=True,
            )
            e = await event.client.get_entity(int(BOTLOG_CHATID))
            fwd_message = await event.client.forward_messages(
                e, event.message, silent=True
            )
        else:
            if event.is_private:
                if not (await event.get_chat()).bot:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"<b>📮 #TAGS</b> \n<b> • Dari : </b>{sender.first_name}\
                                \n<b> • User ID : </b><code>{sender.id}</code>",
                        parse_mode="html",
                        link_preview=True,
                    )
                    e = await event.client.get_entity(int(BOTLOG_CHATID))
                    fwd_message = await event.client.forward_messages(
                        e, event.message, silent=True
                    )


@register(outgoing=True, pattern=r"^.save(?: |$)(.*)")
async def log(log_text):
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"**#LOG / Chat ID:** {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit("**Apa yang harus saya simpan?**")
            return
        await log_text.edit("**Berhasil disimpan di Grup Log**")
    else:
        await log_text.edit("**Module ini membutuhkan LOGGER untuk diaktifkan!**")
    await asyncio.sleep(2)
    await log_text.delete()


@register(outgoing=True, pattern=r"^.log(?: |$)(.*)")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.disapprove(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Diaktifkan**", 15
            )


@register(outgoing=True, pattern=r"^.nolog(?: |$)(.*)")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.approve(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Dimatikan**", 15
            )


@register(outgoing=True, pattern=r"^.pmlog(?: |$)(.*)")
async def set_pmlog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await event.edit("**PM LOG Sudah Diaktifkan**")
        else:
            addgvar("PMLOG", h_type)
            await event.edit("**PM LOG Berhasil Dimatikan**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await event.edit("**PM LOG Berhasil Diaktifkan**")
    else:
        await event.edit("**PM LOG Sudah Dimatikan**")


@register(outgoing=True, pattern=r"^.gruplog(?: |$)(.*)")
async def set_gruplog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await event.edit("**Group Log Sudah Diaktifkan**")
        else:
            addgvar("GRUPLOG", h_type)
            await event.edit("**Group Log Berhasil Dimatikan**")
    elif h_type:
        addgvar("GRUPLOG", h_type)
        await event.edit("**Group Log Berhasil Diaktifkan**")
    else:
        await event.edit("**Group Log Sudah Dimatikan**")


CMD_HELP.update({
    "log": f"**Plugin : **`log`\
    \n\n  •  **Syntax :** `.save`\
    \n  •  **Function : **Untuk Menyimpan pesan yang ditandai ke grup pribadi\
    \n\n  •  **Syntax :** `.log`\
    \n  •  **Function : **Untuk mengaktifkan Log Chat dari obrolan/grup itu\
    \n\n  •  **Syntax :** `.nolog`\
    \n  •  **Function : **Untuk menonaktifkan Log Chat dari obrolan/grup itu\
    \n\n  •  **Syntax :** `.pmlog on/off`\
    \n  •  **Function : **Untuk mengaktifkan atau menonaktifkan pencatatan pesan pribadi\
    \n\n  •  **Syntax :** `.gruplog on/off`\
    \n  •  **Function : **Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup pmlogger."
})
