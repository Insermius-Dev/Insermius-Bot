from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import re
from datetime import date, datetime
from babel.dates import format_date
import json
from time import sleep
import discord
from keep_alive import keep_alive
from random import choice
from discord.utils import get
from discord.ext.tasks import loop

load_dotenv()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the chat"))

colours = [discord.Colour(0xe91e63), discord.Colour(0x0000FF0), discord.Colour(0x00FF00), discord.Colour(0xFF0000)]
guild_id = 12345
role_name = "Bot"
role_to_change = None
@loop(seconds=1)
async def colour_change():
    await role_to_change.edit(colour=choice(colours))
    print("Task")

@colour_change.before_loop
async def colour_change_before():
    global role_to_change
    await bot.wait_until_ready()
    guild = bot.get_guild(guild_id)
    role_to_change = get(guild.roles, name=role_name)

colour_change.start()

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

def tictactoe():
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True

    board = []

    winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    @bot.command()
    async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            # print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")

    @bot.command()
    async def place(ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    checkWinner(winningConditions, mark)
                    print(count)
                    if gameOver == True:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")

                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the !tictactoe command.")


    def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

    @tictactoe.error
    async def tictactoe_error(ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

    @place.error
    async def place_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")

with open("data/namedays.json", encoding="utf-8") as f:
    namedays = json.load(f)

with open("data/namedays.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)  
     
@bot.event
async def on_message(message):

    if message.content == "!vd":
        today = date.today().strftime("%m-%d")
        channel = message.channel
        sleep(0.5)
        await channel.send("Šodien vārda dienu svin " + ", ".join(namedays[today]))

    elif message.content.startswith("!vd "):
        matches = re.search(r"\!vd (\w+)", message.content)
        if matches:
            find_name = matches.group(1)
            find_name = find_name[0].upper() + find_name[1:]
        else:
            return

        nday = None
        for k in namedays.keys():
            v = namedays[k] + namedays_ext[k]
            if find_name in v:
                nday = datetime.strptime("2000-" + k, "%Y-%m-%d").date()
                nday_text = format_date(date=nday, format="d. MMMM", locale="lv")
                if nday_text.endswith("is"):
                    nday_text = nday_text[:-2] + "ī"
                else:
                    nday_text = nday_text[:-1] + "ā"
                msg = f"{find_name} vārda dienu svin {nday_text}"
                break
        if nday is None:
            msg = f"Kalendārā neatradu vārdu {find_name}"

        channel = message.channel
        sleep(0.5)
        await channel.send(msg)

    elif message.content.startswith('$'):
      emojiup = '✅'
      emojidown = '❌'
      emoji1 = '1️⃣'
      emoji2 = '2️⃣'
      emoji3 = '3️⃣'
      emoji4 = '4️⃣'
      emoji5 = '5️⃣'
      if message.content.startswith('$ '):
        await message.add_reaction(emojiup)
        await message.add_reaction(emojidown)
      elif message.content.startswith('$2'):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
      elif message.content.startswith('$3'):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
      elif message.content.startswith('$4'):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
        await message.add_reaction(emoji4)
      elif message.content.startswith('$5'):
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
        await message.add_reaction(emoji4)
        await message.add_reaction(emoji5)
        
keep_alive()
secret_TOKEN = os.environ['CUSTOMCONNSTR_DISCORD_TOKEN']
bot.run(secret_TOKEN)   