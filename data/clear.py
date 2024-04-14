from interactions import *


class Clear(Extension):

    @slash_command(
        name="clear",
        description="clears messages",
        default_member_permissions=Permissions.MANAGE_MESSAGES,
    )
    @slash_option(
        name="count",
        description="number of messages to clear",
        required=True,
        opt_type=OptionType.INTEGER,
        max_value=30,
        min_value=2,
    )
    @slash_option(
        name="user",
        description="user to clear messages from",
        required=False,
        opt_type=OptionType.USER,
    )
    @slash_option(
        name="bot",
        description="clear messages only from bots",
        required=False,
        opt_type=OptionType.BOOLEAN,
    )
    async def clear(self, ctx, count, user=None, bot=False) -> None:
        reason = f"@{ctx.author.display_name}({ctx.author.id}) cleared {count} messages"

        target = user if ((user and bot) and user.bot) else False if ((user and bot) and not user.bot) else user if user else user.bot if bot else True

        if target:
            count = 0
        elif not target:
            await ctx.channel.purge(deletion_limit=count);
        else:
            await ctx.channel.purge(
                deletion_limit=count,
                predicate=lambda m: m.author == target,
                reason=reason,
            )

        # if user and bot:
        #     if user.bot:
        #         await ctx.channel.purge(
        #             deletion_limit=count,
        #             predicate=lambda m: m.author == user,
        #             reason=reason,
        #         )
        #     else:
        #         count = 0

        # elif user:
        #     await ctx.channel.purge(
        #         deletion_limit=count,
        #         predicate=lambda m: m.author == user,
        #         reason=reason,
        #     )
        # elif bot:
        #     await ctx.channel.purge(
        #         deletion_limit=count,
        #         predicate=lambda m: m.author == user.bot,
        #         reason=reason,
        #     )
        # if (user == None) and (bot == False):
        #     await ctx.channel.purge(deletion_limit=count)

        user = "`All`" if user == None else user.displaly_name

        embed = Embed(
            title="Messages deleted successfully",
            description=f"> `{count}` messages deleted succesfully",
            color=Color.from_hex("5e50d4"),
        )
        embed.add_field(
            name="Parameters",
            value=f"> User: {user}\n> Bot only: `{bot}`",
        )
        await ctx.send(embed=embed, ephemeral=True)


def setup(bot):
    Clear(bot)
