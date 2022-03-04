from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import io
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd


@kyy_cmd(pattern="itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "sir this is not a image message reply to image message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_delete(event, "sir, This is not a image ")
        return
    chat = "@buildstickerbot"
    xx = await edit_or_reply(event, "Membuat Sticker..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=164977173))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock me (@buildstickerbot) and try again")
            return
        if response.text.startswith("Hi!"):
            await xx.edit("Can you kindly disable your forward privacy settings for good?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


@kyy_cmd(pattern="get$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "`Mohon Maaf, Balas Ke Sticker Terlebih Dahulu.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_delete(event, "`Mohon Maaf, Balas Ke Sticker Terlebih Dahulu.`")
        return
    chat = "@stickers_to_image_bot"
    xx = await edit_or_reply(event, "`Sedang Mengubah Sticker Menjadi Gambar...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Mohon Maaf, Buka Blokir @stickers_to_image_bot Lalu Coba Lagi.")
            return
        if response.text.startswith("I understand only stickers"):
            await xx.edit("`Maaf, Saya Tidak Bisa Mengubah Ini Menjadi Gambar, Periksa Kembali Apakah Itu Sticker Animasi ?`")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            response = await response
            if response.text.startswith("..."):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=611085086))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_message(event.chat_id, [msg.id, response.id])
            else:
                await xx.edit("`Tolong Coba Lagi.`")
        await bot.send_read_acknowledge(conv.chat_id)


@kyy_cmd(pattern="stoi$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await edit_delete(sticker, "`NULL information to feftch...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await edit_delete(sticker, "`Mohon Maaf, Ini Bukanlah Sticker`")
        return False

    xx = await edit_or_reply(sticker, "`Berhasil Mengambil Sticker Ini !`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await xx.delete()
    return


CMD_HELP.update({"stickers2": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}itos`"
                 "\n↳ : Balas ke sticker atau gambar .itos untuk mengambil sticker bukan ke pack."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}get`"
                 "\n↳ : Balas ke sticker untuk mendapatkan file 'PNG' sticker."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stoi`"
                 "\n↳ : Balas Ke sticker untuk mendapatkan file 'PNG' sticker."})
