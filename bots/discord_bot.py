import discord
from discord.ext import commands

with open("discord_bot_token.txt", "r") as f:
    TOKEN = f.readline()

bot = commands.Bot(command_prefix="!")

@bot.command(pass_context=True)
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)

bot.run(TOKEN)