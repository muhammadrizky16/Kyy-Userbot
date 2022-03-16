from userbot.utils import edit_or_reply, kyy_cmd
from userbot import CMD_HELP, bot, CMD_HANDLER as cmd


# Port By @VckyouuBitch From GeezProject
# Untuk Siapapun Yang Hapus Credits Ini, Kamu Anjing:)
@kyy_cmd(pattern="tmsg (.*)")
async def _(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await edit_or_reply(event, f"Total Message Dari {u}. Total Chats `{a.total}`")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=u)
    await edit_or_reply(event, f"Total Message Dari {u}. Total Chats `{a.total}`")

CMD_HELP.update(
    {
        "totalmsg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}tmsg` | `{cmd}tmsg` <username>\
    \n↳ : Mengembalikan jumlah pesan total pengguna dalam obrolan saat ini."
    }
)
