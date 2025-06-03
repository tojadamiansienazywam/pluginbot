import discord
from discord.ext import commands
from logic import analyze_input
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

@bot.command(name="plugin")
async def plugin_help(ctx, *, message: str):
    await ctx.send("⏳ Przetwarzam dane...")
    response = analyze_input(message)
    await ctx.send(response[:2000])  # Discord ma limit 2000 znaków

if __name__ == "__main__":
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    if not discord_token:
        print("❌ Brakuje DISCORD_BOT_TOKEN w zmiennych środowiskowych")
    else:
        bot.run(discord_token)