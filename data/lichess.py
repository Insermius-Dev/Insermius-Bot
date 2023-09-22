import berserk as lichess
from dotenv import load_dotenv
import os
import interactions as inter
from interactions import (
    Extension,
    slash_command,
    OptionType,
    slash_option,
    Color,
    Embed,
    ActionRow,
    Button,
    ButtonStyle,
    listen,
)
from datetime import *

delete_btn = Button(style=ButtonStyle.RED, custom_id="delete", emoji="🗑️")

load_dotenv()
api_key = os.getenv("LICHESS_API")

session = lichess.TokenSession(api_key)
client = lichess.Client(session=session)


class Lichess(Extension):
    @slash_command(name="lichess", description="Get lichess stats")
    @slash_option(
        name="username",
        description="Input a username to get stats",
        required=True,
        opt_type=OptionType.STRING,
    )
    async def lichess(self, ctx, username):

        # TODO: Get the user statuses to work

        try:
            user = client.users.get_public_data(username)
            # userstatus = client.users.get_realtime_statuses(user)[0].get("online")
        except Exception as e:
            await ctx.send(f"```{e}```")
            return
        if user["perfs"]["bullet"]["games"] < 10:
            user["perfs"]["bullet"]["rating"] = str(user["perfs"]["bullet"]["rating"]) + "?"
        if user["perfs"]["blitz"]["games"] < 10:
            user["perfs"]["blitz"]["rating"] = str(user["perfs"]["blitz"]["rating"]) + "?"
        if user["perfs"]["rapid"]["games"] < 10:
            user["perfs"]["rapid"]["rating"] = str(user["perfs"]["rapid"]["rating"]) + "?"
        if user["perfs"]["classical"]["games"] < 10:
            user["perfs"]["classical"]["rating"] = str(user["perfs"]["classical"]["rating"]) + "?"
        if user["perfs"].get("puzzle") == None:
            user["perfs"]["puzzle"] = {"games": 0, "rating": 1500}
        if user["perfs"]["puzzle"]["games"] < 10:
            user["perfs"]["puzzle"]["rating"] = str(user["perfs"]["puzzle"]["rating"]) + "?"
        # if userstatus:
        #     if user["patron"]:
        #         status = f"<:Don_online:1059387820097142794>  [{user['username']}]({user['url']})"
        #     else:
        #         status = f"<:Nor_online:1059387814854271006> [{user['username']}]({user['url']})"
        # elif userstatus == None:
        #     if user["patron"]:
        #         status = f"<:Don_offline:1059387818566238269> [{user['username']}]({user['url']})"
        #     else:
        #         status = f"<:Nor_offline:1059387816833982514> [{user['username']}]({user['url']})"
        if user.get("patron"):
            user["patron"] = "<:Donator:1059387813235273728> Activated"
        else:
            user["patron"] = "<:Normal:1059387811687567380> Not activated"
        embed = Embed(
            title=f"{user['username']}'s Lichess Stats",
            thumbnail="https://cdn.discordapp.com/attachments/1054486043665125436/1059235301056331816/Lichess_Logo_2019.png",
            color=Color.from_hex("#FFFFFF"),
            timestamp=datetime.utcnow(),
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url
        )
        embed.add_field(
            name="Ratings",
            value=f"""
> **Bullet:** {user['perfs']['bullet']['rating']}
> **Blitz:** {user['perfs']['blitz']['rating']}
> **Rapid:** {user['perfs']['rapid']['rating']}
> **Classical:** {user['perfs']['classical']['rating']}
> **Puzzle:** {user['perfs']['puzzle']['rating']}
""",
        )
        embed.add_field(
            name="Stats",
            value=f"""
> **Games:** {user['count']['all']}
> **Wins:** {user['count']['win']}
> **Losses:** {user['count']['loss']}
> **Draws:** {user['count']['draw']}
""",
        )
        embed.add_field(name="Patron status", value=f"> {user['patron']}")
        # embed.add_field(name="Full profile", value=f"> {status}")
        await ctx.send(embed=embed, components=[delete_btn])


def setup(bot):
    Lichess(bot)
