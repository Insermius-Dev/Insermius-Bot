# Bot originally made by using NAFF
# Ported to i.py v5
# pip install -U discord-py-interactions

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
from const import EPIC_CONTRIBUTING_PPL, LIL_HELPERS

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

def load_extensions(bot, folder, folder_name="", exclude_files=[]):
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        bot.load_extension(f"{folder_name}{ext}")
        print(f"Loadded {ext}.py correctly")

@listen()
async def on_startup():
    print(f"{bot.user} has connected to Discord!")
    load_extensions(bot, "data", "data.", exclude_files=[
        "quit.py",
        "tictactoe.py",
        "voice.py",
        "spotify.py",
        "configcmds.py"])
    bot.del_unused_app_cmd = True

    lab_guild = 974354202430169139
    lab_contributor = 974586417932021760
    lab_lilhelper = 1041445249668624475
    # get all of the users with the roles
    contributors = bot.get_guild(lab_guild)
    if contributors != None : 
        contributors.get_role(lab_contributor).members
        for i in range(len(contributors)):
            EPIC_CONTRIBUTING_PPL.append(contributors[i].id)
    
    lilhelpers = bot.get_guild(lab_guild)
    if lilhelpers != None :
        lilhelpers.get_role(lab_lilhelper).members
        for i in range(len(lilhelpers)):
            LIL_HELPERS.append(lilhelpers[i].id)

    dev = bot.get_user(737983831000350731)

    start(contributors, lilhelpers, dev)

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


secret_TOKEN = os.environ["TOKEN"]
try:
    bot.start(secret_TOKEN)
except Exception as e:
    os.system("kill 1")
    raise Exception(f"Failed to log in, reason: {e}")
