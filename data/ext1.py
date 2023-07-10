import interactions as inter
import json
from interactions import (
    Extension,
    slash_command,
    slash_option,
    Color,
    Embed,
    ActionRow,
    Button,
    ButtonStyle,
    listen,
    OptionType,
)
from datetime import date, datetime
from babel.dates import format_date
from calculator import calculate

delete_btn = Button(style=ButtonStyle.RED, custom_id="delete", emoji="🗑️")

with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)

spotify_emoji = "<:spotify:985229541482061854>"

class Extensionclass(Extension):

    @slash_command(
        name="spotify",
        description="Share what you're listening to!",
    )
    async def spotify(self, ctx):
        listener = ctx.author

        # Get the first activity that contains "Spotify". Return None, if none present.
        spotify_activity = next((x for x in listener.activities if x.name == "Spotify"), None)


        if spotify_activity is not None:
            cover = f"https://i.scdn.co/image/{spotify_activity.assets.large_image.split(':')[1]}"
            embed = Embed(
                title=f"{listener.display_name}'s Spotify",
                description="Listening to {}".format(spotify_activity.name),
                color="#36b357",
                thumbnail=cover,
            )
            embed.add_field(name="Artist", value=spotify_activity.state)
            embed.add_field(name="Album", value=spotify_activity.assets.large_text)
        else:
            embed = Embed(
                title=f"{listener.display_name}'s Spotify",
                description="Currently not listening to anything",
                color="#36b357",
                timestamp=datetime.utcnow(),
            )
        embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
        message = await ctx.send(embeds=embed, components=[delete_btn])
        # await message.add_reaction(spotify_emoji)

    #     @slash_command(
    #         name="smashorpass",
    #         description="Smash or Pass",
    #         scopes=[829026541950206049, 905462820009828352],
    #     )
    #     @slash_option(
    #         name="the_photo",
    #         description="Input a link of the video/photo.",
    #         required=True,
    #         opt_type=OptionType.STRING,
    #     )
    #     async def smashorpass(self, ctx, spicyphoto):
    #         message = await ctx.send(
    #             f"""
    # Smash or Pass?
    # {spicyphoto}
    # """
    #         )
    #         await message.add_reaction("<:smash:1023135175237980231>")
    #         await message.add_reaction("<:pass:1023135160310448191>")

    # @slash_command(name="vd", description="Get latvian namedays.")
    # @slash_option(
    #     name="name",
    #     description="Input a name to get nameday date.",
    #     required=False,
    #     opt_type=OptionType.STRING,
    # )
    # async def nameday(self, ctx, name=None):
    #     if name == None:
    #         components = [
    #             ActionRow(
    #                 Button(
    #                     label="Rādīt visus",
    #                     style=ButtonStyle.RED,
    #                     custom_id="extendedlistshow",
    #                     emoji="🗓",
    #                 )
    #             ),
    #         ]
    #         today = date.today().strftime("%m-%d")
    #         embed = Embed(
    #             title="Šodien vārda dienu svin:",
    #             description=", ".join(namedays[today]),
    #             color=Color.from_rgb(255, 13, 13),
    #         )
    #         embed.set_thumbnail(
    #             url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
    #         )
    #         await ctx.send(embed=embed, components=components)
    #     else:
    #         nday = None
    #         for k in namedays.keys():
    #             v = namedays[k] + namedays_ext[k]
    #             if name in v:
    #                 nday = datetime.strptime("2000-" + k, "%Y-%m-%d").date()
    #                 nday_text = format_date(date=nday, format="d. MMMM", locale="lv")
    #                 if nday_text.endswith("is"):
    #                     unedited_ndaytext = nday_text
    #                     nday_text = nday_text[:-2] + "ī"
    #                 else:
    #                     unedited_ndaytext = nday_text
    #                     nday_text = nday_text[:-1] + "ā"

    #                 embed = Embed(
    #                     title=f"{unedited_ndaytext}",
    #                     description=f"{name} vārda dienu svin {nday_text}",
    #                     color=Color.from_rgb(255, 13, 13),
    #                 )
    #                 embed.set_thumbnail(
    #                     url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
    #                 )

    #         if nday is None:
    #             embed = Embed(
    #                 title="Error_",
    #                 description=f"Kalendārā neatradu '{name}'",
    #                 color=Color.from_rgb(255, 13, 13),
    #             )
    #             embed.set_thumbnail(
    #                 url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
    #             )
    #         await ctx.send(embed=embed)

    #         await dm.send(embed=embed)
    @slash_command(name="calculate", description="calculate some numbers")
    @slash_option(
        name="equation",
        required=True,
        opt_type=OptionType.STRING,
        description="input your math equation",
    )
    async def calc(self, ctx, equation):
        try:
            answer = calculate(equation)
            embed = Embed(
                title="Calculator",
                color=Color.from_rgb(52, 152, 219),
                timestamp=datetime.utcnow(),
            )
            embed.add_field(name="Expression", value=f"`{equation}`")
            embed.add_field(name="Result", value=f"{answer}")
            await ctx.send(embed=embed, components=[delete_btn])
        except Exception as e:
            await ctx.send(f"Something went wrong... \n `{e}`", components=[delete_btn])


def setup(bot):
    Extensionclass(bot)
