import discord
from discord.ext import commands

# Enable necessary intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Set command prefix (e.g., !hello)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am your bot!")

@bot.command()
async def how(ctx):
    # Replace YOUR_OPENWEATHERMAP_API_KEY with your actual API key
    await ctx.send("am find thanks you!")

bot.run("MTI3ODk4NzgzNzkyNDA1MzA3Mw.GtFRhP.GSZ04ThmUDHMTQWVz4s3m7raC24uoJ3kDAd1Bk")
