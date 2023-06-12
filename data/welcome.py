import interactions
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

class welcome(Extension):
    @listen()
    async def on_member_add(self, event):  # When a user joins
        print("User joined")
        print(event.guild.id)
        with open("data/nowelcome.txt", "r") as f:  # Get all joined users
            lines = f.readlines()
            int_lines = [eval(i) for i in lines]
            f.close
        joiner = event.member
        if event.guild.id in int_lines:  # Check if user already joined
            pass
        elif not event.guild.id in int_lines:
            if joiner.bot:  # Check if a bot joined
                embed = Embed(
                    description=f"Application '{joiner.display_name}' was added to the server!",
                    color=Color.from_hex("58f728"),
                )

                embed.set_author("Application added", icon_url=joiner.avatar.url)
                await event.guild.system_channel.send(embed=embed)
            else:  # A regular user joined
                embed = Embed(
                    title=f"Welcome {joiner.display_name}!",
                    description=f"Thanks for joining {joiner.guild.name}!",
                    timestamp=datetime.utcnow(),
                    color=Color.from_rgb(88, 109, 245),
                )
                embed.set_thumbnail(url=joiner.avatar.url)

                message = await event.guild.system_channel.send(
                    f"Welcome {joiner.mention}! :wave: ", embed=embed
                )
                await message.add_reaction("👋")


    @listen()
    async def on_member_remove(self, event):  # On member leave
        with open("data/nowelcome.txt", "r") as f:
            lines = f.readlines()
            int_lines = [eval(i) for i in lines]
            f.close()
        leaver = event.member
        if event.guild.id in int_lines:
            pass
        elif leaver == self.bot.user:
            pass
        elif int(event.guild.id) == 1090004044111696075:
            pass
        elif not event.guild.id in int_lines:
            if leaver.bot:
                embed = Embed(
                    description=f"Application '{leaver.display_name}' was removed from the server!",
                    color=Color.from_hex("f73528"),
                )

                embed.set_author(f"Application removed", icon_url=leaver.avatar.url)
                await event.guild.system_channel.send(embed=embed)
            else:
                embed = Embed(
                    title=f"{leaver.display_name} left.",
                    description=f"Sorry to see you go {leaver.display_name}!",
                    timestamp=datetime.utcnow(),
                    color=Color.from_rgb(255, 13, 13),
                )

                await event.guild.system_channel.send(embed=embed)

def setup(bot):
    welcome(bot)