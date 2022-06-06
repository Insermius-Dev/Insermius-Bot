import asyncio
import discord
from unicodedata import name
from discord.ext import commands, tasks
from keep_alive import keep_alive
import re
import random
from discord import utils
import os
from random import randint
from dotenv import load_dotenv
import re
from datetime import date, datetime
from babel.dates import format_date
import json
import json as jason
from time import sleep
import sys
from time import sleep
from random import choice
from discord.utils import get
from discord.ext.tasks import loop
from PIL import Image
from discord.utils import get
from discord import Spotify
from osuapi import OsuApi, AHConnector
from asyncpg import UniqueViolationError


load_dotenv()
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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
defenitionmade = False

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    # load all extensions
    bot.load_extension("")
    bot.load_extension("foo")
    # channel and user globals
    global test_server
    global testannounce_role
    global testsuggestion_channel
    global testmember_role
    global test_announce
    global test_audit
    global testmain_channel
    global Emain_channel
    global Emod_channel
    global ezic_server
    global owner
    # gaming globals
    global gaming_server
    global Gmain_channel
    global Gaudit_channel
    global Gsuggestion_channel
    # role globals
    global defenitionmade
    global Ggamer_role
    global Groblox_role
    global Gspiderheck_role
    global Gminecraft_role
    global Gvalorant_role
    global Gkrunker_role
    global Gosu_role
    global defenitionmade
    # channels and users
    test_server = bot.get_guild(974354202430169139)
    testsuggestion_channel = bot.get_channel(974360212033110106)
    test_audit = bot.get_channel(974361855952834621)
    test_announce = bot.get_channel(979306543487025184)
    testmain_channel = bot.get_channel(974354203583606836)
    testannounce_role = test_server.get_role(979447462379003964)
    owner = bot.get_user(737983831000350731)
    gaming_server = bot.get_guild(829026541950206049)
    Gsuggestion_channel = bot.get_channel(968944421481623642)
    Gmain_channel = bot.get_channel(829026542495203390)
    Gaudit_channel = bot.get_channel(975052349666107432)
    Gsuggestion_channel = bot.get_channel(968944421481623642)
    Emain_channel = bot.get_channel(954823151601221712)
    Emod_channel = bot.get_channel(962591528369418240)
    ezic_server = bot.get_guild(954823151139827774)
    # roles
    testmember_role = test_server.get_role(974360634663768085)
    # gaming server gaming roles
    Ggamer_role = gaming_server.get_role(969266703039070278)
    Gspiderheck_role = gaming_server.get_role(975389469018570752)
    Groblox_role = gaming_server.get_role(975389469018570752)
    Gminecraft_role = gaming_server.get_role(969300067590762566)
    Gvalorant_role = gaming_server.get_role(967313889131900959)
    Gkrunker_role = gaming_server.get_role(969299665671577611)
    Gosu_role = gaming_server.get_role(969300757302108160)

    while True:
        statusType = random.randint(0, 1)
        if statusType == 0:
            statusNum = random.randint(0, 10)
            await bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.playing, name=playingStatus[statusNum]
                ),
            )
            await asyncio.sleep(10)
        elif statusType == 1:
            statusNum = random.randint(0, 4)
            await bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching, name=watchingStatus[statusNum]
                ),
            )
            await asyncio.sleep(10)


@bot.command()
@commands.is_owner()
async def reload(ctx):
    try:
        bot.reload_extension("foo")
        bot.reload_extension("funnicommands")
        embed = discord.Embed(
            title="Reload",
            description=f"extension successfully reloaded!",
            color=discord.Colour.light_grey(),
        )
    except:
        embed = discord.Embed(
            title="Err_",
            description=f"Looks like something went wrong!",
            color=discord.Colour.dark_red(),
        )
    await ctx.send(embed=embed)


@bot.command(name="vbux", description="get free vbux")
async def getfreevbux(ctx, ammount):
    try:
        stringedammount = int(ammount)
        if stringedammount <= 0:
            desc = f"{ammount} vbux has been taken from {ctx.author.mention} account!"
        else:
            desc = f"{ammount} vbux has been added to {ctx.author.mention} account!"
    except:
        await ctx.send("Invalid ammount")
        return
    embed = discord.Embed(title="Vbux granted", description=desc, color=discord.Color.blue())
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/fortnite/images/e/eb/V-Bucks_-_Icon_-_Fortnite.png/revision/latest?cb=20170806013747"
    )
    await ctx.send(embed=embed)


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
    if member.guild == ezic_server:
        await Emain_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Emod_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")
    elif member.guild == test_server:
        await testmain_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await test_audit.send(embed=embed)
        await member.add_roles(testmember_role)
        print("Sent message to " + member.name + "\n")


