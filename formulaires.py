import discord
from discord.ext import commands


class Formulaires(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ─────────────────────────────
    # 📋 STAFF IG
    # ─────────────────────────────

    @commands.command(name="staff-ig")
    async def staff_ig(self, ctx):
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
Qu’est-ce qui te motive ?
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
    # 💬 STAFF DISCORD
    # ─────────────────────────────

    @commands.command(name="staff-discord")
    async def staff_discord(self, ctx):
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
Quelles sont tes qualités ?
Quels sont tes défauts ?

# 🛠️ EXPÉRIENCE

As-tu déjà été staff sur un serveur Discord ?
Si oui, lequel et à quel poste ?

# 🧠 MISE EN SITUATION

Un membre spam, que fais-tu ?
Un membre est irrespectueux, que fais-tu ?
Tu ne comprends pas une situation, que fais-tu ?

# ✨ CONCLUSION

Pourquoi devrions-nous te choisir ?
As-tu quelque chose à ajouter ?

Bonne chance 💚
""")


async def setup(bot):
    await bot.add_cog(Formulaires(bot))
