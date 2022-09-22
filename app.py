# Bot made by using NAFF
# pip install git+https://github.com/NAFTeam/NAFF@dev

import naff
from naff import (
    Client,
    Button,
    ButtonStyles,
    CommandTypes,
    slash_command,
    InteractionContext,
    context_menu,
    listen,
    Intents,
    Member,
    Embed,
    slash_option,
    OptionTypes,
    ChannelTypes,
)

from dotenv import load_dotenv
import asyncio
import re
import random
import os
from random import randint
from datetime import date, datetime
from babel.dates import format_date

bot_intents: Intents = Intents.GUILD_PRESENCES | Intents.DEFAULT | Intents.GUILD_MEMBERS

load_dotenv()

bot = Client(sync_interactions=True, intents=bot_intents, send_command_tracebacks=False)

lab = bot.get_guild(974354202430169139)
labsuggestion_channel = bot.get_channel(974360212033110106)
lab_audit = bot.get_channel(974361855952834621)
lab_announce = bot.get_channel(979306543487025184)
labmain_channel = bot.get_channel(974354203583606836)
# labannounce_role = lab.get_role(979447462379003964)
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
# labmember_role = lab.get_role(974360634663768085)
# gaming server gaming roles
# Ggamer_role = gaming_server.get_role(969266703039070278)
# Gspiderheck_role = gaming_server.get_role(975389469018570752)
# Groblox_role = gaming_server.get_role(975389469018570752)
# Gminecraft_role = gaming_server.get_role(969300067590762566)
# Gvalorant_role = gaming_server.get_role(967313889131900959)
# Gkrunker_role = gaming_server.get_role(969299665671577611)
# Gosu_role = gaming_server.get_role(969300757302108160)

# load emojis
spotify_emoji = "<:spotify:985229541482061854>"

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


@listen()
async def on_startup():
    print(f"{bot.user} has connected to Discord!")
    while True:
        await bot.change_presence(
            activity=naff.Activity(
                name=random.choice(playingStatus),
                type=naff.ActivityType.PLAYING,
            )
        )
        asyncio.sleep(60)
    # load all extensions
    # bot.load_extension("funnycommands")
    # bot.load_extension("foo")
    # bot.load_extension("namedays")
    # bot.load_extension("ownercommands")


welcomeguilds = []

welcomechannels = []


@slash_command(
    name="welcome",
    description="Configure the welcome message system",
    sub_cmd_name="message",
    sub_cmd_description="Send `help` for possible placeholders",
)
@slash_option(
    name="channel",
    description="The channel you'd like to send welcome messages in",
    opt_type=OptionTypes.CHANNEL,
    required=True,
)
async def welcome_message(ctx: InteractionContext, channel: OptionTypes.CHANNEL):
    if channel.guild.id in welcomeguilds:
        await ctx.send("This guild is already in the welcome system!")
    elif channel.id in welcomechannels:
        await ctx.send("This channel is already in the welcome message system!")
    else:
        welcomechannels.append(channel.id)
        welcomeguilds.append(channel.guild.id)
        await ctx.send(f"Added {channel.mention} to the welcome message system!")


# @listen()
# async def on_member_add(self, event: AddMember):
#     print("\nRecognised that a member called " + member.name + " joined {guild.name}")
#     member = event.member
#     log_channel = member.guild.get_channel(id)

#     embed = Embed(
#         title=f"Welcome {member.name}",
#         description=f"Thanks for joining {member.guild.name}!",
#         timestamp=datetime.utcnow(),
#         color=0x4D9D54,
#     )
#     embed.set_thumbnail(url=member.avatar.url)
#     await log_channel.send(embed=embed)


@slash_command(name="ping", description="check the bots status")
async def ping(ctx):
    await ctx.send("pong")


# @bot.event
# async def on_member_remove(member):

