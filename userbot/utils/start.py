from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await startupmessage(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption="✨ **Kyy Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @NastyProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/NastySupportt"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
