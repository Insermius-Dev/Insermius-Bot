from interactions import Extension
from interactions import *
import interactions as inter
import random
import asyncio
from interactions.api.voice.audio import AudioVolume


class voice(Extension):
    @slash_command("play", description="Play a song in your voice channel")
    @slash_option(
        name="song",
        description="Select the song you want to play",
        required=True,
        opt_type=OptionType.INTEGER,
        choices=[
            SlashCommandChoice(name="Never gonna give you up", value=1),
            SlashCommandChoice(name="Gas-gas-gas", value=2),
        ],
    )
    async def play(self, ctx: InteractionContext, song: int):
        if not ctx.author.voice:
            return await ctx.send("You are not in a voice channel", ephemeral=True)
        elif ctx.voice_state:
            return await ctx.send("Already in a voice channel!", ephemeral=True)
        else:
            color = random.randrange(0, 2**24)
            hex_color = hex(color)
            if song == 1:
                embed = Embed(
                    'Playing "Never gonna give you up" by Rick Astley',
                    description=f"<#{ctx.author.voice.channel.id}>",
                    color="#" + hex_color[2:],
                )
                embed.set_footer(
                    text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url
                )
                await ctx.send(embed=embed)
                audio = AudioVolume(r"data\giveyouup.mp3")
                audio.probe = False
            elif song == 2:
                embed = Embed(
                    'Playing "Gas-gas-gas" by Manuel',
                    description=f"<#{ctx.author.voice.channel.id}>",
                    color="#" + hex_color[2:],
                )
                embed.set_footer(
                    text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url
                )
                await ctx.send(embed=embed)
                audio = AudioVolume(r"data\gas-gas-gas.mp3")
                audio.probe = False

            await ctx.author.voice.channel.connect(deafened=True)
            await asyncio.sleep(0.5)
            await ctx.voice_state.play(audio)
            await asyncio.sleep(3)
            await ctx.voice_state.disconnect()

    @slash_command("stop", description="Stop the current song")
    async def stop(self, ctx: InteractionContext):
        if not ctx.author.voice:
            return await ctx.send("You are not in a voice channel!", ephemeral=True)
        elif not ctx.voice_state:
            return await ctx.send("Not playing anything at the moment.", ephemeral=True)
        else:
            await ctx.voice_state.stop()
            await ctx.send("Stopped playing!")


def setup(bot):
    voice(bot)
