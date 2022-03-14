# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd


@kyy_cmd(pattern="logo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_or_reply(event, "`Give a name too!`")
    else:
        await edit_or_reply(event, "`Processing`")
    chat = "@Nastymusiicbot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @Nastymusiicbot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"ʟᴏɢᴏ ʙʏ [{owner}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()


CMD_HELP.update({"logo": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}logo <text>`"
                 "\n↳ : Hasilkan logo dari Teks atau Balas Ke gambar yang diberikan, untuk menulis teks Anda di atasnya. Atau Balas Ke File Font, Untuk menulis dengan font itu."})
