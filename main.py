import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)


# ─────────────────────────────
# 📦 CHARGEMENT DES MODULES
# ─────────────────────────────

async def load_extensions():
    await bot.load_extension("formulaires")
    await bot.load_extension("welcome")


@bot.event
async def setup_hook():
    await load_extensions()


# ─────────────────────────────
# 🤖 BOT READY
# ─────────────────────────────

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")


# ─────────────────────────────
# 🚀 LANCEMENT
# ─────────────────────────────

bot.run(TOKEN)
