import asyncio
import os
import time
from urllib.request import urlretrieve
from asyncio import get_event_loop
from functools import partial

import requests as r
from pyrogram import Client, filters
from youtubesearchpython import SearchVideos

import wget
import os, pytube, requests
from pyrogram import *
from pyrogram.types import *
from youtube_search import YoutubeSearch
from pytube import YouTube
from Himiko import *
from yt_dlp import YoutubeDL

from config import CMD_HANDLER as cmd
from Himiko.helpers.basic import edit_or_reply

from .help import add_command_help

#Credits BY.Tomi

CAPTION_TEXT = """
<b>• Names:</b> `{}'
<b>• Duration:</b> '{}'
"""

CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("+ News", url="https://t.me/HimikoSupportChat")]])

def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))

async def downloadsong(m, message, vid_id):
   try: 
    m = await m.edit(text = f"📥 **Upload Started**",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📥 Downloading...", callback_data="progress")]]))
    link =  YouTube(f"https://youtu.be/{vid_id}")
    thumbloc = link.title + "thumb"
    thumb = requests.get(link.thumbnail_url, allow_redirects=True)
    open(thumbloc , 'wb').write(thumb.content)
    songlink = link.streams.filter(only_audio=True).first()
    down = songlink.download()
    first, last = os.path.splitext(down)
    song = first + '.mp3'
    os.rename(down, song)
    m = await m.edit(text = """
📤 **Upload Started**
  """,
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📤 Uploading...", callback_data="progress")]]))
    await message.reply_audio(song,
    caption = CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else "Anonymous Admin", "Youtube"),
    thumb = thumbloc,
    reply_markup = CAPTION_BTN)
    await m.delete()
    if os.path.exists(song):
        os.remove(song)
    if os.path.exists(thumbloc):
        os.remove(thumbloc)
   except Exception as e:
       await m.edit(f"There is an error. ⚠️ \nYou can also get help from @d4msy or @HimikoSupportChat.\n\n{str(e)}")

async def downlodvideo(m, message, vid_id):
   try: 
    m = await m.edit(text = "📥 Downloading...",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📥 Downloading...", callback_data="progress")]]))
    link =  YouTube(f"https://youtu.be/{vid_id}")
    videolink = link.streams.get_highest_resolution()
    video = videolink.download()
    m = await m.edit(text = "📤 Uploading...",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📤 Uploading...", callback_data="progress")]]))
    await message.reply_video(video, 
    caption=CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else "Anonymous Admin", "Youtube"),
    reply_markup=CAPTION_BTN)
    await m.delete()
    if os.path.exists(video):
            os.remove(video)
   except Exception as e:
       await m.edit(f"`There is an error. ⚠️ \nYou can also get help from @d4msy or @HimikoSupportChat.\n\n{str(e)}`")


@Client.on_message(filters.command(["song"], cmd) & filters.me)
async def yt_audio(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>Audio not found</b>\nPlease enter the song title correctly.",
        )
    infomsg = await message.reply_text("<b>🔍 Searching...</b>", quote=False)
    try:
        search = SearchVideos(str(message.text.split(None, 1)[1]), offset=1, mode="dict", max_results=1).result().get("search_result")
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 Searching...\n\n❌ Error: {error}</b>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<b>📥 Downloader...</b>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg" 
    except Exception as error:
        return await infomsg.edit(f"<b>📥 Downloader...\n\n❌ Error: {error}</b>")
    thumbnail = wget.download(thumbs)
    await client.send_audio(
        message.chat.id,
        audio=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        caption="<b>Song Informasi {}</b>\n\n<b>• Names:</b> {}\n<b>• Duration:</b> {}\n<b>• Views:</b> {}\n<b>• Channel:</b> {}\n<b>• Linked:</b> <a href={}>Youtube</a>\n\n<b>• Powered By:</b> {}".format(
            "Audio",
            title,
            duration,
            views,
            channel,
            url,
            app.me.mention,
        ),
        reply_to_message_id=message.id,
    )
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)

@Client.on_message(filters.command(["vid", "vsong"], cmd) & filters.me)
async def yt_video(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>Videos not found</b>\nPlease enter the video title correctly.",
        )
    infomsg = await message.reply_text("<b>🔍 Searching...</b>", quote=False)
    try:
        search = SearchVideos(str(message.text.split(None, 1)[1]), offset=1, mode="dict", max_results=1).result().get("search_result")
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 Searching...\n\n❌ Error: {error}</b>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<b>📥 Downloader...</b>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg" 
    except Exception as error:
        return await infomsg.edit(f"<b>📥 Downloader...\n\n❌ Error: {error}</b>")
    thumbnail = wget.download(thumbs)
    await client.send_video(
        message.chat.id,
        video=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption="<b>Video Informasi {}</b>\n\n<b>• Names:</b> {}\n<b>• Duration:</b> {}\n<b>• Views:</b> {}\n<b>• Channel:</b> {}\n<b>• Linked:</b> <a href={}>Youtube</a>\n\n<b>• Powered By:</b> {}".format(
            "video",
            title,
            duration,
            views,
            channel,
            url,
            app.me.mention,
        ),
        reply_to_message_id=message.id,
    )
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)
            
            


add_command_help(
    "youtubedl",
    [
        ["song [query]", "Download Audio From YouTube."],
        [
            "vsong [query]",
            "Download Video from YouTube ",
        ],
    ],
)