@bot.command()
async def marco(ctx):
    await ctx.send("polo!")


@bot.event
async def on_member_remove(member):

    if member.guild == gaming_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Gaudit_channel.send(embed=embed)
        print("Message sent")
    if member.guild == ezic_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Emod_channel.send(embed=embed)
        print("Message sent")
    elif member.guild == test_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await test_audit.send(embed=embed)
        print("Message sent")


async def wait_and_ban(m: discord.Member):
    print(f"{m.display_name} has been detected playing league of legends")
    await asyncio.sleep(1800)  # 30 (m) x 60 (s) = 1800 nu basic matene vispar lol
    gaming_server: discord.Guild = m.guild
    m: discord.Member = gaming_server.get_member(m.id)
    shall_ban = False
    for (
        a
    ) in m.activities:  # iteretes through his new activities and checks if hes still playing league
        if (
            a.name is not None
        ):  # citadi vins dazriez prosta crasho nu gnjau custom activity kkas idfk ez fix
            if a.name.lower() == "league of legends":
                shall_ban = True  # designate the person for a ban
    if shall_ban:
        print(f"{m.display_name} has been banned from {gaming_server.name}")
        await m.send(
            f"You have been banned from {gaming_server.name} for playing too much League of Legends"
        )
        await gaming_server.ban(m, reason="played league", delete_message_days=0)
        await Gmain_channel.send(
            f"{m.display_name} has been banned from {gaming_server.name} for playing league"
        )
    else:
        print(f"{m.display_name} has closed the game timely")


@bot.event
async def on_member_update(prev, cur):
    for a in cur.activities:
        if cur == owner:
            return
        elif a.name.lower() == "league of legends":
            await wait_and_ban(cur)


@bot.event
async def on_member_update(prev, cur):

    if cur == bot.user:
        return
    else:
        if cur.activity is None:
            return
        else:
            useractivity = cur.activity.name.lower()

    if useractivity is not None:
        if prev.activity is None:
            print(f"{cur.name} started playing {useractivity}")

    games = [
        "valorant",
        "minecraft",
        "osu!",
        "krunker",
        "roblox",
        "spiderheck demo",
        "just shapes and beats",
        "fortnite",
        "bloons battles",
        "aim lab",
    ]

    if cur.guild == gaming_server:

        async def give_role(role, member):
            if role in member.roles:
                return
            else:
                await member.add_roles(role)
                print(f"Gave {role.name} role to {member.name}")
                useractivity = None

        if cur.activity and useractivity == games[0]:
            await give_role(Gvalorant_role, cur)
        if cur.activity and useractivity == games[1]:
            await give_role(Gminecraft_role, cur)
        if cur.activity and useractivity == games[2]:
            await give_role(Gosu_role, cur)
        if cur.activity and useractivity == games[3]:
            await give_role(Gkrunker_role, cur)
        if cur.activity and useractivity == games[4]:
            await give_role(Groblox_role, cur)
        if cur.activity and useractivity == games[5]:
            await give_role(Gspiderheck_role, cur)
        if cur.activity and useractivity in games:
            if Ggamer_role in cur.roles:
                useractivity = None
            else:
                await cur.add_roles(Ggamer_role)
                print(f"Gave gamer role to {cur.name}")
                useractivity = None
                await asyncio.sleep(5)


@bot.command(name="rand")
async def randomise(ctx, num1, num2):
    await ctx.send(int(float(random.randint(int(float(num1)), int(float(num2))))))


@bot.command(name="calc")
async def calculate(ctx, operation):
    if re.search("[a-z,A-Z]", operation) is None:
        await ctx.send(eval(operation))
    else:
        await ctx.send("Thats not a mathematical problem...")


