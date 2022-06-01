import json
import re
import sys
import os
import asyncio
from os import execl
import requests as r
from pyrogram import Client, Filters
from pyrogram import (InlineKeyboardMarkup,
                      InlineKeyboardButton,
                      CallbackQuery)

import functions as func
import raid_dynamax as raid

from Config import Config

app = Client(
    api_id=Config.aid,
    api_hash=Config.ahash,
    bot_token=Config.bot_token,
    session_name='inhunmanDexBot'
)

texts = json.load(open('src/texts.json', 'r'))
data = json.load(open('src/pkmn.json', 'r'))
stats = json.load(open('src/stats.json', 'r'))
jtype = json.load(open('src/type.json', 'r'))

usage_dict = {'vgc': None}
raid_dict = {}

read=r.get("https://gist.githubusercontent.com/nryadav7412/bc797e2fce05ae3913b9aa48f8edb83c/raw/pokemon.txt").text

# ===== Home =====
@app.on_message(Filters.command(['start', 'start@hexa_dex_bot']))
def start(app, message):
    app.send_message(
        chat_id=message.chat.id,
        text=texts['start_message'],
        parse_mode='HTML'
    )

@app.on_message(Filters.command(['po', 'po@hexa_dex_bot']))
def poke(app, message):
    try:
        gtype = message.text.split(' ')[1]
    except IndexError as s:
        app.send_message(
            chat_id=message.chat.id,
            text="Provide A Valid Pokemon Name"
        )
        return
    if "_" not in gtype.lower():
        app.send_message(
            chat_id=message.chat.id,
            text="THAT HINT NOT FROM GUESS"
        )
        return
    toreplace = {"_": ".", " ": ""}
    for key, value in toreplace.items():
        mon = mon.replace(key, value)
    patt = re.compile(mon)
    matches = patt.finditer(read)
    for match in matches:
            app.send_message(
                chat_id=message.chat.id,
                text=match[0],
            )

app.run()
