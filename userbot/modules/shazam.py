# Ported By VICKY <@VckyouuBitch>
#
# Geez Projects UserBot
# Copyright (C) 2021 GeezProjects
#
# This file is a part of <https://github.com/vckyou/GeezProjects/>
# PLease read the GNU Affero General Public License in
# <https://github.com/vckyou/GeezProjects/blob/master/LICENSE>.


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd


@kyy_cmd(pattern="shazam(?: |$)(.*)")
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await edit_delete(event, "```Membalas pesan audio.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                xx = await edit_or_reply(event, "```Mengidentifikasi lagu```")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await xx.edit(
                        "Terjadi kesalahan saat mengidentifikasi lagu. Coba gunakan pesan audio berdurasi 5-10 detik."
                    )
                await xx.edit("```Tunggu sebentar...```")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await xx.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**Judul : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
            await xx.edit(namem)
            await event.client.delete_messages(
                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id, response.id]
            )
    except TimeoutError:
        return await xx.edit("`Error: `@auddbot` tidak merespons, coba lagi nanti")

CMD_HELP.update(
    {
        "shazam": f">`{cmd}shazam <reply to voice/audio>"
        "\nUsage: Reverse search audio file using (@auddbot)"
    }
)
