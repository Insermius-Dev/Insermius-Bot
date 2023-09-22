# Bot originally made by using NAFF
# Ported to i.py v5
# pip install -U discord-py-interactions
bot_official_version = "4.0.0"

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
    check,
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
import pandas as pd
from bs4 import BeautifulSoup as bs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv

load_dotenv()

from Bot_website import start

bot_intents: Intents = Intents.ALL

bot = inter.Client(sync_interactions=True, intents=bot_intents, send_command_tracebacks=False)

notauthormessages = [
    "Im not broken, you are!",
    "You're not my boss!",
    "Are you trying to quit me?",
    "Sorry what did you say? I couldn't hear you.",
    "My off button is out of your reach, and im not helping you get it any time soon!",
    "Did you something?",
    "!yes",
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

url_links_contributors = []
url_links_lilhelpers = []
usernames_contributors = []
usernames_lilhelpers = []

channel_cooldown = []
invite_cooldown = []
nameday_cooldown = []

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)

# @listen()
# async def on_error():
#     print("Caught an error")
#     os.system("kill 1")

delete_btn = Button(style=ButtonStyle.RED, custom_id="delete", emoji="🗑️")

base = os.path.dirname("templates/")
html = open(os.path.join(base, "index.html"))
soup = bs(html, "html.parser")

# for i in range(len(epiccontribbutingppl)):
#     url_links_contributors.append((bot.fetch_user(epiccontribbutingppl[i])).avatar.url)
#     usernames_contributors.append((bot.fetch_user(epiccontribbutingppl[i])).name)

# for id in lilhelpers:
#     url_links_lilhelpers.append((bot.fetch_user(lilhelpers[i])).avatar.url)
#     usernames_lilhelpers.append((bot.fetch_user(lilhelpers[i])).name)

html = f"""
<table>
</table>
"""


@listen()
async def on_startup():
    print(f"{bot.user} has connected to Discord!")
    # bot.load_extension("data.voice")
    bot.load_extension("data.ext1")  # Load all games
    # bot.load_extension("data.tictactoe")
    # bot.load_extension("data.ghostgame")
    bot.load_extension("data.lichess")
    bot.load_extension("data.welcome")
    bot.load_extension("data.spotify")

    # contr_icons = []
    # contr_usernames = []

    # lilhelp_icons = []
    # lilhelp_usernames = []

    # for contributor in epiccontribbutingppl:
    #     contr_icons.append(bot.get_user(contributor).avatar.url)
    #     contr_usernames.append(bot.get_user(contributor).username)

    # for lilhelper in lilhelpers:
    #     lilhelp_icons.append(bot.get_user(lilhelper).avatar.url)
    #     lilhelp_usernames.append(bot.get_user(lilhelper).username)

    # with open("index.html", "wb") as f:
    #     f.write(soup.prettify("utf-8"))

    start()

    guild_list = bot.guilds
    guild_names = []
    guild_members = []
    guild_ids = []

    for i in range(len(guild_list)):
        guild_names.append(guild_list[i].name)
        guild_members.append(guild_list[i].member_count)
        guild_ids.append(guild_list[i].id)

    guild_list = pd.DataFrame({"id": guild_ids, "guild": guild_names, "members": guild_members})
    guild_list.set_index("id", inplace=True)
    print(guild_list)

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
                        url="https://www.twitch.tv/Larss_j",
                        name="to {0} server".format(len(bot.guilds)),
                    )
                )
            else:
                await bot.change_presence(
                    activity=inter.Activity(
                        type=inter.ActivityType.STREAMING,
                        name="to {0} servers".format(len(bot.guilds)),
                        url="https://www.twitch.tv/Larss_j",
                    )
                )
            await asyncio.sleep(60)


@slash_command(
    name="reload",
    description="Reloads a cog",
)
@slash_option(
    name="cog",
    description="The cog to reload",
    opt_type=OptionType.INTEGER,
    choices=[
        SlashCommandChoice(name="Welcome", value=1),
        # SlashCommandChoice(name="TicTacToe", value=2),
        # SlashCommandChoice(name="GhostGame", value=3),
        SlashCommandChoice(name="Lichess", value=4),
        SlashCommandChoice(name="Ext1", value=5),
        SlashCommandChoice(name="Spotify", value=6),
    ],
    required=False,
)
async def reload(ctx, cog=None):
    if bot.owner.id == ctx.author.id:
        if cog == 1:
            bot.reload_extension("data.welcome")
            await ctx.respond("Reloaded `data.welcome`")
        # if cog == 2:
        #     bot.reload_extension("data.tictactoe")
        # elif cog == 3:
        #     bot.reload_extension("data.ghostgame")
        elif cog == 4:
            bot.reload_extension("data.lichess")
            await ctx.respond("Reloaded `data.lichess`")
        elif cog == 5:
            bot.reload_extension("data.ext1")
            await ctx.respond("Reloaded `data.ext1`")
        elif cog == 6:
            bot.reload_extension("data.spotify")
            await ctx.respond("Reloaded `data.spotify`")
        elif cog == None:
            bot.reload_extension("data.welcome")
            # bot.reload_extension("data.tictactoe")
            # bot.reload_extension("data.ghostgame")
            bot.reload_extension("data.lichess")
            bot.reload_extension("data.ext1")
            await ctx.respond("Reloaded all cogs")
    else:
        await ctx.respond(random.choice(notauthormessages), ephemeral=True, components=[delete_btn])


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
        url="https://larss-bot.onrender.com",
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
    embed.add_field(
        name="Support the creator!",
        value="https://ko-fi.com/larssj",
    )

    btn1 = Button(label="Contributors", style=ButtonStyle.BLUE, emoji="⭐", custom_id="contributors")
    btn2 = Button(
        label="Partnered servers", style=ButtonStyle.BLUE, emoji="🏘", custom_id="guildsinvites"
    )
    components: list[ActionRow] = spread_to_rows(btn1, btn2)
    components.append(ActionRow(delete_btn))

    await ctx.send(embed=embed, components=components)


