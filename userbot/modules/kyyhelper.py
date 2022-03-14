""" Userbot module for other small commands. """
from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import kyy_cmd


@kyy_cmd(pattern="lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {owner} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/IDnyaKosong)"
        "\n[Repo](https://github.com/S/Kyy-Userbot)"
        "\n[Instagram](instagram.com/rizkyhamdanii16_)")


@kyy_cmd(pattern="vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {owner}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/muhammadrizky16/Kyy-Userbot/Kyy-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    f"`{cmd}lhelp`\
\nUsage: Bantuan Untuk Kyy-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
