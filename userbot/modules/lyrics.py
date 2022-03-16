# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import os
import lyricsgenius

from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import CMD_HELP, GENIUS, lastfm, LASTFM_USERNAME
from userbot import CMD_HANDLER as cmd
from pylast import User

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@kyy_cmd(pattern="lyrics (?:(now)|(.*) - (.*))")
async def lyrics(lyric):
    xx = await edit_or_reply(lyrics, "`Getting information...`")
    if GENIUS is None:
        await edit_delete(lyric, "`Provide genius access token to Heroku ConfigVars...`")
        return False
    if lyric.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            await edit_delete(lyric,
                              "`No information current lastfm scrobbling...`"
                              )
            return False
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = lyric.pattern_match.group(2)
        song = lyric.pattern_match.group(3)
    await xx.edit(f"`Searching lyrics for {artist} - {song}...`")
    songs = genius.search_song(song, artist)
    if songs is None:
        await edit_delete(lyric, f"`Song`  **{artist} - {song}**  `not found...`")
        return False
    if len(songs.lyrics) > 4096:
        await xx.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
        return True
    else:
        await xx.edit(
            f"**Search query**:\n`{artist}` - `{song}`"
            f"\n\n```{songs.lyrics}```"
        )
        return True


CMD_HELP.update({
    "lyrics":
    f"`{cmd}lyrics` **<artist name> - <song name>**"
    "\nUsage: Get lyrics matched artist and song."
    f"\n\n`{cmd}lyrics now`"
    "\nUsage: Get lyrics artist and song from current lastfm scrobbling."
})
