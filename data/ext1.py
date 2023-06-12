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

with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)


class Extensionclass(Extension):
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

    # TODO: Fix the invite creation
    @listen()
    async def on_guild_join(self, guild):
        if self.bot.is_ready:
            print("New guild joined")
            #         dm = await self.bot.owner.fetch_dm()
            #         invite = await guild.guild.system_channel.create_invite()
            #         embed = Embed(
            #             title=guild.guild.name,
            #             description=guild.guild.description,
            #             timestamp=datetime.utcnow(),
            #             color=Color.from_hex("32a852"),
            #             thumbnail=guild.guild.icon,
            #         )
            #         # embed.add_field(name="Member count", value=len(guild.guild.members))
            #         # embed.add_field(name="Created", value=guild.guild.created_at)
            #         # embed.add_field(name="Boost level", value="Level {0}".format(guild.guild.premium_tier))
            #         await dm.send(invite, embed=embed)
            with open("data/nowelcome.txt", "w") as f:
                lines = f.readlines()
                lines.append(guild.guild.id)
                f.write("\n".join(lines))

    @listen()
    async def on_guild_remove(self, guild):
        if self.bot.is_ready:
            print("Guild left")
            #         dm = await self.bot.owner.fetch_dm()
            #         embed = Embed(
            #             title="left " + guild.guild.name,
            #             timestamp=datetime.utcnow(),
            #             color=Color.from_hex("b50a07"),
            #             thumbnail=guild.guild.icon,
            #         )
            with open("data/nowelcome.txt", "w") as f:
                lines = f.readlines()
                int_lines = [eval(i) for i in lines]
                if guild.guild.id in int_lines:
                    int_lines.remove(guild.guild.id)
                    f.write("\n".join(int_lines))

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
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Something went wrong... \n `{e}`")


def setup(bot):
    Extensionclass(bot)
