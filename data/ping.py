from interactions import *
from datetime import *
from const import DELETE_BTN

class Ping(Extension) : 

    @slash_command(name="ping", description="check the bots status")
    async def ping(self, ctx : InteractionContext):
        embed = Embed(
            title="Pong! :ping_pong:",
            description=f"Latency : {round(self.bot.latency * 1000, 2)}ms",
            color=Color.from_hex("5e50d4"),
            timestamp=datetime.now(),
            footer=EmbedFooter(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        )
        message = await ctx.send(embed=embed, components=DELETE_BTN)
        await message.add_reaction("🟢")

def setup(bot):
    Ping(bot)