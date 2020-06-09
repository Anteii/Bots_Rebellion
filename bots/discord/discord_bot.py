import discord
from discord.ext import commands


with open("D:\\PyCharm\\Bots_Rebellion\\bots\\discord\\token.txt", "r") as f:
    TOKEN = f.readline()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot's ready")


@bot.command()
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def play_game(ctx):
    ctx.send("Ok. What is a number that I mind ?")
    discord.VoiceChannel

bot.run(TOKEN)
"""
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
"""
