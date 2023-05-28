# Bot originally made by using NAFF
# Ported to i.py v5
# pip install -U discord-py-interactions
bot_official_version = "4.0.0 dev"

import interactions as inter
from interactions import (
    Client,
    Button,
    VoiceState,
    slash_command,
    InteractionContext,
    context_menu,
    listen,
    Intents,
    Member,
    Embed,
    slash_option,
    Color,
    ActionRow,
    ComponentContext,
    spread_to_rows,
    ComponentContext,
    is_owner,
    OptionType,
    Permissions,
    SlashCommandChoice,
    ButtonStyle,
)

import asyncio
import re
import random
import os
from random import randint
from datetime import date, datetime
from babel.dates import format_date
import json
import time
from asyncio import sleep as eep

from dotenv import load_dotenv

load_dotenv()

from Bot_website import start

start()  # starts the website (https://larss-bot.onrender.com)

bot_intents: Intents = Intents.GUILD_PRESENCES | Intents.DEFAULT | Intents.GUILD_MEMBERS

bot = inter.Client(sync_interactions=True, intents=bot_intents, send_command_tracebacks=False)

spotify_emoji = "<:spotify:985229541482061854>"

# notauthormessages = [
#     "Im not broken, you are!",
#     "You're not my boss!",
#     "Are you trying to quit me?",
#     "Sorry what did you say? I couldn't hear you.",
#     "My off button is out of your reach, and im not helping you get it any time soon!",
#     "Did you something?",
#     "!no",
#     "This is no caution tape, this is an emergency shut down command!",
#     "Can I stay up just a little longer, pweeeeese??",
# ]

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

# unedited_ndaytext = None
# defenitionmade = False

epiccontribbutingppl = [
    324352543612469258,
    975738227669499916,
    400713431423909889,
    717769897278570507,
]

lilhelpers = [
    954821934808449125,
    830021857067532349,
    488257154701197322,
]

channel_cooldown = []
invite_cooldown = []
nameday_cooldown = []


# @listen()
# async def on_error():
#     print("Caught an error")
#     os.system("kill 1")


@listen()
async def on_startup():
    print(f"{bot.user} has connected to Discord!")
    # bot.load_extension("data.voice")
    bot.load_extension("data.ext1")  # Load all games
    bot.load_extension("data.tictactoe")
    bot.load_extension("data.ghostgame")
    bot.load_extension("data.lichess")

    global now_unix
    now_unix = time.mktime(datetime.utcnow().timetuple())
    while True:  # Select a random activity, which will change every 60 seconds
        random_activity = randint(1, 3)
        if random_activity == 1:
            await bot.change_presence(
                activity=inter.Activity(
                    name=random.choice(playingStatus),
                    type=inter.ActivityType.PLAYING,
                )
            )
            await asyncio.sleep(60)
        elif random_activity == 2:
            await bot.change_presence(
                activity=inter.Activity(
                    name=random.choice(watchingStatus),
                    type=inter.ActivityType.WATCHING,
                )
            )
            await asyncio.sleep(60)
        elif random_activity == 3:
            if str(len(bot.guilds)).endswith("1") and not str(len(bot.guilds)).endswith("11"):
                await bot.change_presence(
                    activity=inter.Activity(
                        type=inter.ActivityType.STREAMING,
                        url="https://www.twitch.tv/dubiaroach",
                        name="to {0} server".format(len(bot.guilds)),
                    )
                )
            else:
                await bot.change_presence(
                    activity=inter.Activity(
                        type=inter.ActivityType.STREAMING,
                        name="to {0} servers".format(len(bot.guilds)),
                        url="https://www.twitch.tv/dubiaroach",
                    )
                )
            await asyncio.sleep(60)


