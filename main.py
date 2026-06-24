import discord
from discord.ext import commands
import os

# 🔐 TOKEN sécurisé (Railway)
TOKEN = os.getenv("TOKEN")

# ⚙️ Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ─────────────────────────────
# 💚 STAFF IG
# ─────────────────────────────

@bot.command(name="staff-ig")
async def staff_ig(ctx):
    await ctx.message.delete()

    await ctx.send("""
# 📋 CANDIDATURE STAFF IG

Bonjour et merci de l’intérêt que tu portes à BILLIE FR RP 💚

Nous recherchons des personnes sérieuses, actives et motivées pour assurer le bon fonctionnement du roleplay.

# 👤 INFORMATIONS GÉNÉRALES

Pseudo Roblox :
Pseudo Discord :
Âge :
Fuseau horaire :
Disponibilités :

# 💚 MOTIVATION

Pourquoi souhaites-tu rejoindre le Staff IG ?
Quelles sont tes motivations principales ?
Quelles qualités doit avoir un bon staff IG ?

# 🎮 EXPÉRIENCE

As-tu déjà été staff sur un serveur RP ?
Si oui, lequel et à quel poste ?
Ton niveau en roleplay ?

# 🧠 MISE EN SITUATION

Un joueur ne respecte pas les règles RP. Que fais-tu ?
Deux joueurs sont en conflit. Que fais-tu ?
Tu ne comprends pas une situation. Que fais-tu ?

# ✨ CONCLUSION

Pourquoi devrions-nous te choisir ?
As-tu quelque chose à ajouter ?

Bonne chance 💚
""")

# ─────────────────────────────
# 💚 STAFF DISCORD
# ─────────────────────────────

@bot.command(name="staff-discord")
async def staff_discord(ctx):
    await ctx.message.delete()

    await ctx.send("""
# 📋 CANDIDATURE STAFF DISCORD

Bonjour et merci de l’intérêt que tu portes à BILLIE FR RP 💚

Nous recherchons des personnes sérieuses et actives pour gérer la communauté Discord.

# 👤 INFORMATIONS GÉNÉRALES

Pseudo Discord :
Âge :
Fuseau horaire :
Disponibilités :

# 💚 MOTIVATION

Pourquoi souhaites-tu rejoindre le Staff Discord ?
Tes qualités ?
Tes défauts ?

# 🛠️ EXPÉRIENCE

As-tu déjà été staff sur un serveur Discord ?
Si oui, lequel et à quel poste ?

# 🧠 MISE EN SITUATION

Un membre spam, que fais-tu ?
Un membre est toxique, que fais-tu ?
Tu es perdu dans une situation, que fais-tu ?

# ✨ CONCLUSION

Pourquoi toi et pas un autre ?
As-tu quelque chose à ajouter ?

Bonne chance 💚
""")

# ─────────────────────────────
# ▶️ LANCEMENT DU BOT
# ─────────────────────────────

bot.run(TOKEN)
