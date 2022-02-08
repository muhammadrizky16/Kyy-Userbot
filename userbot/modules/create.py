# lorduserbot
from telethon.tl import functions
from userbot.utils import kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="buat (gb|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """ For .create command, Creating New Group & Channel """
    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):
        if grop.fwd_from:
            return
        type_of_group = grop.pattern_match.group(1)
        group_name = grop.pattern_match.group(2)
        if type_of_group == "gb":
            try:
                result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@MissRose_bot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name
                ))
                created_chat_id = result.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await grop.edit("Grup/Channel {} Berhasil Dibuat. Tekan [{}]({}) Untuk Melihatnya".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))
        elif type_of_group == "g" or type_of_group == "c":
            try:
                r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                    title=group_name,
                    about="`Selamat Datang Di Channel Ini!`",
                    megagroup=False if type_of_group == "c" else True
                ))
                created_chat_id = r.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await grop.edit("Grup/Channel {} Berhasil Dibuat. Tekan [{}]({}) Untuk Melihatnya".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))

CMD_HELP.update(
    {
        "membuat": f"**Plugin : **`membuat`\
        \n\n  •  **Syntax :** `{cmd}buat g` <nama grup>\
        \n  •  **Function : **Membuat grup telegram.\
        \n\n  •  **Syntax :** `{cmd}buat gb` <nama grup>\
        \n  •  **Function : **Membuat Grup bersama bot.\
        \n\n  •  **Syntax :** `{cmd}buat c` <nama channel>\
        \n  •  **Function : **Membuat sebuah Channel.\
    "
    }
)
