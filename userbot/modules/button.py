# Copyright (C) 2020  sandeep.n(π.$)
# button post makker for catuserbot thanks to uniborg for the base
# by @sandy1709 (@mrconfused)
# Man-Userbot

import re

from telethon import Button

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_delete, kyy_cmd, reply_id

# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@kyy_cmd(pattern="button(?:\\s|$)([\\s\\S]*)")
async def _(event):
    reply_to_id = await reply_id(event)
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(
            event, "**Teks apa yang harus saya gunakan di pesan button?**"
        )
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


CMD_HELP.update(
    {
        "button": f"**Plugin : **`button`\
        \n\n  •  **Syntax :** `{cmd}button` <text> [Name on button]<buttonurl:link you want to open>\
        \n  •  **Function : **Untuk membuat pesan button melalui inline\
        \n  •  **Examples : **`{cmd}button test [google]<buttonurl:https://www.google.com> [Channel]<buttonurl:https://t.me/NastyProject:same> [Support]<buttonurl:https://t.me/NastySupportt>`\
    "
    }
)
