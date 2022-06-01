#Credit - @coderax copy mat karo yar ganda pat gaya he bana ne me

import re
import sys
import os
import asyncio
from telethon import events
from os import execl
import requests as r




@bot.on(admin_cmd(pattern="fi (.*)"))
async def _(event):
    args = event.pattern_match.group(1)
    print(args)
    args = args.split()
    delay = float(args[0])
    
    
    await edit_delete(event,"`Ok..`")

    while True:
        await event.client.send_message(event.chat_id,f"/guess")
        await asyncio.sleep(delay)
         
