from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.mmk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGAAAA MEMEKNYA ANAK INI!!!!**")


@register(outgoing=True, pattern='^.ek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH KONTOOOLL!!!**")


@register(outgoing=True, pattern='^.ya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAA SAYANG...**")


@register(outgoing=True, pattern='^.asn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAH NGENTOOOT!!!**")


@register(outgoing=True, pattern='^.suci(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU LAMA-LAMA JADI KEK ANAK HARAM, KEKNYA HARUS GUA BAPTIS. SINI LU NGENTOT GUA BAPTIS BIAR SUCI JIWA LO YANG HARAM ITU!!!**")


CMD_HELP.update({
    "toxic3":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.asn`\
\n↳ : Hmmm.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mmk`\
\n↳ : Biasalah.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.suci`\
\n↳ : Baptis.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ek`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ya`\
\n↳ : Yasaja."
})
