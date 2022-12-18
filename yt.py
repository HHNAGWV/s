from telethon import Button, events
import os
from pytube import YouTube
from youtube_search import YoutubeSearch
import json
from config import *
sedthon.start()


def downloader(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True)[0]
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file


title = []
url = []
user_id = []


@bot.on(events.InlineQuery)
async def _(query):
    user_id.append(query.original_update.user_id)
    keyboard = [
        [Button.inline(title[0], data="F1")],
        [Button.inline(title[1], data="F2")],
        [Button.inline(title[2], data="F3")],
        [Button.inline(title[3], data="F4")],
        [Button.inline(title[4], data="F5")]
    ]
    res = await query.builder.article('Search', text="نتائج البحث : ", buttons=keyboard)
    res = await query.answer([res])


@bot.on(events.CallbackQuery)
async def _(event):
    j = event.original_update.user_id
    if j == user_id[0]:
        data = event.data
        if data == b'F1':
            file = downloader(url[0])
            await sedthon.send_file(event.chat_id, file)
            os.remove(file)
        if data == b'F2':
            file = downloader(url[1])
            await sedthon.send_file(event.chat_id, file)
            os.remove(file)
        if data == b'F3':
            file = downloader(url[2])
            await sedthon.send_file(event.chat_id, file)
            os.remove(file)
        if data == b'F4':
            file = downloader(url[3])
            await sedthon.send_file(event.chat_id, file)
            os.remove(file)
        if data == b'F5':
            file = downloader(url[4])
            await sedthon.send_file(event.chat_id, file)
            os.remove(file)
    else:
        pass
    title.clear()
    url.clear()


@بحر سيد.on(events.NewMessage(outgoing=True, pattern="\.بحث (.*)"))
async def _(event):
    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 0)
    name = str(msg[0])
    results = YoutubeSearch(name, max_results=5).to_json()
    results_dict = json.loads(results)
    title.clear()
    url.clear()
    user_id.clear()
    for v in results_dict['videos']:
        title.append(str(v['title']))
        url.append(f'https://www.youtube.com' + v['url_suffix'])
    res = await sedthon.inline_query(f"@{BOT_USERNAME}", 'search')
    await res[0].click(event.chat_id)
    await event.delete()
