from userbot.utils import edit_or_reply, kyy_cmd
from userbot import CMD_HELP, bot, CMD_HANDLER as cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError


@kyy_cmd(pattern="detect(?: |$)(.*)")
async def detect(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Please reply to the user or type .detect (ID/Username) that you want to detect.```")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_or_reply(event, "`Please Give ID/Username to Find History.`"
                                    )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    await edit_or_reply(event, "`Currently Doing Account Detection...`")
    await edit_or_reply(event, "__Checking.__")
    await edit_or_reply(event, "__Checking..__")
    await edit_or_reply(event, "__Checking...__")
    await edit_or_reply(event, "__Checking.__")
    await edit_or_reply(event, "__Checking..__")
    await edit_or_reply(event, "__Checking...__")
    await edit_or_reply(event, "__Connecting.__")
    await edit_or_reply(event, "__Connecting..__")
    await edit_or_reply(event, "__Connecting...__")
    await edit_or_reply(event, "__Connecting.__")
    await edit_or_reply(event, "__Connecting..__")
    await edit_or_reply(event, "__Connecting...__")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await edit_or_reply(event,
                                "```Please Unblock @tgscanrobot And Try Again.```"
                                )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await edit_or_reply(event, response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CMD_HELP.update({
    "detection":
        f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}detect`\
          \n📌 : Melihat Riwayat Grup Yang Pernah/Sedang dimasuki."
})
