from interactions import *
import random
from datetime import *
from const import DELETE_BTN

class Randomise(Extension) :

    @slash_command(
        name="randomise",
        description="give a random value between two numbers",
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
    async def randomise(self, ctx : InteractionContext, min, max):
        if min < max : 
            embed = Embed(
                title=str(random.randint(min, max)),
                description=f"> `{min}` - `{max}`",
                color=Color.from_hex("5e50d4"),
                timestamp=datetime.utcnow(),
                footer=EmbedFooter(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            )
            await ctx.send(embed=embed, components=[DELETE_BTN])
        elif min > max:
            await ctx.send("The maximum number must be bigger than the minimum!", ephemeral=True)
        elif min == max:
            await ctx.send("The max and min can't be the same number!", ephemeral=True)

def setup(bot):
    Randomise(bot)