from interactions import *
from random import randint
from const import DELETE_BTN

class GhostGame(Extension):
        
    @slash_command(
        name="ghostgame",
        description="Start TheGhostGame",
    )
    async def ghostgamev2(self, ctx : InteractionContext) -> None :
        embed = Embed(
            title="The Ghost Game 👻",
            description="There are three doors. Choose one by pressing one of the 3 buttons !",
            color=Color.from_hex("808080"),
            footer="You are at door 0"
        )
        buttons = [
            ActionRow(
                Button(custom_id=f"GhostGameCallback1_{ctx.author_id}_1", emoji="🚪", style=ButtonStyle.BLURPLE),
                Button(custom_id=f"GhostGameCallback2_{ctx.author_id}_1", emoji="🚪", style=ButtonStyle.BLURPLE),
                Button(custom_id=f"GhostGameCallback3_{ctx.author_id}_1", emoji="🚪", style=ButtonStyle.BLURPLE),
                DELETE_BTN
            )
        ]
        await ctx.send(embed=embed, components=buttons)
        
    @listen()
    async def on_component(self, ctx) -> any :
        """
        customID format :
        
        GhostGameCallback1_AuthorID_1 -> ["GhostGameCallback1", "AuthorID", "1"]
        
        > GhostGameCallback1 : 
            To identify the event we are listenning to. The number at the end is just to avoid having the same customID
        > AuthorID :
            Used to make the game personnal and not having everyone playing it
        > 1
            The number of door the player went throught
        """
        ctx : ComponentContext = ctx.ctx
        c_id = ctx.custom_id.split("_")
        print(c_id)
        if (c_id[0].startswith("GhostGameCallback") and c_id[1] == f"{ctx.author_id}") :
            if randint(1,3) == 3 :
                return await ctx.edit_origin(components=DELETE_BTN, embed=Embed(
                   title="The Ghost Game 👻",
                   description=f"Oh no ! You encountered a ghost ! You lost and went throught {int(c_id[2])} doors !"
                ))
            buttons = [
                ActionRow(
                    Button(custom_id=f"GhostGameCallback1_{c_id[1]}_{int(c_id[2]) + 1}", emoji="🚪", style=ButtonStyle.BLURPLE),
                    Button(custom_id=f"GhostGameCallback2_{c_id[1]}_{int(c_id[2]) + 1}", emoji="🚪", style=ButtonStyle.BLURPLE),
                    Button(custom_id=f"GhostGameCallback3_{c_id[1]}_{int(c_id[2]) + 1}", emoji="🚪", style=ButtonStyle.BLURPLE),
                    DELETE_BTN
                )
            ]
            return await ctx.edit_origin(components=buttons, embed=Embed(
                title="The Ghost Game 👻",
                description="There are three doors. Chose one !",
                color=Color.from_hex("808080"),
                footer=f"You are at door {c_id[2]}"
            ))
        elif (c_id[0].startswith("GhostGameCallback") and c_id[1] != f"{ctx.author_id}") :
            return await ctx.send("Hey! It's not your game! If you want to play, just use the /ghostgame command", ephemeral=True)

def setup(bot):
    GhostGame(bot)