# credits to userge
# ported to Kyy-Userbot by Kyy
# will be adding more soon
# KONTOLLL

import asyncio
import os
import urllib


from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.spill(?: |$)(.*)")
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Menemukan beberapa payudara besar untukmu 😂")
    await asyncio.sleep(0.5)
    await a.edit("Ini besar banget nih 😂")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


CMD_HELP.update(
    {
        "zonadewasa": "** Plugin :** zonadewasa\
        \n\n  •  Perintah : `.payudara`\
        \n  •  Function : Khusus Sangean\
    "
    }
)
