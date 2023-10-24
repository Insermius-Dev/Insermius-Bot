from interactions import *
import random, os
from const import DELETE_BTN, NOTAUTHORMESSAGE

class Reload(Extension): 


    @slash_command(
        name="reload",
        description="Reloads a cog",
    )
    @slash_option(
        name="cog",
        description="The cog to reload",
        opt_type=OptionType.INTEGER,
        choices=[
            SlashCommandChoice(name="Welcome", value=1),
            # SlashCommandChoice(name="TicTacToe", value=2),
            # SlashCommandChoice(name="GhostGame", value=3),
            SlashCommandChoice(name="Lichess", value=4),
            SlashCommandChoice(name="VD", value=5),
            SlashCommandChoice(name="Spotify", value=6),
            SlashCommandChoice(name="Randomise", value=7),
            SlashCommandChoice(name="Ping", value=8),
            SlashCommandChoice(name="Info", value=9),
            SlashCommandChoice(name="Calculate", value=10),
            SlashCommandChoice(name="Welcome", value=11),
            SlashCommandChoice(name="Quit", value=12),
            SlashCommandChoice(name="Clear", value=13),
            SlashCommandChoice(name="Component Callback", value=14),
            SlashCommandChoice(name="Reload", value=15)
        ],
        required=False,
    )
    async def reload(self, ctx, cog=None):
        if self.bot.owner.id == ctx.author.id:
            match (cog):
                case 1 :
                    self.bot.reload_extension("data.welcome")
                    await ctx.respond("Reloaded cog `Welcome`")
                case 2 :
                    self.bot.reload_extension("data.tictactoe")
                    await ctx.respond("Reloaded cog `tictactoe`")
                case 3 :
                    self.bot.reload_extension("data.ghostgame")
                    await ctx.respond("Reloaded cog `ghostgame`")
                case 4 :
                    self.bot.reload_extension("data.lichess")
                    await ctx.respond("Reloaded cog `lichess`")
                case 5 :
                    self.bot.reload_extension("data.VD")
                    await ctx.respond("Reloaded cog `VD`")
                case 6 :
                    self.bot.reload_extension("data.spotify")
                    await ctx.respond("Reloaded cog `spotify`")
                case 7 :
                    self.bot.reload_extension("data.randomise")
                    await ctx.respond("Reloaded cog `randomise`")
                case 8 :
                    self.bot.reload_extension("data.ping")
                    await ctx.respond("Reloaded cog `ping`")
                case 9 :
                    self.bot.reload_extension("data.info")
                    await ctx.respond("Reloaded cog `info`")
                case 10 :
                    self.bot.reload_extension("data.calculate")
                    await ctx.respond("Reloaded cog `calculate`")
                case 11 :
                    self.bot.reload_extension("data.welcome")
                    await ctx.respond("Reloaded cog `welcome`")
                case 12 :
                    self.bot.reload_extension("data.quit")
                    await ctx.respond("Reloaded cog `quit`")
                case 13 :
                    self.bot.reload_extension("data.clear")
                    await ctx.respond("Reloaded cog `clear`")
                case 14 :
                    self.bot.reload_extension("data.compo_callback")
                    await ctx.respond("Reloaded cog `compo_callback`")
                case 15 :
                    self.bot.reload_extension("data.reload")
                    await ctx.respond("Reloaded cog `reload`")
                case None : 
                    self.bot.reload_extension("data.info")
                    print("Reloaded cog info")
                    self.bot.reload_extension("data.ping")
                    print("Reloaded cog ping")
                    #self.bot.reload_extension("data.spotify")
                    #print("Reloaded cog spotify")
                    self.bot.reload_extension("data.lichess")
                    print("Reloaded cog lichess")
                    self.bot.reload_extension("data.welcome")
                    print("Reloaded cog welcome")
                    self.bot.reload_extension("data.randomise")
                    print("Reloaded cog randomise")
                    self.bot.reload_extension("data.quit")
                    print("Reloaded cog quit")
                    self.bot.reload_extension("data.VD")
                    print("Reloaded cog VD")
                    self.bot.reload_extension("data.clear")
                    print("Reloaded cog clear")
                    self.bot.reload_extension("data.compo_callback")
                    print("Reloaded cog compo_callback")
                    self.bot.reload_extension("data.calculate")
                    print("Reloaded cog calculate")
                    await ctx.respond("Reloaded all cogs !")
        else:
            await ctx.respond(random.choice(NOTAUTHORMESSAGE), ephemeral=True, components=[DELETE_BTN])

def setup(bot):
    Reload(bot)