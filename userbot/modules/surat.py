from time import sleep

from userbot import CMD_HELP, CMD HANDLER as cmd
from userbot.utils import kyy_cmd


@kyy_cmd(pattern='alfatihah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**SURAT ALFATIHAH**")
    sleep(1)
    await typew.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await typew.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**māliki yaumid-dīn**")
    sleep(1)
    await typew.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await typew.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await typew.edit("**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**")
    sleep(1)
    await typew.edit("**Amin..**")
# Create by myself @localheart

CMD_HELP.update({
    "surat":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}alfatihah`\
    \n↳ : Surat Alfatihah."
})
