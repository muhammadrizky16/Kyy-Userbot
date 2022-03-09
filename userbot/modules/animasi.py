from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd


@kyy_cmd(pattern='sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    xnxx = await edit_or_reply(typew, "`Pertama-tama kamu cantik`")
    sleep(2)
    await xnxx.edit("`Kedua kamu manis`")
    sleep(1)
    await xnxx.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@kyy_cmd(pattern='punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "`\n┻┳|―-∩`"
                        "`\n┳┻|     ヽ`"
                        "`\n┻┳|    ● |`"
                        "`\n┳┻|▼) _ノ`"
                        "`\n┻┳|￣  )`"
                        "`\n┳ﾐ(￣ ／`"
                        "`\n┻┳T￣|`"
                        "\n**Punten**")

# Create by myself @localheart


@kyy_cmd(pattern='pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "`\n┻┳|―-∩`"
                        "`\n┳┻|     ヽ`"
                        "`\n┻┳|    ● |`"
                        "`\n┳┻|▼) _ノ`"
                        "`\n┻┳|￣  )`"
                        "`\n┳ﾐ(￣ ／`"
                        "`\n┻┳T￣|`"
                        "\n**Masih Ku Pantau**")


# Create by myself @localheart


@kyy_cmd(pattern='idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "\n╭╮╱╱╭╮"
                        "\n┃╰╮╭╯┃"
                        "\n╰╮╰╯╭┻━┳╮╭╮"
                        "\n╱╰╮╭┫╭╮┃┃┃┃"
                        "\n╱╱┃┃┃╰╯┃╰╯┃"
                        "\n╱╱╰╯╰━━┻━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮"
                        "\n┃╭━╮┃"
                        "\n┃┃╱┃┣━┳━━╮"
                        "\n┃╰━╯┃╭┫┃━┫"
                        "\n┃╭━╮┃┃┃┃━┫"
                        "\n╰╯╱╰┻╯╰━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮╱╭╮╱╱╱╭╮"
                        "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                        "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                        "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                        "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                        "\n╰━━━┻━━┻┻━━┻━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━╮╱╭╮"
                        "\n┃┃╰╮┃┃"
                        "\n┃╭╮╰╯┣━━╮"
                        "\n┃┃╰╮┃┃╭╮┃"
                        "\n┃┃╱┃┃┃╰╯┃"
                        "\n╰╯╱╰━┻━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                        "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                        "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                        "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                        "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                        "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update({
    "animasi":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sadboy`\
    \n↳ : Biasalah sadboy hikss\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}punten` dan `.pantau`\
    \n↳ : Coba aja hehehe.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}idiot`\
    \n↳ : u're ediot xixixi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `kosong`\
    \n↳ : Tunggu update selanjutnya kawan."
})
