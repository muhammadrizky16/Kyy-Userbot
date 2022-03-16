"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban REASON"""
import asyncio
from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import kyy_cmd
from userbot import BOTLOG_CHATID, bot
# imported from uniborg by @heyworld


@kyy_cmd(pattern="gbanb(?: |$)(.*)")
async def _(event):
    if BOTLOG_CHATID is None:
        await event.edit("Set BOTLOG_CHATID in vars otherwise module won't work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await bot.send_message(
            BOTLOG_CHATID,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**gbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**User gbanned by {owner}**")
    asyncio.sleep(5)
    await event.delete()


@kyy_cmd(pattern="ungbanb(?: |$)(.*)")
async def _(event):
    if BOTLOG_CHATID is None:
        await event.edit("Set BOTLOG_CHATID in vars otherwise module won't work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await bot.send_message(
            BOTLOG_CHATID,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**ungbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**User ungbanned by {owner}**")
    asyncio.sleep(5)
    await event.delete()

CMD_HELP.update({
    "gbanbot": f"`{cmd}gbanb`\
    \nUsage: globally Ban Bot.\
    \n\n`{cmd}ungbanb` :\
    \nUsage: Cancel globally Ban Bot."
})
