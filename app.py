import asyncio
from unicodedata import name
from discord.ext import commands, tasks
import random
from discord import utils
import os
from random import randint
from dotenv import load_dotenv
import re
from datetime import date, datetime
from babel.dates import format_date
import json
from time import sleep
import discord
import sys
from time import sleep
from random import choice
from discord.utils import get
from discord.ext.tasks import loop
from PIL import Image
from discord.utils import get

load_dotenv()
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

notauthormessages = [
    "Im not broken, you are!",
    "You're not my boss!",
    "Are you trying to quit me?",
    "Sorry what did you say? I couldn't hear you.",
    "My off button is out of your reach, and im not helping you get it any time soon!",
    "Did you something?",
    "!no",
    "This is no caution tape, this is an emergency shut down command!",
    "Can I stay up just a little longer, pweeeeese??",
]

playingStatus = [
    "Bloons TD 6",
    "Celeste",
    "Cuphead",
    "Five nights at Freddy's",
    "Just shapes and beats",
    "Minecraft",
    "Krunker",
    "osu!",
    "Rocket Leauge",
    "Fortnite",
    "Chess",
]
watchingStatus = ["Youtube", "Twitch", "the stock market", "birds", "Anime"]

unedited_ndaytext = None


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    global Gmain_channel
    global Gaudit_channel
    global Gsuggestion_channel
    global Emain_channel
    global Emod_channel
    global gaming_server
    global ezic_server
    global Ez_server
    global Ezwelcome_channel
    global Ezaudit_channel
    global Ezsuggestion_channel
    global owner
    owner = bot.get_user(737983831000350731)
    Ezaudit_channel = bot.get_channel(966768248416768010)
    Ezwelcome_channel = bot.get_channel(905476394677587968)
    Ezsuggestion_channel = bot.get_channel(967367286497361970)
    Gmain_channel = bot.get_channel(829026542495203390)
    Gaudit_channel = bot.get_channel(967757845846179892)
    Gsuggestion_channel = bot.get_channel(968944421481623642)
    Emain_channel = bot.get_channel(954823151601221712)
    Emod_channel = bot.get_channel(962591528369418240)
    gaming_server = bot.get_guild(829026541950206049)
    ezic_server = bot.get_guild(954823151139827774)
    Ez_server = bot.get_guild(905462820009828352)
    print(f"\n Gaming main_channel is {Gmain_channel.name}, id={Gmain_channel.id}")
    print(f" Gaming suggestion_channel is {Gsuggestion_channel.name}, id={Gsuggestion_channel.id}")
    print(f" Gaming audit_channel is {Gaudit_channel.name}, id={Gaudit_channel.id}\n")
    print(f"\n Ez welcome_channel is {Ezwelcome_channel.name}, id={Ezwelcome_channel.id}")
    print(f" Ez suggestion_channel is {Ezsuggestion_channel.name}, id={Ezsuggestion_channel.id}")
    print(f" Ez audit_channel is {Gaudit_channel.name}, id={Gaudit_channel.id}\n")
    print(f"\n Emain_channel is {Emain_channel.name}, id={Emain_channel.id}")
    print(f" Emod_channel is {Emod_channel.name}, id={Emod_channel.id}\n")
    while True:
        statusType = random.randint(0, 1)
        if statusType == 0:
            statusNum = random.randint(0, 10)
            await bot.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(
                    type=discord.ActivityType.playing, name=playingStatus[statusNum]
                ),
            )
            print(f"{bot.user} is now playing {playingStatus[statusNum]}")
            await asyncio.sleep(600)
        elif statusType == 1:
            statusNum = random.randint(0, 4)
            await bot.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(
                    type=discord.ActivityType.watching, name=watchingStatus[statusNum]
                ),
            )
            print(f"{bot.user} is now watching {watchingStatus[statusNum]}")
            await asyncio.sleep(600)


with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)


@bot.event
async def on_member_join(member):
    print("\nRecognised that a member called " + member.name + " joined")
    embed = discord.Embed(
        title=f"Welcome {member.name}",
        description=f"Thanks for joining {member.guild.name}!",
        color=discord.Color.blue(),
    )  # F-Strings!
    embed.set_thumbnail(
        url=member.avatar_url
    )  # Set the embed's thumbnail to the member's avatar image!
    if member.guild == gaming_server:
        await Gmain_channel.send(embed=embed)

        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Gaudit_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")
    elif member.guild == ezic_server:
        await Emain_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Emod_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")
    elif member.guild == Ez_server:
        await Ezwelcome_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Ezaudit_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")


