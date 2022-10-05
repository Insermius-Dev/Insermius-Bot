import naff
import json
import json as jason
from naff import Extension, slash_command, OptionTypes, slash_option


class Extensionclass(Extension):
    @slash_command(name="checkext", description="Check if extension is loaded")
    async def check(self, ctx):
        await ctx.send("Yep, it's loaded!")

    @slash_command(name="smashorpass", description="Smash or Pass", scopes=[829026541950206049])
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


def setup(bot):
    Extensionclass(bot)
