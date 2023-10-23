from interactions import *
from asyncio import sleep as eep

class Quit(Extension) :

    #@is_owner()
    @slash_command("quit", description="Log off the bot")
    async def quit(self, ctx: InteractionContext):
        await ctx.send("Logging off...")
        await self.bot.http.close()
        await eep(0.1)
        print(f"\n{self.bot.user} has logged out")

def setup(bot): 
    Quit(bot)