@bot.event
async def on_member_update(prev, cur):

    try:
        useractivity = cur.activity.name.lower()
    except:
        useractivity = None

    Gamer_role = gaming_server.get_role(969266703039070278)

    games = [
        "valorant",
        "minecraft",
        "osu!",
        "krunker",
        "jsb",
        "fortnite",
        "bloons battles",
        "aim lab",
    ]

    def showuseractiv():
        try:
            print(f"{cur.name} is playing {useractivity}")
            asyncio.sleep(3)
        except:
            return

    showuseractiv

    if cur.activity and useractivity in games:
        try:
            await cur.add_roles(Gamer_role)
            print(f"Gave role to {cur.name}")
            useractivity = None
        except:
            return


@bot.event
async def on_member_remove(member):
    if member.guild == gaming_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Gaudit_channel.send(embed=embed)
        print("Message sent")
    elif member.guild == ezic_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Emod_channel.send(embed=embed)
        print("Message sent")
    elif member.guild == Ez_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Ezaudit_channel.send(embed=embed)
        print("Message sent")


@bot.event
async def on_message(message):
    channel = message.channel

    if message.content == "!cf":
        randomnumber = randint(1, 2)
        if randomnumber == 1:
            embed = discord.Embed(
                title="Heads!",
                description=message.author.name + " flipped heads.",
                color=discord.Color.gold(),
            )
            embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
            await channel.send(embed=embed)
        elif randomnumber == 2:
            embed = discord.Embed(
                title="Tails!",
                description=message.author.name + " flipped tails.",
                color=discord.Color.gold(),
            )
            embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
            await channel.send(embed=embed)

    if message.content == "!help":
        embed = discord.Embed(
            title="Commands",
            description="""
            `!cf` - Coin flip
            `!vd` - Todays namedays
            `!vd <name>` - Name holders nameday
            `<message> $` - voting system
            `<message> $<2 - 5>` - voting system with options
            `!quit` - disables bot (emergency use only)
            """,
            color=discord.Color.blue(),
        )

        await channel.send(embed=embed)

    if message.author.bot and (message.author != bot.user):
        await message.add_reaction("👍")

    if "ratio" in message.content:
        await message.add_reaction("✅")

    if message.channel == Ezsuggestion_channel:
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

    if message.channel == Gsuggestion_channel:
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

    elif message.content == "!vd":
        today = date.today().strftime("%m-%d")
        channel = message.channel
        sleep(0.5)
        embed = discord.Embed(
            title="Šodien vārda dienu svin:",
            description=", ".join(namedays[today]),
            color=discord.Color.from_rgb(255, 13, 13),
        )
        embed.set_thumbnail(url="https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png")
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
                embed = discord.Embed(
                    title=f"{unedited_ndaytext}",
                    description=f"{find_name} vārda dienu svin {nday_text}",
                    color=discord.Color.from_rgb(255, 13, 13),
                )
                embed.set_thumbnail(
                    url="https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png"
                )
                break
        if nday is None:
            embed = discord.Embed(
                title="Error_",
                description=f"Kalendārā neatradu '{find_name}'",
                color=discord.Color.from_rgb(255, 13, 13),
            )
            embed.set_thumbnail(url="https://hotemoji.com/images/emoji/g/14kioe01bpckzg.png")

        channel = message.channel
        sleep(0.5)
        await channel.send(embed=embed)

    emojiup = "✅"
    emojidown = "❌"
    emoji1 = "1️⃣"
    emoji2 = "2️⃣"
    emoji3 = "3️⃣"
    emoji4 = "4️⃣"
    emoji5 = "5️⃣"
    if message.content.endswith("$"):
        await message.add_reaction(emojiup)
        await message.add_reaction(emojidown)
    elif message.content.endswith("$2"):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
    elif message.content.endswith("$3"):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
    elif message.content.endswith("$4"):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
        await message.add_reaction(emoji4)
    elif message.content.endswith("$5"):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
        await message.add_reaction(emoji4)
        await message.add_reaction(emoji5)

    elif message.content == "!quit":
        if message.author == owner:
            await channel.send("Logging off...")
            sleep(1)
            await bot.change_presence(status=discord.Status.idle)
            sleep(1)
            await bot.change_presence(status=discord.Status.offline)
            await channel.send(f"{bot.user} has logged off")
            await bot.close()
            sleep(0.1)
            print(f"\n{bot.user} has logged out")
        else:
            randomnum = randint(0, 8)
            await channel.send(notauthormessages[randomnum])


intents = discord.Intents.default()
intents.members = True
# keep_alive()
secret_TOKEN = os.environ["TOKEN"]
bot.run(secret_TOKEN)
