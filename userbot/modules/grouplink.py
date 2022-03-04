# port by KOALA 🐨 /@manusiarakitann

from userbot.utils import edit_or_reply, kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="gsend ?(.*)")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await edit_or_reply(event, "`Pesan Di Di Teruskan Ke Grup Tujuan`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await edit_or_reply(event, "Pesan Di Di Teruskan Ke Grup Tujuan`")
    except BaseException:
        await edit_or_reply(event, "** Gagal Mengirim Pesan, Emang Lu Join Grup Nya Goblok ? **")

CMD_HELP.update(
    {
        "grouplink": f"{cmd}gsend\
    \nMengirim Pesan Jarak Jauh Ke Grup Lain .gsend <link grup> <pesan>."
    })
