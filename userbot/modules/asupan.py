# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyy_cmd


@kyy_cmd(pattern=".asupan$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan.**")


@kyy_cmd(pattern="chika$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


@kyy_cmd(pattern="bocil$")
async def _(event):
    try:
        response = requests.get(
            "https://api-alphabot.herokuapp.com/api/asupan/bocil?apikey=Alphabot"
        ).json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video bocil.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
        \n\n  •  **Syntax :** `{cmd}bocil`\
        \n  •  **Function : **Untuk Mengirim video bocil secara random.\
    "
    }
)
