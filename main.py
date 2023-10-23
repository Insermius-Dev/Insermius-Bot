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
from const import WATCHINGSTATUS, PLAYINSTATUS
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

# unedited_ndaytext = None
# defenitionmade = False

# # @listen()
# # async def on_error():
# #     print("Caught an error")
# #     os.system("kill 1")


# base = os.path.dirname("templates/")
# html = open(os.path.join(base, "index.html"))
# soup = bs(html, "html.parser")

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
    bot.load_extension("data.VD")
    bot.load_extension("data.lichess")
    bot.load_extension("data.welcome")
    bot.load_extension("data.clear")
    bot.load_extension("data.compo_callback")
    bot.load_extension("data.info")
    bot.load_extension("data.ping")
    bot.load_extension("data.quit")
    bot.load_extension("data.randomise")
    bot.load_extension("data.reload")
    bot.load_extension("data.calculate")
    # bot.load_extension("data.spotify")
    # bot.load_extension("data.tictactoe")
    # bot.load_extension("data.voice")
    # bot.load_extension("data.ghostgame")


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

    #start()

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


    while True:  # Select a random activity, which will change every 60 seconds
        random_activity = randint(1, 3)
        if random_activity == 1:
            await bot.change_presence(
                activity=inter.Activity(
                    name=random.choice(PLAYINSTATUS),
                    type=inter.ActivityType.PLAYING,
                )
            )
            await asyncio.sleep(60)
        elif random_activity == 2:
            await bot.change_presence(
                activity=inter.Activity(
                    name=random.choice(WATCHINGSTATUS),
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

secret_TOKEN = os.environ["TOKEN"]
try:
     bot.start(secret_token)
except Exception as e:
     os.system("kill 1")
     raise Exception(f"Failed to log in, reason: {e}")
