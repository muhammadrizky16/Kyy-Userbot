# OWN MY CODE RENDY
# Credits Rendy

""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import random
from userbot.events import register

# OWN BY RENDY CODE
# CPING

cping = [
    "**Hadir cping** `100.699` ",
    "**Hadir speed** `999.999` ",
    "**Hadir boosted** `565.930` ",
    "**Hadir pingers power** `789.666` ",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=1663258664, pattern=r"^.cping$")
async def _(rendy):
    await kyy.reply(random.choice(cping))
