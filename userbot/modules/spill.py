# Ported by Fariz (Flicks-Userbot)
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@register(outgoing=True, pattern=r"^\.spill(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan spill...")
    async with bot.conversation("@Spillgame_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1361222893)
            )
            await conv.send_message("/spill")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@Spillgame_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan spill**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "spill": "** Plugin :** spill\
        \n\n  •  Perintah : `.spill`\
        \n  •  Function : Mengirim Pertanyaan Random\
    "
    }
)