@bot.command(name="ping", description="True/False do you want to be pinged for announcments")
async def pinguser(ctx, channel, yn):
    async def takeping():
        if channel == test_announce:
            if testannounce_role not in author.roles:
                await ctx.send("You already dont have this role")
            else:
                await author.remove_roles(testannounce_role)
                await ctx.send("Succesfully removed role")

    async def giveping():
        if channel == test_announce:
            if testannounce_role in author.roles:
                await ctx.send("You already have this role")
            else:
                await author.add_roles(testannounce_role)
                await ctx.send("Role added succesfully")

    if ctx.guild == test_server:
        global author
        author = ctx.author
        if channel == "server-announcments" or "server":
            channel = test_announce
        else:
            await ctx.send("please write a correct channel name!")
            return
        if yn == "False" or yn == "no":
            await takeping()
        elif yn == "True" or yn == "yes":
            await giveping()


@bot.command()
async def spotify(ctx):
    user = ctx.author
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title=f"{user.name}'s Spotify",
                    description="Listening to {}".format(activity.title),
                    color=0x36B357,
                )
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"{user.name}'s Spotify",
            description="Currently not listening anything",
            color=0x36B357,
        )
        await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    channel = message.channel

    if message.content == "YES":
        if message.author == owner:
            channel.send("Yes indeed")

    if message.content == "!help":
        embed = discord.Embed(
            title="Commands",
            description="""
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

    if message.channel == testsuggestion_channel:
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

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

    elif message.content == "!quit REPL":
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

    await bot.process_commands(message)


@bot.command(name="vd")
async def nameday(ctx):
    today = date.today().strftime("%m-%d")
    embed = discord.Embed(
        title="Šodien vārda dienu svin:",
        description=", ".join(namedays[today]),
        color=discord.Color.from_rgb(255, 13, 13),
    )
    embed.set_thumbnail(url="https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png")
    await ctx.send(embed=embed)


@bot.command(name="cf")
async def coinflip(ctx):
    randomnumber = randint(1, 1000)
    if randomnumber == 1:
        embed = discord.Embed(
            title="Tie!",
            description=ctx.author.mention + " flipped heads.",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
        await ctx.send(embed=embed)
    elif randomnumber >= 500:
        embed = discord.Embed(
            title="Tails!",
            description=ctx.author.mention + " flipped tails.",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
        await ctx.send(embed=embed)
    elif randomnumber <= 501:
        embed = discord.Embed(
            title="Heads!",
            description=ctx.author.mention + " flipped tails.",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
        await ctx.send(embed=embed)


@bot.command(name="getvd")
async def getnameday(ctx, name):
    nday = None
    for k in namedays.keys():
        v = namedays[k] + namedays_ext[k]
        if name in v:
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
                description=f"{name} vārda dienu svin {nday_text}",
                color=discord.Color.from_rgb(255, 13, 13),
            )
            embed.set_thumbnail(
                url="https://freeiconshop.com/wp-content/uploads/edd/calendar-flat.png"
            )
            await ctx.send(embed=embed)
            break

    if nday is None:
        embed = discord.Embed(
            title="Error_",
            description=f"Kalendārā neatradu '{name}'",
            color=discord.Color.from_rgb(255, 13, 13),
        )
        embed.set_thumbnail(url="https://hotemoji.com/images/emoji/g/14kioe01bpckzg.png")
        await ctx.send(embed=embed)


@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")


@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile."
                )
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if (
            board[condition[0]] == mark
            and board[condition[1]] == mark
            and board[condition[2]] == mark
        ):
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


async def check_for_birthday(self):
    await self.wait_until_ready()
    now = datetime.datetime.now()
    curmonth = now.month
    curday = now.day

    while not self.is_closed():
        with open("birthdays.json", "r") as f:
            var = jason.load(f)
            for member in var:
                if member["month"] == curmonth:
                    if member["day"] == curday:
                        try:
                            await bot.get_user(member).send("Happy birthday!")
                        except:
                            pass
                        success = False
                        index = 0
                        while not success:
                            try:
                                await test_server.channels[index].send(
                                    f"Happy birthday to <@{member}>!"
                                )
                            except discord.Forbidden:
                                index += 1
                            except AttributeError:
                                index += 1
                            except IndexError:
                                # if the server has no channels, doesn't let the bot talk, or all vc/categories
                                pass
                            else:
                                success = True
        await asyncio.sleep(86400)  # task runs every day


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count):
    try:
        await ctx.channel.purge(limit=int(count) + 1)
    except:
        await ctx.send("Please input a string!")


intents = discord.Intents.default()
intents.members = True
keep_alive()
secret_TOKEN = os.environ["TOKEN"]
bot.run(secret_TOKEN)
