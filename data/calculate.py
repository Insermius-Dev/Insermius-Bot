from interactions import *
from calculator import calculate
from datetime import datetime
from const import DELETE_BTN


class Calculate(Extension) : 

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
                timestamp=datetime.now(),
                footer=EmbedFooter(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            )
            embed.add_field(name="Expression", value=f"`{equation}`")
            embed.add_field(name="Result", value=f"{answer}")
            await ctx.send(embed=embed, components=[DELETE_BTN])
        except Exception as e:
            await ctx.send(f"Something went wrong... \n `{e}`", components=[DELETE_BTN])


def setup(bot):
    Calculate(bot)