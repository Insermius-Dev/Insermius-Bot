import discord
from discord.ext import commands
import json
import json as jason


class Indev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def baz(self, ctx):
        await ctx.send("something")

    @commands.command()
    async def setbirthday(self, ctx, msg):
        """Set a birthday."""
        member = ctx.message.author.id
        await ctx.send("What is your birthday? Please use MM/DD format.")

        def check(user):
            return user == ctx.message.author and user == ctx.message.channel

        #   msg = await bot.wait_for("message", check=check)
        try:
            list = msg.split("/")
            print(list)
            list[0] = int(list[0])
            list[1] = int(list[1])
            print(list)
            if list[0] > 13 or list[0] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass

            if list[0] in (1, 3, 5, 7, 8, 10, 12):
                if list[1] > 31 or list[1] < 1:
                    await ctx.send("Invalid date.")
                    await ctx.send("Aborting...")
                    return
                else:
                    pass
            elif list[0] in (4, 6, 9, 11):
                if list[1] > 30 or list[1] < 1:
                    await ctx.send("Invalid date.")
                    await ctx.send("Aborting...")
                    return
                else:
                    pass
            elif list[0] == 2:
                if list[1] > 29 or list[1] < 1:
                    await ctx.send("Invalid date.")
                    await ctx.send("Aborting...")
                    return
                else:
                    pass
            else:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
        except:
            print("faill")
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return

        month = list[0]
        day = list[1]

        with open("birthdays.json", "r+") as f:
            var = jason.load(f)
            var[member] = {"month": month, "day": day}
            jason.dump(var, f, indent=4)


def setup(bot):
    bot.add_cog(Indev(bot))
