from userbot import owner, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyy_cmd


@kyy_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@kyy_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@kyy_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@kyy_cmd(pattern="perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {owner}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update({
    "gabut": f"**Modules** - `Gabut`\
    \n\n Cmd : `{cmd}l`\
    \nUsage : Untuk Menjawab Salam\
    \n\n Cmd : `{cmd}perkenalan`\
    \nUsage : Memperkenalkan Diri\
    \n\n Cmd : `{cmd}p`\
    \nUsage : Untuk Memberi Salam."
})
