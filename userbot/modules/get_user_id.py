from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "`Mohon Reply Ke Pesan`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_delete(event, "```Mohon Balas Ke Reply```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_delete(event, "`Mohon Reply Ke Pesan`")
        return
    xx = await edit_or_reply(event, "`Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1663258664))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Sedang Error`")
            return
        if response.text.startswith("Forward"):
            await xx.edit("`Mohon Maaf, Orang Ini Tidak Mempunyai ID`")
        else:
            await xx.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}getid`"
    "\n↳ : Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
