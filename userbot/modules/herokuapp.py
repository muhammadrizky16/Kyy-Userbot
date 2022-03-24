"""
   Heroku manager for your userbot
"""

import heroku3
import aiohttp
import math

import os
import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import (
    HEROKU_APP_NAME,
    HEROKU_API_KEY,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    owner,
)
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


"""
   ConfigVars setting, get current var, set var or delete var...
"""


@kyy_cmd(pattern="(get|del) var(?: |$)(\\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await edit_or_reply(var, "`[HEROKU]"
                            "\nHarap Siapkan`  **HEROKU_APP_NAME**.")
        return False
    if exe == "get":
        xx = await edit_or_reply(var, "`Mendapatkan Informasi...`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#ConfigVars\n\n"
                        "**Config Vars**:\n"
                        f"`{variable}` **=** `{heroku_var[variable]}`\n"
                    )
                    await xx.edit("`Diterima Ke BOTLOG_CHATID...`")
                    return True
                else:
                    await xx.edit("`Mohon Ubah BOTLOG Ke True...`")
                    return False
            else:
                await xx.edit("`Informasi Tidak Ditemukan...`")
                return True
        else:
            configvars = heroku_var.to_dict()
            msg = ''
            if BOTLOG:
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**Config Vars**:\n"
                    f"{msg}"
                )
                await xx.edit("`Diterima Ke BOTLOG_CHATID`")
                return True
            else:
                await xx.edit("`Mohon Ubah BOTLOG Ke True`")
                return False
    elif exe == "del":
        xx = await edit_or_reply(var, "`Menghapus Config Vars...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await xx.edit("`Mohon Tentukan Config Vars Yang Mau Anda Hapus`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#MenghapusConfigVars\n\n"
                    "**Menghapus Config Vars**:\n"
                    f"`{variable}`"
                )
            await edit_delete(var, "`Config Vars Telah Dihapus`")
            del heroku_var[variable]
        else:
            await edit_delete(var, "`Tidak Dapat Menemukan Config Vars, Kemungkinan Telah Anda Hapus.`")
            return True


@kyy_cmd(pattern=r'set var (\w*) ([\s\S]*)')
async def set_var(var):
    xx = await edit_or_reply(var, "`Sedang Menyetel Config Vars ヅ`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SetelConfigVars\n\n"
                "**Mengganti Config Vars**:\n"
                f"`{variable}` = `{value}`"
            )
        await xx.edit("`Sedang Di Proses, Mohon Menunggu Dalam Beberapa Detik 😼`")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#MenambahkanConfigVar\n\n"
                "**Menambahkan Config Vars**:\n"
                f"`{variable}` **=** `{value}`"
            )
        await edit_delete(var, "`Menambahkan Config Vars...`")
    heroku_var[variable] = value


"""
    Check account quota, remaining quota, used quota, used app quota
"""


@kyy_cmd(pattern="usage(?: |$)")
async def dyno_usage(dyno):
    """
        Get your account Dyno Usage
    """
    xx = await edit_or_reply(dyno, "`Processing...`")
    await asyncio.sleep(2)
    useragent = (
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/81.0.4044.117 Mobile Safari/537.36'
    )
    user_id = Heroku.account().id
    headers = {
        'User-Agent': useragent,
        'Authorization': f'Bearer {HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session:
        async with session.get(heroku_api + path, headers=headers) as r:
            if r.status != 200:
                await dyno.client.send_message(
                    dyno.chat_id,
                    f"`{r.reason}`",
                    reply_to=dyno.id
                )
                await xx.edit("`Tidak Bisa Mendapatkan Informasi Dyno Anda`")
                return False
            result = await r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - User Quota Limit and Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - User App Used Quota - """
            Apps = result['apps']
            for apps in Apps:
                if apps.get('app_uuid') == app.id:
                    AppQuotaUsed = apps.get('quota_used') / 60
                    AppPercentage = math.floor(
                        apps.get('quota_used') * 100 / quota)
                    break
            else:
                AppQuotaUsed = 0
                AppPercentage = 0

            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)

            await xx.edit(
                "✨ **ɪɴꜰᴏʀᴍᴀsɪ ᴅʏɴᴏ ʜᴇʀᴏᴋᴜ :**\n"
                "╔════════════════════╗\n"
                f"• **ᴘᴇɴɢɢᴜɴᴀ ᴅʏɴᴏ sᴀᴀᴛ ɪɴɪ :**\n"
                f"  `{AppHours}`**ᴊᴀᴍ**  `{AppMinutes}`**ᴍᴇɴɪᴛ**  "
                f"**|**  [`{AppPercentage}`**%**]"
                "\n◖════════════════════◗\n"
                "• **sɪsᴀ ᴋᴏᴜᴛᴀ ᴅʏɴᴏ ʙᴜʟᴀɴ ɪɴɪ :**\n"
                f"  `{hours}`**ᴊᴀᴍ**  `{minutes}`**ᴍᴇɴɪᴛ**  "
                f"**|**  [`{percentage}`**%**]\n"
                f"• **ʙᴏᴛ ᴏꜰ :** {owner}  "
                "\n╚════════════════════╝"
            )
            await asyncio.sleep(30)
            await xx.delete()
            return True


@kyy_cmd(pattern="logs")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            "`Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var.`"
        )
    xx = await edit_or_reply(dyno, "`Sedang Mengambil Logs Anda`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await xx.delete()
    await dyno.client.send_file(
        dyno.chat_id,
        file="logs.txt",
        caption="`Ini Logs Heroku anda`",
    )
    return os.remove("logs.txt")


CMD_HELP.update({"herokuapp": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}usage`"
                 "\n↳ : Check Quota Dyno Heroku"
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}logs`"
                 "\n↳ : Melihat Logs Heroku Anda"
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}set var <NEW VAR> <VALUE>`"
                 "\n↳ : Tambahkan Variabel Baru Atau Memperbarui Variabel"
                 "\nSetelah Menyetel Variabel Tersebut, Rose-Userbot Akan Di Restart."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}get var atau .get var <VAR>`"
                 "\n↳ : Dapatkan Variabel Yang Ada, !!PERINGATAN!! Gunakanlah Di Grup Privasi Anda."
                 "\nIni Mengembalikan Semua Informasi Pribadi Anda, Harap berhati-hati."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}del var <VAR>`"
                 "\n↳ : Menghapus Variabel Yang Ada"
                 "\nSetelah Menghapus Variabel, Bot Akan Di Restart."})