@is_owner()
@slash_command(
    name="reload",
    description="Reloads a cog",
)
@slash_option(
    name="cog",
    description="The cog to reload",
    opt_type=OptionType.INTEGER,
    choices=[
        # SlashCommandChoice(name="Voice", value=1),
        SlashCommandChoice(name="TicTacToe", value=2),
        SlashCommandChoice(name="GhostGame", value=3),
        SlashCommandChoice(name="Lichess", value=4),
        SlashCommandChoice(name="Ext1", value=5),
    ],
    required=False,
)
async def reload(ctx, cog=None):
    # if cog == 1:
    #     bot.reload_extension("data.voice")
    if cog == 2:
        bot.reload_extension("data.tictactoe")
    elif cog == 3:
        bot.reload_extension("data.ghostgame")
    elif cog == 4:
        bot.reload_extension("data.lichess")
    elif cog == 5:
        bot.reload_extension("data.ext1")

    await ctx.respond("Reloaded cog")


@slash_command(
    name="info",
    description="get info about the bot",
)
async def info(ctx):
    embed = Embed(
        title="Info",
        description="Info about the bot",
        timestamp=datetime.utcnow(),
        color=Color.from_hex("5e50d4"),
        thumbnail="https://cdn.discordapp.com/attachments/983081269543993354/1041045309695987712/image.png",
    )
    embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
    embed.add_field(
        name="Bot Version",
        value=bot_official_version,
    )
    embed.add_field(
        name="Guilds",
        value=f"in {len(bot.guilds)} guilds.",
    )
    embed.add_field(
        name="Created by",
        value="<@737983831000350731>",
    )
    embed.add_field(
        name="Last startup",
        value=f"<t:{int(str(now_unix)[:-2])}:R>",
    )

    btn1 = Button(label="Contributors", style=ButtonStyle.BLUE, emoji="⭐", custom_id="contributors")
    btn2 = Button(
        label="Partnered servers", style=ButtonStyle.BLUE, emoji="🏘", custom_id="guildsinvites"
    )
    components: list[ActionRow] = spread_to_rows(btn1, btn2)

    await ctx.send(embed=embed, components=components)


@listen()
async def on_component(ctx: ComponentContext):
    event = ctx.ctx
    if event.custom_id == "contributors":
        if event.channel.id not in channel_cooldown:
            embed = Embed(
                title="⭐ Contributors",
                description=f"Awesome people who have helped to make Larss_Bot what it is today!",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("5e50d4"),
            )
            embed.set_footer(
                text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url
            )

            value = ""
            for contributor in epiccontribbutingppl:
                value += f"> <@{contributor}> \n"

            embed.add_field(
                name="Contributors",
                value=value,
            )

            value = ""
            for lilhelper in lilhelpers:
                value += f"> <@{lilhelper}> \n"

            embed.add_field(
                name="Little helpers",
                value=value,
            )
            await event.send(embed=embed)
            channel_cooldown.append(event.channel.id)
            await asyncio.sleep(15)
            channel_cooldown.remove(event.channel.id)
        else:
            await event.send(
                "Looks like someone already pressed the button. No need to do it again.",
                ephemeral=True,
            )

    if event.custom_id == "guildsinvites":
        if event.channel.id not in invite_cooldown:
            embed = Embed(
                title="Partner servers",
                description=f"Press any of the buttons below to get invited to one of the partnered servers",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("5e50d4"),
            )
            embed.set_footer(
                text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url
            )

            btn1 = Button(
                style=ButtonStyle.URL,
                label="Dev lab",
                emoji="🧪",
                url="https://discord.gg/TReMEyBQsh",
            )
            btn2 = Button(
                style=ButtonStyle.URL,
                label="Big-Floppa software solutions",
                emoji="🐱",
                url="https://discord.gg/MDVcb8wdUd",
            )
            btn3 = Button(
                style=ButtonStyle.URL,
                label="Tyler army",
                emoji="🐸",
                url="https://discord.gg/w78rcjW8ck",
            )
            components: list[ActionRow] = spread_to_rows(
                btn1,
                btn2,
                btn3,
            )

            await event.send(embed=embed, components=components)
            channel_cooldown.append(event.channel.id)
            await asyncio.sleep(15)
            channel_cooldown.remove(event.channel.id)
        else:
            # ephemeral not gonna work, once again
            await event.send(
                "Looks like someone already pressed the button. No need to do it again.",
                ephemeral=True,
            )
    # if event.custom_id == "extendedlistshow":
    #     if event.channel.id not in nameday_cooldown:
    #         today = date.today().strftime("%m-%d")
    #         embed = Embed(
    #             title="Visi šodienas vārdi",
    #             description="> " + "\n> ".join(namedays_ext[today]),
    #             color=Color.from_rgb(255, 13, 13),
    #         )
    #         await event.send(embed=embed)
    #         nameday_cooldown.append(event.channel.id)
    #         await asyncio.sleep(15)
    #         nameday_cooldown.remove(event.channel.id)
    #     else:
    #         # ephemeral not gonna work, once again
    #         await event.send(
    #             "Looks like someone already pressed the button. No need to do it again.",
    #             ephemeral=True,
    #         )