@listen()
async def on_component(ctx: ComponentContext):
    event = ctx.ctx
    match event.custom_id:
        case "contributors":
            message_components = event.message.components
            message_components[0].components[0].disabled = True
            await event.message.edit(components=message_components)

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
            await event.send(embed=embed, components=[delete_btn])

        case "guildsinvites":
            message_components = event.message.components
            message_components[0].components[1].disabled = True
            await event.message.edit(components=message_components)

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
            components: list[ActionRow] = spread_to_rows(btn1, btn2, btn3)
            components.append(ActionRow(delete_btn))

            await event.send(embed=embed, components=components)
        case "extendedlistshow":
            today = date.today().strftime("%m-%d")
            embed = Embed(
                title="Visi šodienas vārdi",
                description="> " + "\n> ".join(namedays_ext[today]),
                color=Color.from_rgb(255, 13, 13),
            )

            message_components = event.message.components
            message_components[0].components[0].disabled = True
            await event.message.edit(components=message_components)

            await event.send(embed=embed, components=[delete_btn])

        case "delete":
            if event.author.id == 494795032717426688:
                await event.send("FUCK YOU!! YOU CANT DO THIS!!", ephemeral=True)
            else:
                try:
                    if (
                        event.message.interaction._user_id == event.author.id
                        or event.author.has_permission(Permissions.MANAGE_MESSAGES)
                    ):
                        await event.message.delete()
                    else:
                        await event.send("Not your interaction.", ephemeral=True)
                except:
                    if event.author.has_permission(Permissions.MANAGE_MESSAGES):
                        await event.message.delete()
                    else:
                        await event.send("Not your interaction.", ephemeral=True)


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
        # check if the numbers are floats
        try:
            min = int(min)
            max = int(max)
        except:
            await ctx.send("The numbers must be integers!", ephemeral=True)
            return
        rand = random.randint(min, max)
        embed = Embed(
            title=rand,
            description=f"> `{min}` - `{max}`",
            color=Color.from_hex("5e50d4"),
            timestamp=datetime.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url
        )
        await ctx.send(embed=embed, components=[delete_btn])

    except:
        if min >= max:
            await ctx.send("The first number must be smaller than the second one!", ephemeral=True)
        if min == max:
            await ctx.send("The numbers cant be the same!", ephemeral=True)
        else:
            await ctx.send("Something didnt go right. Try a different aproach!", ephemeral=True)


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
    max_value=30,
    min_value=2,
)
@slash_option(
    name="user",
    description="user to clear messages from",
    required=False,
    opt_type=OptionType.USER,
)
@slash_option(
    name="bot",
    description="clear messages only from bots",
    required=False,
    opt_type=OptionType.BOOLEAN,
)
async def clear(ctx, count, user=None, bot=False):
    try:
        count = int(count)
    except e as Exception:
        await ctx.send("Please input an integer", ephemeral=True)
        return
    reason = f"@{ctx.author.display_name}({ctx.author.id}) cleared {count} messages"
    if user:
        if bot:
            if user.bot:
                await ctx.channel.purge(
                    deletion_limit=count,
                    predicate=lambda m: m.author == user,
                    reason=reason,
                )
            else:
                count = 0
        else:
            await ctx.channel.purge(
                deletion_limit=count,
                predicate=lambda m: m.author == user,
                reason=reason,
            )
    elif bot:
        await ctx.channel.purge(
            deletion_limit=count,
            predicate=lambda m: m.author == user.bot,
            reason=reason,
        )
    if (user == None) and (bot == False):
        await ctx.channel.purge(deletion_limit=count)
    if user == None:
        user = "`All`"
    elif user:
        user = user.mention
    embed = Embed(
        title="Messages deleted successfully",
        description=f"> `{count}` messages deleted succesfully",
        color=Color.from_hex("5e50d4"),
    )
    embed.add_field(
        name="Parameters",
        value=f"> User: {user}\n> Bot only: `{bot}`",
    )
    await ctx.send(embed=embed, ephemeral=True)


secret_TOKEN = os.environ["TOKEN"]
try:
    bot.start(secret_TOKEN)
except Exception as e:
    os.system("kill 1")
    raise Exception(f"Failed to log in, reason: {e}")
