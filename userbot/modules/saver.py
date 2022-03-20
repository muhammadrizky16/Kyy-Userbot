
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import CMD_HANDLER as cmd, CMD_HELP, bot


@kyy_cmd(pattern="igsaver ?(.*)")
async def igsaver(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "`Mohon Reply Ke Link Instagram Ya..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_delete(event, "`Mohon Maaf, Saya Membutuhkan Link Media Instagram Untuk di Download`")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        xx = await edit_or_reply(event, "`Sedang Memproses...`")
        return
    user = await event.client.get_me()
    await xx.edit("`Sedang Memproses...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await xx.edit("`Mohon Pergi ke ` @SaveAsbot `Lalu Tekan Start dan Coba Lagi.`")
            return
        if response.text.startswith("Forward"):
            await xx.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await xx.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By [{user.first_name}](tg://user?id={user.id})**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await xx.delete()


CMD_HELP.update({"instasaver": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}igsaver`"
                 f"\n↳ : Download Postingan di Instagram, Silahkan Salin Link Postingan Instagram Yang Ingin Anda Download Terus Kirim Link, Lalu Reply dan Ketik `{cmd}igsaver`"})
