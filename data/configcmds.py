import interactions
from interactions import (
    Extension,
    slash_command,
    slash_option,
    Color,
    SlashContext,
)

class ConfigCMDs(Extension):
    # /config namedays
    @slash_command(
    name="config",
    description="Configurate the bot for your server",
    group_name="namedays",
    group_description="Configure the nameday command",
    )
    async def my_command_function(ctx: SlashContext):
        await ctx.send("Hello, World!")
        

def setup(bot):
    ConfigCMDs(bot)