#     if member.guild == gaming_server:
#         print("Recognised that a member called " + member.name + " left")
#         embed = discord.Embed(
#             title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
#         )
#         await Gaudit_channel.send(embed=embed)
#         print("Message sent")
#     if member.guild == ezic_server:
#         print("Recognised that a member called " + member.name + " left")
#         embed = discord.Embed(
#             title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
#         )
#         await Emod_channel.send(embed=embed)
#         print("Message sent")
#     elif member.guild == test_server:
#         print("Recognised that a member called " + member.name + " left")
#         embed = discord.Embed(
#             title=member.name + " left.", color=discord.Color.from_rgb(255, 13, 13)
#         )
#         await test_audit.send(embed=embed)
#         print("Message sent")


# async def wait_and_ban(m: discord.Member):
#     print(f"{m.display_name} has been detected playing league of legends")
#     await asyncio.sleep(1800)  # 30 (m) x 60 (s) = 1800 nu basic matene vispar lol
#     gaming_server: discord.Guild = m.guild
#     m: discord.Member = gaming_server.get_member(m.id)
#     shall_ban = False
#     for (
#         a
#     ) in m.activities:  # iteretes through his new activities and checks if hes still playing league
#         if (
#             a.name is not None
#         ):  # citadi vins dazriez prosta crasho nu gnjau custom activity kkas idfk ez fix
#             if a.name.lower() == "league of legends":
#                 shall_ban = True  # designate the person for a ban
#     if shall_ban:
#         print(f"{m.display_name} has been banned from {gaming_server.name}")
#         await m.send(
#             f"You have been banned from {gaming_server.name} for playing too much League of Legends"
#         )
#         await gaming_server.ban(m, reason="played league", delete_message_days=0)
#         await Gmain_channel.send(
#             f"{m.display_name} has been banned from {gaming_server.name} for playing league"
#         )
#     else:
#         print(f"{m.display_name} has closed the game timely")


# @bot.event
# async def on_member_update(prev, cur):

#     for a in cur.activities:
#         if cur == owner:
#             return
#         elif a.name.lower() == "league of legends":
#             await wait_and_ban(cur)

#     if cur == bot.user:
#         return
#     else:
#         if cur.activity is None:
#             return
#         else:
#             useractivity = cur.activity.name.lower()

#     if useractivity is not None:
#         if prev.activity is None:
#             print(f"{cur.name} started playing {useractivity}")

#     games = [
#         "valorant",
#         "minecraft",
#         "osu!",
#         "krunker",
#         "roblox",
#         "spiderheck demo",
#         "just shapes and beats",
#         "fortnite",
#         "bloons battles",
#         "aim lab",
#     ]

#     if cur.guild == gaming_server:

#         async def give_role(role, member):
#             if role in member.roles:
#                 return
#             else:
#                 await member.add_roles(role)
#                 print(f"Gave {role.name} role to {member.name}")
#                 useractivity = None

#         if cur.activity and useractivity == games[0]:
#             await give_role(Gvalorant_role, cur)
#         if cur.activity and useractivity == games[1]:
#             await give_role(Gminecraft_role, cur)
#         if cur.activity and useractivity == games[2]:
#             await give_role(Gosu_role, cur)
#         if cur.activity and useractivity == games[3]:
#             await give_role(Gkrunker_role, cur)
#         if cur.activity and useractivity == games[4]:
#             await give_role(Groblox_role, cur)
#         if cur.activity and useractivity == games[5]:
#             await give_role(Gspiderheck_role, cur)
#         if cur.activity and useractivity in games:
#             if Ggamer_role in cur.roles:
#                 useractivity = None
#             else:
#                 await cur.add_roles(Ggamer_role)
#                 print(f"Gave gamer role to {cur.name}")
#                 useractivity = None
#                 await asyncio.sleep(5)


@slash_command(
    name="randomise",
    description="randomise some numbers",
)
@slash_option(
    name="first", required=True, opt_type=OptionTypes.STRING, description="smallest number"
)
@slash_option(
    name="second", required=True, opt_type=OptionTypes.STRING, description="biggest number"
)
async def randomise(ctx, num1, num2):
    try:
        await ctx.send(int(float(random.randint(int(float(num1)), int(float(num2))))))
    except:
        await ctx.send("Something didnt go right. Try a different aproach!")


