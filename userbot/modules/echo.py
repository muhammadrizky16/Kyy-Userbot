# Thanks Sandy
# Recode By Apis
# fixes by : @pikyus1 / sendi

from userbot import CMD_HELP
from userbot.events import register

from userbot.utils import edit_delete, edit_or_reply
from userbot.modules.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    get_echos,
    is_echo,
    remove_all_echos,
    remove_echo,
    remove_echos,
)
from userbot.utils.events import get_user_from_event


@register(outgoing=True, pattern=r"^.addecho(?: |$)(.*)")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await event.edit("`Balas pesan Pengguna untuk menggemakan pesannya.`")
    roseevent = await event.edit("`Tambahkan Echo ke pengguna...`")
    user, rank = await get_user_from_event(event, roseevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = event.chat.title
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if is_echo(chat_id, user_id):
        return await event.edit("`Pengguna sudah diaktifkan dengan echo.`")
    try:
        addecho(
            chat_id,
            user_id,
            chat_name,
            user_name,
            user_username,
            chat_type)
    except Exception as e:
        await event.edit("**Error:**\n`{str(e)}`")
    else:
        await event.edit("`Berhasil`")


@register(outgoing=True, pattern=r"^.rmecho(?: |$)(.*)")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await event.edit("`Balas pesan Pengguna untuk menggemakan pesannya.`")
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if is_echo(chat_id, user_id):
        try:
            remove_echo(chat_id, user_id)
        except Exception as e:
            await event.edit("**Error:**\n`{str(e)}`")
        else:
            await event.edit("`Echo Pengguna Telah Dihentikan.`")
    else:
        await event.edit("`Pengguna Tidak Diaktifkan Dengan Echo.`")


@register(outgoing=True, pattern=r"^.delecho(?: |$)(.*)")
async def echo(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = get_all_echos()
        if len(lecho) == 0:
            await event.edit("`Anda belum mengaktifkan echo,setidaknya untuk satu pengguna dalam obrolan apa pun.`")
        try:
            remove_all_echos()
        except Exception as e
            await event.edit("**Error:**\n`{str(e)}`", 10)
        else:
            await event.edit("`Echo Pengguna Telah Dihapus, Untuk Semua Pengguna Yang Diaktifkan Di Semua Obrolan.`"
            )
    else:
        lecho = get_echos(event.chat_id)
        if len(lecho) == 0:
            return await event.edit("`Anda belum mengaktifkan Echo setidaknya untuk satu pengguna dalam obrolan ini.`"
            )
        try:
            remove_echos(event.chat_id)
        except Exception as e
            await event.edit("**Error:**\n`{str(e)}`", 10)
        else:
            await event.edit("`Gema yang dihapus untuk semua pengguna yang diaktifkan dalam obrolan ini.`")


@register(outgoing=True, pattern=r"^.echolist(?: |$)(.*)")
async def echo(event):  # sourcery no-metrics
    input_str = event.pattern_match.group(1)
    private_chats = ""
    event.edit = "**Pengguna yang mengaktifkan Echo:**\n\n"
    if input_str:
        lsts = get_all_echos()
        group_chats = ""
        if len(lsts) > 0:
            for echos in lsts:
                if echos.chat_type == "Personal":
                    if echos.user_username:
                        private_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                    else:
                        private_chats += (
                            f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                        )
                else:
                    if echos.user_username:
                        group_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"
                    else:
                        group_chats += f"☞ [{echos.user_name}](tg://user?id={echos.user_id}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"

        else:
            return await event.edit("`Tidak ada pengguna yang mengaktifkan Echo.`")
        if private_chats != "":
            event.edit += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            event.edit += "**Group Chats**\n" + group_chats
    else:
        lsts = get_echos(event.chat_id)
        if len(lsts) <= 0:
            return await event.edit("`Tidak ada pengguna yang mengaktifkan gema dalam obrolan ini.`")

        for echos in lsts:
            if echos.user_username:
                private_chats += (
                    f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                )
            else:
                private_chats += (
                    f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                )
                event.edit = f"**Pengguna yang mengaktifkan Echo dalam obrolan ini adalah:**\n" + private_chats

    await edit_or_reply(event, event.edit)


@register(incoming=True, disable_edited=True)
async def samereply(event):
    if is_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        await event.reply(event.message)

CMD_HELP.update(
    {
        "echo": "**✘ Plugin :** `Echos`\
        \n\n  •  **Perintah :** `.addecho`\
        \n  •  **Function : **Untuk Menambahkan Echo Pengguna\
        \n\n  •  **Perintah :** `.rmecho`\
        \n  •  **Function : **Untuk Menghentikan Echo Pengguna Dalam 1 Orang\
        \n\n  •  **Perintah :** `.delecho`\
        \n  •  **Function : **Untuk Menghentikan Echo Di Semua Pengguna Obrolan\
        \n\n  •  **Perintah :** `.echolist`\
        \n  •  **Function : **Untuk Melihat Daftar Pengguna Echo Anda\
    "
    }
)
