from interactions import *
import random, os
from const import EXCLUDED_EXTS, DEV_ROLE

async def isDev(ctx : BaseContext) :
    return ctx.author.has_role(DEV_ROLE)

class Reload(Extension): 

    def reload_exts(self, bot : Client, folder : str, excluded_files : list[str] = None) :
        cogs = [files.replace(".py", "") for files in os.listdir(folder) if files.endswith("py") and files not in excluded_files]
        for _ in cogs : 
            bot.reload_extension(f"{folder}.{_}")
            print(f"{_} reloaded")

    @slash_command(
        name="reload",
        description="Command to reload extensions",
        scopes=[974354202430169139]
    )
    @slash_option(
        name="extension",
        description="Select a cog to reload",
        required=False, 
        autocomplete=True,
        opt_type=OptionType.STRING
    )
    @check(isDev)
    async def reload(self, ctx : SlashContext, extension : str = None):
        if not extension :
            self.reload_exts(self.bot, "data", EXCLUDED_EXTS)
            await ctx.send("Reloaded all extensions !")
        else :
            self.bot.reload_extension(f"data.{extension}")
            print(f"Correctly reloaded {extension}")
            await ctx.send(f"Reloaded {extension} correctly !")

    @reload.autocomplete("extension")
    async def autocomplete(self, ctx : AutocompleteContext) : 
        string_input = ctx.input_text
        ext = [ext for ext in os.listdir("./data") if ext.startswith(string_input) and ext.endswith(".py") and ext not in EXCLUDED_EXTS] 
        await ctx.send(choices=[{"name": ext, "value": ext.replace(".py", "")} for ext in ext])

def setup(bot):
    Reload(bot)