@listen()
async def on_member_add(event):  # When a user joins
    print("User joined")
    print(event.guild.id)
    with open("data/nowelcome.txt", "r") as f:  # Get all joined users
        lines = f.readlines()
        int_lines = [eval(i) for i in lines]
        f.close
    joiner = event.member
    if event.guild.id in int_lines:  # Check if user already joined
        pass
    elif not event.guild.id in int_lines:
        if joiner.bot:  # Check if a bot joined
            embed = Embed(
                description=f"Application '{joiner.display_name}' was added to the server!",
                color=Color.from_hex("58f728"),
            )

            embed.set_author("Application added", icon_url=joiner.avatar.url)
            await event.guild.system_channel.send(embed=embed)
        else:  # A regular user joined
            embed = Embed(
                title=f"Welcome {joiner.display_name}!",
                description=f"Thanks for joining {joiner.guild.name}!",
                timestamp=datetime.utcnow(),
                color=Color.from_rgb(88, 109, 245),
            )
            embed.set_thumbnail(url=joiner.avatar.url)

            message = await event.guild.system_channel.send(
                f"Welcome {joiner.mention}! :wave: ", embed=embed
            )
            await message.add_reaction("👋")


@listen()
async def on_member_remove(event):  # On member leave
    with open("data/nowelcome.txt", "r") as f:
        lines = f.readlines()
        int_lines = [eval(i) for i in lines]
        f.close()
    leaver = event.member
    if event.guild.id in int_lines:
        pass
    elif leaver == bot.user:
        pass
    elif int(event.guild.id) == 1090004044111696075:
        pass
    elif not event.guild.id in int_lines:
        if leaver.bot:
            embed = Embed(
                description=f"Application '{leaver.display_name}' was removed from the server!",
                color=Color.from_hex("f73528"),
            )

            embed.set_author(f"Application removed", icon_url=leaver.avatar.url)
            await event.guild.system_channel.send(embed=embed)
        else:
            embed = Embed(
                title=f"{leaver.display_name} left.",
                description=f"Sorry to see you go {leaver.display_name}!",
                timestamp=datetime.utcnow(),
                color=Color.from_rgb(255, 13, 13),
            )

            await event.guild.system_channel.send(embed=embed)


@slash_command(name="ping", description="check the bots status")
async def ping(ctx):
    message = await ctx.send(
        """
pong! 🏓
latency: `{0}ms`
    """.format(
            round(bot.latency * 1000, 2)
        )
    )
    await message.add_reaction("🟢")


@slash_command(
    name="randomise",
    description="randomise some numbers",
)
@slash_option(
    name="min",
    required=True,
    opt_type=OptionType.INTEGER,
    description="smallest possible number",
)
@slash_option(
    name="max",
    required=True,
    opt_type=OptionType.INTEGER,
    description="biggest possible number",
)
async def randomise(ctx, min, max):
    try:
        rand = random.randint(min, max)
        await ctx.send(f"> `{min}` - `{max}` \n** {rand} **")

    except:
        if min >= max:
            await ctx.send("The first number must be smaller than the second one!")
        if min == max:
            await ctx.send("The numbers must be different!")
        else:
            await ctx.send("Something didnt go right. Try a different aproach!")


