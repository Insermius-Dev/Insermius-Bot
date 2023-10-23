from interactions import *
from datetime import * 
from const import DELETE_BTN, BOT_VERSION, NOW_UNIX


class Info(Extension):


    @slash_command(
        name="info",
        description="get info about the bot",
    )
    async def info(self, ctx):
        embed = Embed(
            title="Info",
            description="Info about the bot",
            timestamp=datetime.utcnow(),
            color=Color.from_hex("5e50d4"),
            thumbnail="https://cdn.discordapp.com/attachments/983081269543993354/1041045309695987712/image.png",
            url="https://larss-bot.onrender.com",
            footer=EmbedFooter(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
        )
        embed.add_field(
            name="Bot Version",
            value=BOT_VERSION,
        )
        embed.add_field(
            name="Guilds",
            value=f"in {len(self.bot.guilds)} guilds.",
        )
        embed.add_field(
            name="Created by",
            value="<@737983831000350731>",
        )
        embed.add_field(
            name="Last startup",
            value=f"<t:{int(str(NOW_UNIX)[:-2])}:R>",
        )
        embed.add_field(
            name="Support the creator!",
            value="https://ko-fi.com/larssj",
        )

        btn1 = Button(
            label="Contributors", style=ButtonStyle.BLUE, emoji="⭐", custom_id="contributors"
        )
        btn2 = Button(
            label="Partnered servers", style=ButtonStyle.BLUE, emoji="🏘", custom_id="guildsinvites"
        )
        components: list[ActionRow] = spread_to_rows(btn1, btn2)
        components.append(ActionRow(DELETE_BTN))
        await ctx.send(embed=embed, components=components)

def setup(bot) : 
    Info(bot)