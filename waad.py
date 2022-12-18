import telethon
from telethon import events
from config import *
import asyncio
from help import *


@بحر سيد.on(events.NewMessage(outgoing=True, pattern=r"\.وعد"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit(waad)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@بحر سيد.on(events.NewMessage(outgoing=True, pattern=r"\.كلمات وعد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            if ispay[0] == 'no':
                break
            chat = event.chat_id
            await sedthon.send_message(chat, 'كلمات')
            await asyncio.sleep(0.5)
            masg = await sedthon.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
            if len(masg) == 2:
                msg = masg[0]
                await sedthon.send_message(chat, msg)
            else:
                msg = masg[0] + " " + masg[1]
                await sedthon.send_message(chat, msg)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

# ↢ ()


@بحر سيد.on(events.NewMessage(outgoing=True, pattern=r"\.استثمار وعد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            if ispay[0] == 'no':
                break
            chat = event.chat_id
            await sedthon.send_message(chat, 'فلوسي')
            await asyncio.sleep(0.5)
            masg = await sedthon.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
            msg = masg[0]
            if int(msg) > 500000000:
                await sedthon.send_message(chat, f"استثمار {msg}")
                await asyncio.sleep(10)
                mssag2 = await sedthon.get_messages(chat, limit=1)
                await mssag2[0].click(text="اي ✅")
            else:
                await sedthon.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(1210)

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
