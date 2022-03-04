from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from asyncio.exceptions import TimeoutError


@kyy_cmd(pattern="sg(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Mohon Balas Ke Pesan Pengguna.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await edit_delete(steal, "```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    xx = await edit_or_reply(steal, "```Mengambil Informasi Pengguna Tersebut, Mohon Menunggu..```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await xx.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await xx.edit("```Saya Tidak Menemukan Informasi Pengguna Ini, Pengguna Ini Belum Pernah Mengganti Nama Sebelumnya```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await xx.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await xx.edit("`Saya Sedang Sakit Mohon Maaf`")


CMD_HELP.update({
    "sangmata":
        f"`{cmd}sg`\
          \nUsage: Mendapatkan Riwayat Nama Pengguna."
})
