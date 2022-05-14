import asyncio
from unicodedata import name
from discord.ext import commands, tasks
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
import discord
import sys
from time import sleep
from random import choice
from discord.utils import get
from discord.ext.tasks import loop
from PIL import Image
from discord.utils import get
from discord import Spotify

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
    # channel and user globals
    global test_server
    global testsuggestion_channel
    global testmember_role
    global test_audit
    global testmain_channel
    global Emain_channel
    global Emod_channel
    global ezic_server
    global Ez_server
    global Ezwelcome_channel
    global Ezaudit_channel
    global Ezsuggestion_channel
    global owner
    # gaming globals
    global gaming_server
    global Gmain_channel
    global Gaudit_channel
    global Gsuggestion_channel
    # role globals
    global defenitionmade
    global Ggamer_role
    global Gminecraft_role
    global Gvalorant_role
    global Gkrunker_role
    global Gosu_role
    global defenitionmade
    global Ezvalorant_role
    global Ezgaming_role
    global Ezminecraft_role
    global Ezosu_role
    # channels and users
    test_server = bot.get_guild(974354202430169139)
    testsuggestion_channel = bot.get_channel(974360212033110106)
    test_audit = bot.get_channel(974361855952834621)
    testmain_channel = bot.get_channel(974354203583606836)
    owner = bot.get_user(737983831000350731)
    gaming_server = bot.get_guild(829026541950206049)
    Ezaudit_channel = bot.get_channel(966768248416768010)
    Ezwelcome_channel = bot.get_channel(905476394677587968)
    Ezsuggestion_channel = bot.get_channel(967367286497361970)
    Gsuggestion_channel = bot.get_channel(968944421481623642)
    Gmain_channel = bot.get_channel(829026542495203390)
    Gaudit_channel = bot.get_channel(975052349666107432)
    Gsuggestion_channel = bot.get_channel(968944421481623642)
    Emain_channel = bot.get_channel(954823151601221712)
    Emod_channel = bot.get_channel(962591528369418240)
    ezic_server = bot.get_guild(954823151139827774)
    Ez_server = bot.get_guild(905462820009828352)
    # roles
    testmember_role = test_server.get_role(974360634663768085)
    # gaming server gaming roles
    Ggamer_role = gaming_server.get_role(969266703039070278)
    Gminecraft_role = gaming_server.get_role(969300067590762566)
    Gvalorant_role = gaming_server.get_role(967313889131900959)
    Gkrunker_role = gaming_server.get_role(969299665671577611)
    Gosu_role = gaming_server.get_role(969300757302108160)
    # ez server gaming roles
    Ezvalorant_role = Ez_server.get_role(973944584914731030)
    Ezgaming_role = Ez_server.get_role(973945427760132186)
    Ezminecraft_role = Ez_server.get_role(973982347928145940)
    Ezosu_role = Ez_server.get_role(973993664953081856)
    # print all channels and ids
    print(f"\n gamer role is {Ggamer_role.name}, id={Ggamer_role.id}")
    print(f" minecraft role is {Gminecraft_role.name}, id={Gminecraft_role.id}")
    print(f" valorant role is {Gvalorant_role.name}, id={Gvalorant_role.id}")
    print(f" krunker role is {Gkrunker_role.name}, id={Gkrunker_role.id}")
    print(f" osu role is {Gosu_role.name}, id={Gosu_role.id}")
    print(f"\n Ez welcome_channel is {Ezwelcome_channel.name}, id={Ezwelcome_channel.id}")
    print(f" Ez suggestion_channel is {Ezsuggestion_channel.name}, id={Ezsuggestion_channel.id}")
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
            await asyncio.sleep(600)
        elif statusType == 1:
            statusNum = random.randint(0, 4)
            await bot.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(
                    type=discord.ActivityType.watching, name=watchingStatus[statusNum]
                ),
            )
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
    if member.guild == ezic_server:
        await Emain_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Emod_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")
    elif member.guild == Ez_server:
        await Ezwelcome_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await Ezaudit_channel.send(embed=embed)
        print("Sent message to " + member.name + "\n")
    elif member.guild == test_server:
        await testmain_channel.send(embed=embed)
        embed = discord.Embed(title="User " + member.name + " joined.", color=discord.Color.green())
        await test_audit.send(embed=embed)
        await member.add_roles(testmember_role)
        print("Sent message to " + member.name + "\n")


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
    elif member.guild == Ez_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await Ezaudit_channel.send(embed=embed)
        print("Message sent")
    elif member.guild == test_server:
        print("Recognised that a member called " + member.name + " left")
        embed = discord.Embed(
            title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
        )
        await test_audit.send(embed=embed)
        print("Message sent")


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
        if cur.activity and useractivity in games:
            if Ggamer_role in cur.roles:
                useractivity = None
            else:
                await cur.add_roles(Ggamer_role)
                print(f"Gave gamer role to {cur.name}")
                useractivity = None
                await asyncio.sleep(5)

    if cur.guild == Ez_server:

        async def give_role(role, member):
            if role in member.roles:
                return
            else:
                await member.add_roles(role)
                print(f"Gave {role.name} role to {member.name}")
                useractivity = None

        if cur.activity and useractivity == games[0]:
            await give_role(Ezvalorant_role, cur)

        if cur.activity and useractivity == games[1]:
            await give_role(Ezminecraft_role, cur)

        if cur.activity and useractivity == games[2]:
            await give_role(Ezosu_role, cur)

        if cur.activity and useractivity in games:
            if Ezgaming_role in cur.roles:
                useractivity = None
            else:
                await cur.add_roles(Ezgaming_role)
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

    if message.channel == Ezsuggestion_channel:
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

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
    randomnumber = randint(1, 2)
    if randomnumber == 1:
        embed = discord.Embed(
            title="Heads!",
            description=ctx.author.mention + " flipped heads.",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(url="https://c.tenor.com/pPYpISB14vwAAAAM/coin.gif")
        await ctx.send(embed=embed)
    elif randomnumber == 2:
        embed = discord.Embed(
            title="Tails!",
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


@bot.command()
async def setbirthday(ctx, msg):
    """Set a birthday."""
    member = ctx.message.author.id
    await ctx.send("What is your birthday? Please use MM/DD format.")

    def check(user):
        return user == ctx.message.author and user == ctx.message.channel

    #   msg = await bot.wait_for("message", check=check)
    try:
        list = msg.split("/")
        print(list)
        list[0] = int(list[0])
        list[1] = int(list[1])
        print(list)
        if list[0] > 13 or list[0] < 1:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
        else:
            pass

        if list[0] in (1, 3, 5, 7, 8, 10, 12):
            if list[1] > 31 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] in (4, 6, 9, 11):
            if list[1] > 30 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] == 2:
            if list[1] > 29 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        else:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
    except:
        print("faill")
        await ctx.send("Invalid date.")
        await ctx.send("Aborting...")
        return

    list = msg.split("/")
    month = list[0]
    day = list[1]

    with open("C:/Users/LarssJ/Desktop/Larss_Python_projects/Larss_Bot/birthdays.json", "r+") as f:
        var = jason.load(f)
        var[member] = {"month": month, "day": day}
        jason.dump(var, f, indent=4)


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
# keep_alive()
secret_TOKEN = os.environ["TOKEN"]
bot.run(secret_TOKEN)
