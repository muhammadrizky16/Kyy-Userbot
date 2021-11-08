import asyncio
import os

import cv2
import PIL
import time

from userbot.events import register
from userbot import CMD_HELP
from userbot.utils import progress

path = "./downloads/"
if not os.path.isdir(path):
    os.makedirs(path)


@register(outgoing=True, pattern='^.rgif(?: |$)(.*)')
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    await event.edit("`Checking...`")
    download = await bot.download_media(reply.media)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    danish = PIL.Image.open("danish.png")
    dark, python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=00ff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""
    await event.edit("```Processing ...```")
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await event.edit("```Uploading...```")
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        "danish.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]")
        ),
    )
    await event.delete()
    os.system("rm -f downloads/*.jpg")
    os.system("rm -f downloads/*.png")
    os.system("rm -f downloads/*.webp")
    os.system("rm -f *.jpg")
    os.system("rm -f *.png")
    os.remove("danish.mp4")


CMD_HELP.update({
    "rgif":
        "`.rgif`\
          \nUsage: Reply a image to convert image to rotate gif."
})
