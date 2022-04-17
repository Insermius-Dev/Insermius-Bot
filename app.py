import asyncio
from unicodedata import name
from discord.ext import commands, tasks
import random
from discord import utils
import os
from dotenv import load_dotenv
import re
from datetime import date, datetime
from babel.dates import format_date
import json
import time
from time import sleep
import discord
#from keep_alive import keep_alive
from random import choice
from discord.utils import get
from discord.ext.tasks import loop

load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

playingStatus = ['Bloons TD 6', 'Celeste', 'Cuphead', "Five nights at Freddy's", 'Just shapes and beats', 'Minecraft', 'Krunker', 'osu!', 'Rocket Leauge', 'Fortnite','Chess']
watchingStatus = ['Youtube', 'Twitch', 'the stock market', 'birds', 'Anime']

nobit = "<:nobitemoji:965118495702540319>"
unedited_ndaytext = None
main_channel = None
mod_channel = None

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    global main_channel
    global mod_channel
    main_channel = bot.get_channel(829026542495203390)
    mod_channel = bot.get_channel(911718281235279932)
    print(f"\nmain channel is {main_channel.name}, id={main_channel.id}")
    print(f"mod_channel is {mod_channel.name}, id={mod_channel.id}\n")
    chans = bot.get_all_channels()
    while True:
        statusType = random.randint(0, 1)
        if statusType == 0:
            statusNum = random.randint(0, 10)
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=playingStatus[statusNum]))
            print(f'{bot.user} is now playing {playingStatus[statusNum]}')
            await asyncio.sleep(600)
        elif statusType == 1:
            statusNum = random.randint(0, 4)
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=watchingStatus[statusNum]))
            print(f'{bot.user} is now watching {watchingStatus[statusNum]}')
            await asyncio.sleep(600)

with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)  

@bot.event
async def on_member_join(member):
    print("\nRecognised that a member called " + member.name + " joined")
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!",
    color=discord.Color.blue()
    ) # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await main_channel.send(embed=embed)

    embed=discord.Embed(
    title="User "+ member.name +" joined.",
    color=discord.Color.green()
    )
    await mod_channel.send(embed=embed)
    print("Sent message to " + member.name + "\n")

@bot.event
async def on_member_remove(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title=member.name+" left.",
        color=discord.Color.from_rgb(255, 13, 13)
    )
    await mod_channel.send(embed=embed)
    print("Message sent")

@bot.event
async def on_message(message):

    if message.content == "!vd":
        today = date.today().strftime("%m-%d")
        channel = message.channel
        sleep(0.5)
        embed=discord.Embed(
        title="Šodien vārda dienu svin:",
        description=", ".join(namedays[today]),
        color=discord.Color.from_rgb(255, 13, 13)
        )
        embed.set_thumbnail(url='https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png')
        await channel.send(embed=embed)

    elif message.content.startswith("!vd "):
        matches = re.search(r"\!vd (\w+)", message.content)
        if matches:
            find_name = matches.group(1)
            find_name = find_name[0].upper() + find_name[1:]
        else:
            return

        nday = None
        for k in namedays.keys():
            v = namedays[k] + namedays_ext[k]
            if find_name in v:
                nday = datetime.strptime("2000-" + k, "%Y-%m-%d").date()
                nday_text = format_date(date=nday, format="d. MMMM", locale="lv")
                if nday_text.endswith("is"):
                    unedited_ndaytext = nday_text
                    nday_text = nday_text[:-2] + "ī"
                else:
                    unedited_ndaytext = nday_text
                    nday_text = nday_text[:-1] + "ā"
                embed=discord.Embed(
                title=f"{unedited_ndaytext}",
                description=f"{find_name} vārda dienu svin {nday_text}",
                color=discord.Color.from_rgb(255, 13, 13)
                )
                embed.set_thumbnail(url='https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png')
                break
        if nday is None:
            embed=discord.Embed(
            title=f"Kalendārā neatradu '{find_name}'",
            color=discord.Color.from_rgb(255, 13, 13)
            )
            embed.set_thumbnail(url='https://hotemoji.com/images/emoji/g/14kioe01bpckzg.png')

        channel = message.channel
        sleep(0.5)
        await channel.send(embed=embed)

    elif message.content.startswith('$'):
        emojiup = '✅'
        emojidown = '❌'
        emoji1 = '1️⃣'
        emoji2 = '2️⃣'
        emoji3 = '3️⃣'
        emoji4 = '4️⃣'
        emoji5 = '5️⃣'
        if message.content.startswith('$ '):
            await message.add_reaction(emojiup)
            await message.add_reaction(emojidown)
        elif message.content.startswith('$2 '):
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
        elif message.content.startswith('$3 '):
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await message.add_reaction(emoji3)
        elif message.content.startswith('$4 '):
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await message.add_reaction(emoji3)
            await message.add_reaction(emoji4)
        elif message.content.startswith('$5 '):
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await message.add_reaction(emoji3)
            await message.add_reaction(emoji4)
            await message.add_reaction(emoji5)
        else:
            await message.reply('The vote option count must be < 2≤X≤5 > !')
    
    if message.author.id(637978980657659924):
        await message.add_reaction(nobit)
    elif message.author.id(919830575706157076):
        await message.add_reaction(nobit)


intents = discord.Intents.default()
intents.members = True
#keep_alive()
secret_TOKEN = os.environ['CUSTOMCONNSTR_DISCORD_TOKEN']
bot.run(secret_TOKEN)   