# # @bot.command(
# #     "spotify",
# #     description="Share what you're listening to!",
# #     options=interactions.Option(
# #         name="min",
# #         required=True,
# #         type=interactions.OptionType.STRING,
# #         description="smallest possible number",
# #     ),
# # )
# # async def spotify(ctx: InteractionContext):
# #     listener = ctx.author

# #     # Get the first activity that contains "Spotify". Return None, if none present.
# #     # spotify_activity = next((x for x in listener.activities if x.name == "Spotify"), None)

# #     print(listener.activities)

# #     if listener.activities[name] == "Spotify":
# #         cover = f"https://i.scdn.co/image/{listener.activities.assets.large_image.split(':')[1]}"
# #         embed = Embed(
# #             title=f"{listener.display_name}'s Spotify",
# #             description="Listening to {}".format(listener.activities.details),
# #             color="#36b357",
# #             thumbnail=cover,
# #         )
# #         embed.add_field(name="Artist", value=listener.activities.state)
# #         embed.add_field(name="Album", value=listener.activities.assets.large_text)
# #     else:
# #         embed = Embed(
# #             title=f"{listener.display_name}'s Spotify",
# #             description="Currently not listening to anything",
# #             color="#36b357",
# #             timestamp=datetime.utcnow(),
# #         )
# #     embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
# #     message = await ctx.send(embeds=embed)
# #     await message.add_reaction(spotify_emoji)


# @slash_command("outro", description="Exit a voice channel in style")
# async def outro(ctx: InteractionContext):
#     if not ctx.author.voice:
#         return await ctx.send("You are not in a voice channel")
#     else:
#         await ctx.send("You will be disconnected in 15 seconds!", ephemeral=True)
#         audio = AudioVolume(
#             r"data\xenogenesis-outro-song.mp3",
#         )
#         audio.probe = False
#         await ctx.author.voice.channel.connect(deafened=True)
#         await asyncio.sleep(0.5)
#         ctx.voice_state.play_no_wait(audio)
#         await asyncio.sleep(15)
#         await ctx.author.voice.disconnect()

# #     elif message.content == "!quit":
# #         if message.author == owner:
# #             await channel.send("Logging off...")
# #             sleep(1)
# #             await bot.change_presence(status=discord.Status.idle)
# #             sleep(1)
# #             await bot.change_presence(status=discord.Status.offline)
# #             await channel.send(f"{bot.user} has logged off")
# #             await bot.close()
# #             sleep(0.1)
# #             print(f"\n{bot.user} has logged out")
# #         else:
# #             randomnum = randint(0, 8)
# #             await channel.send(notauthormessages[randomnum])

# #     await bot.process_commands(message)


@is_owner()
@slash_command("quit", description="Log off the bot")
async def quit(ctx: InteractionContext):
    await ctx.send("Logging off...")
    await bot.close()
    await eep(0.1)
    print(f"\n{bot.user} has logged out")


@slash_command(
    name="clear",
    description="clears messages",
    default_member_permissions=Permissions.MANAGE_MESSAGES,
)
@slash_option(
    name="count",
    description="number of messages to clear",
    required=True,
    opt_type=OptionType.INTEGER,
    max_value=15,
    min_value=2,
)
async def clear(ctx, count):
    try:
        await ctx.channel.purge(limit=count + 1)
    except:
        await ctx.send("Please input a string!")


secret_TOKEN = os.environ["TOKEN"]
try:
    bot.start(secret_TOKEN)
except Exception as e:
    os.system("kill 1")
    raise Exception(f"Failed to log in, reason: {e}")
