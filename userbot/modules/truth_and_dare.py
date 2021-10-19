import requests

from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import edit_or_reply


@register(outgoing=True, pattern="^.truth$")
async def tede_truth(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Truth**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


@register(outgoing=True, pattern="^.dare$")
async def tede_dare(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Dare**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


CMD_HELP.update({
    "truthdare": f"**Plugin : **`truthdare`\
        \n\n  •  **Syntax :** `.truth`\
        \n  •  **Function : **Untuk tantangan.\
        \n\n  •  **Syntax :** `.dare`\
        \n  •  **Function : **Untuk kejujuran."
})
