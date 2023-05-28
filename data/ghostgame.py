import interactions as inter
from interactions import (
    Extension,
    slash_command,
    OptionType,
    slash_option,
    Color,
    Embed,
    ActionRow,
    Button,
    ButtonStyle,
    listen,
)
from random import randint
from datetime import datetime

players = []
door_count = []
game_message_ids = []
game_channel_ids = []

components = [
    ActionRow(
        Button(custom_id="door_1", label="1", style=ButtonStyle.BLURPLE),
        Button(custom_id="door_2", label="2", style=ButtonStyle.BLURPLE),
        Button(custom_id="door_3", label="3", style=ButtonStyle.BLURPLE),
    )
]


class GhostGameExtension(Extension):
    @slash_command(name="ghostgame", description="Play a game of picking and choosing doors!")
    async def ghostgame(self, ctx):

        embed = Embed(
            title="Ghost game",
            description="There are three doors in front of you...",
            color=Color.from_hex("808080"),
        )
        embed.set_footer(text="Press one of the 3 buttons below to pick a door!")

        message = await ctx.send(
            "<@!{0}>".format(ctx.author.id), embed=embed, components=components
        )

        game_message_ids.append(message.id)
        game_channel_ids.append(message.id)
        players.append(ctx.author.id)
        door_count.append(0)

    @listen()
    async def on_component(self, ctx):
        ctx = ctx.ctx
        ghost_door = randint(1, 3)

        if ctx.custom_id.startswith("door_"):
            if ctx.author.id not in players:
                await ctx.send(
                    "This isn't your game! To start a game use `/ghostgame`!", ephemeral=True
                )
            elif ctx.author.id in players and game_message_ids.index(
                ctx.message.id
            ) != players.index(ctx.author.id):
                channel = self.bot.get_channel(game_channel_ids[players.index(ctx.author.id)])
                message = await channel.fetch_message(
                    game_message_ids[players.index(ctx.author.id)]
                )
                await ctx.send(
                    f"This isn't your game! Please finish or abort your previous game to start a new one! ({message.jump_url})",
                    ephemeral=True,
                )
            elif ctx.author.id in players and game_message_ids.index(
                ctx.message.id
            ) == players.index(ctx.author.id):
                door = int(ctx.custom_id.split("_")[-1])

                embed_gameover = Embed(
                    title="Game over!",
                    description="The ghost got you! You went through {0} doors.".format(
                        door_count[players.index(ctx.author.id)]
                    ),
                    color=Color.from_hex("808080"),
                )

                embed_gameover.set_footer(
                    text="Boo ;) (thanks for playing)".format(
                        door_count[players.index(ctx.author.id)]
                    )
                )

                embed_gameover.timestamp = datetime.utcnow()

                if door == ghost_door:
                    components[0].components[0].disabled = True
                    components[0].components[1].disabled = True
                    components[0].components[2].disabled = True
                    await ctx.edit_origin(embed=embed_gameover, components=components)
                    channel = await self.bot.fetch_channel(
                        game_channel_ids[players.index(ctx.author.id)]
                    )
                    message = await channel.get_message(
                        game_message_ids[players.index(ctx.author.id)]
                    )
                    await message.add_reaction("👻")
                else:
                    door_count[players.index(ctx.author.id)] = (
                        door_count[players.index(ctx.author.id)] + 1
                    )
                    await ctx.edit_origin(
                        content="Door {0}.".format(door_count[players.index(ctx.author.id)]),
                        components=components,
                    )

            # Brave = True
            # Ending = False
            # Score = 0
            # Already_said_that = False

            # while Brave == True:

            #     Ghost = randint(1, 3)

            #     if Already_said_that == True:

            #         ctx.send("Pick another door!")

            #     else:

            #         print("There are three doors in front of you...")
            #         print("Witch one will you pick?")
            #         Already_said_that = True

            #     Door = input("1,2 or 3?")
            #     try:
            #         Door_number = int(Door)
            #     except:
            #         Door_number = None

            #     if Door_number != 1 and Door_number != 2 and Door_number != 3:
            #         print("The ghost found you while you were trying to find a door in a wall.")
            #         Brave = False

            #     elif Door_number == Ghost and Brave == True:
            #         print("GHOOOOOOOST!!! RUUUUUUNNNNN!!!")
            #         Brave = False
            #     else:
            #         print("Room clear...")
            #         Score = Score + 1
            # print("You ran away...")
            # print("You went trough", Score, "doors/door")
            # Rly_continue = True
            # while Rly_continue == True:
            #     Continue = input("Do you want to play again?(Y/N)")
            #     if Continue == ("y"):
            #         New_run = True
            #         Rly_continue = False
            #     elif Continue == ("Y"):
            #         New_run = True
            #         Rly_continue = False
            #     else:
            #         print("Byeee!")
            #         New_run = False
            #         Rly_continue = False

    # print when the extension is loaded
    def __init__(self, bot):
        self.bot = bot
        print("Ghost game extension loaded")


def setup(bot):
    GhostGameExtension(bot)
