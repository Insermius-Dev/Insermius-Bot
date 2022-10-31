import naff
import json
from naff import Extension, slash_command, OptionTypes, slash_option, Color, Embed
from datetime import date, datetime
from babel.dates import format_date

with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)


class Extensionclass(Extension):
    @slash_command(name="checkext", description="Check if extension is loaded")
    async def check(self, ctx):
        await ctx.send("Yep, it's loaded!")

    @slash_command(
        name="smashorpass",
        description="Smash or Pass",
        scopes=[829026541950206049, 905462820009828352],
    )
    @slash_option(
        name="the_photo",
        description="Input a link of the video/photo.",
        required=True,
        opt_type=OptionTypes.STRING,
    )
    async def smashorpass(self, ctx, spicyphoto):
        message = await ctx.send(
            f"""
Smash or Pass?
{spicyphoto}
"""
        )
        await message.add_reaction("<:smash:1023135175237980231>")
        await message.add_reaction("<:pass:1023135160310448191>")

    @slash_command(name="vd", description="Get latvian namedays.")
    @slash_option(
        name="name",
        description="Input a name to get nameday date.",
        required=False,
        opt_type=OptionTypes.STRING,
    )
    async def nameday(self, ctx, name=None):
        if name == None:
            today = date.today().strftime("%m-%d")
            embed = Embed(
                title="Šodien vārda dienu svin:",
                description=", ".join(namedays[today]),
                color=Color.from_rgb(255, 13, 13),
            )
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
            )
            await ctx.send(embed=embed)
        else:
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

                    embed = Embed(
                        title=f"{unedited_ndaytext}",
                        description=f"{name} vārda dienu svin {nday_text}",
                        color=Color.from_rgb(255, 13, 13),
                    )
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
                    )

            if nday is None:
                embed = Embed(
                    title="Error_",
                    description=f"Kalendārā neatradu '{name}'",
                    color=Color.from_rgb(255, 13, 13),
                )
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/930891009007710218/1006812016675135568/IMG_7631.jpg"
                )
            await ctx.send(embed=embed)


def setup(bot):
    Extensionclass(bot)
