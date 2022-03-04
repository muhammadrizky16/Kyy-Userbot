from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd


@kyy_cmd(pattern="tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await edit_delete(event, "`Mohon Maaf, Saya Membutuhkan Link Video Tiktok Untuk Mendownload Nya`")
    else:
        xx = await edit_or_reply(event, "```Video Sedang Diproses.....```")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await xx.edit("**Kesalahan:** `Mohon Buka Blokir` @ttsavebot `Dan Coba Lagi !`")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await xx.delete()


CMD_HELP.update(
    {
        "tiktok": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}tiktok <Link tiktok>`"
        "\n• : Download Video Tiktok Tanpa Watermark"
    }
)