@slash_command(name="calculate", description="calculate some numbers")
@slash_option(
    name="equasion",
    required=True,
    opt_type=OptionTypes.STRING,
    description="input your math equation",
)
async def calculate(ctx, equasion):
    if re.search("[a-z,A-Z]", equasion) is None:
        await ctx.send(
            f"""
> `{equasion}`
**{eval(equasion)}**
        """
        )
    else:
        await ctx.send("Thats not a math equasion...")


@slash_command("spotify", description="Share what you're listening to!")
@slash_option(
    name="user",
    description="Check what other people are listening to",
    opt_type=OptionTypes.USER,
    required=False,
)
async def spotify(self, ctx: InteractionContext, user: Member.user = None):
    listener = user or ctx.author

    # Get the first activity that contains "Spotify". Return None, if none present.
    spotify_activity = next((x for x in listener.activities if x.name == "Spotify"), None)

    if spotify_activity != None:
        cover = f"https://i.scdn.co/image/{spotify_activity.assets.large_image.split(':')[1]}"
        embed = Embed(
            title=f"{listener.display_name}'s Spotify",
            description="Listening to {}".format(spotify_activity.details),
            color="#36b357",
        )
        # SUGGESTION: instead of "set_thumbnail", use "thumbnail=" in the Embed constructor
        embed.set_thumbnail(url=cover)
        embed.add_field(name="Artist", value=spotify_activity.state)
        embed.add_field(name="Album", value=spotify_activity.assets.large_text)
        await ctx.send(embeds=embed)
    else:
        embed = Embed(
            title=f"{listener.display_name}'s Spotify",
            description="Currently not listening to anything",
            color="#36b357",
        )

    await ctx.send(embeds=embed)


# @bot.event
# async def on_message(message):
#     channel = message.channel

#     if message.content == "YES":
#         if message.author == owner:
#             await channel.send("Yes indeed")

#     if message.content == "!help":
#         embed = discord.Embed(
#             title="Commands",
#             description="""
# `<message> $` - voting system
# `<message> $<2 - 5>` - voting system with options
# `!quit` - disables bot (emergency use only)
#             """,
#             color=discord.Color.blue(),
#         )

#         await channel.send(embed=embed)

#     if "ratio" in message.content:
#         await message.add_reaction("✅")

#     if message.channel == testsuggestion_channel and message.author != bot.user:
#         await message.add_reaction("⬆️")
#         await message.add_reaction("⬇️")

#     emojiup = "✅"
#     emojidown = "❌"
#     emoji1 = "1️⃣"
#     emoji2 = "2️⃣"
#     emoji3 = "3️⃣"
#     emoji4 = "4️⃣"
#     emoji5 = "5️⃣"
#     if message.content.endswith("$"):
#         await message.add_reaction(emojiup)
#         await message.add_reaction(emojidown)
#     elif message.content.endswith("$2"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#     elif message.content.endswith("$3"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#     elif message.content.endswith("$4"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#         await message.add_reaction(emoji4)
#     elif message.content.endswith("$5"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#         await message.add_reaction(emoji4)
#         await message.add_reaction(emoji5)

#     elif message.content == "!quit":
#         if message.author == owner:
#             await channel.send("Logging off...")
#             sleep(1)
#             await bot.change_presence(status=discord.Status.idle)
#             sleep(1)
#             await bot.change_presence(status=discord.Status.offline)
#             await channel.send(f"{bot.user} has logged off")
#             await bot.close()
#             sleep(0.1)
#             print(f"\n{bot.user} has logged out")
#         else:
#             randomnum = randint(0, 8)
#             await channel.send(notauthormessages[randomnum])

#     await bot.process_commands(message)

# @slash_command(
#     name='clear',
#     description='clears messages',

# )
# @Commands.has_permissions(manage_messages=True)
# async def clear(ctx, count):
#     try:
#         await ctx.channel.purge(limit=int(count) + 1)
#     except:
#         await ctx.send("Please input a string!")


secret_TOKEN = os.environ["TOKEN"]
bot.start(secret_TOKEN)
