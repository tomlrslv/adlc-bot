import discord
from discord.ext import commands

TOKEN = "MTUxOTM3MTUyNjY3ODI0OTY2Mw.GoArEJ.vb1N2Vu8qlod8Fp33qse-narRuTRr--KOk5960"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")


@bot.command(name="staff-ig")
async def staff_ig(ctx):
    await ctx.message.delete()

    await ctx.send("""
**# 📋 CANDIDATURE STAFF IG**

**Bonjour et merci de l’intérêt que tu portes à BILLIE FR RP 💚**

**Nous recherchons des personnes sérieuses, actives et motivées pour assurer le bon fonctionnement du roleplay.**

**# 👤 INFORMATIONS GÉNÉRALES**

**Pseudo Roblox :**

**Pseudo Discord :**

**Âge :**

**Fuseau horaire :**

**Disponibilités :**

**# 💚 MOTIVATION**

**Pourquoi souhaites-tu rejoindre le Staff IG de BILLIE FR RP ?**

**Quelles sont tes motivations principales ?**

**Selon toi, quelles sont les qualités d’un bon staff IG ?**

**# 🎮 EXPÉRIENCE**

**As-tu déjà été staff sur un serveur RP ?**

**Si oui, lequel et à quel poste ?**

**Comment décrirais-tu ton niveau en roleplay ?**

**# 🧠 MISE EN SITUATION**

**Un joueur ne respecte pas les règles RP. Que fais-tu ?**

**Deux joueurs sont en conflit, comment réagis-tu ?**

**Tu ne comprends pas une situation. Que fais-tu ?**

**# ✨ CONCLUSION**

**Pourquoi devrions-nous te choisir ?**

**As-tu quelque chose à ajouter ?**

**Bonne chance pour ta candidature 💚**
""")


@bot.command(name="staff-discord")
async def staff_discord(ctx):
    await ctx.message.delete()

    await ctx.send("""
**# 📋 CANDIDATURE STAFF DISCORD**

**Bonjour et merci de l’intérêt que tu portes à BILLIE FR RP 💚**

**Nous recherchons des personnes sérieuses et actives pour maintenir une bonne ambiance sur le serveur.**

**# 👤 INFORMATIONS GÉNÉRALES**

**Pseudo Discord :**

**Âge :**

**Fuseau horaire :**

**Disponibilités :**

**# 💚 MOTIVATION**

**Pourquoi souhaites-tu rejoindre le Staff Discord de BILLIE FR RP ?**

**Quelles sont tes qualités principales ?**

**Quels sont tes défauts ?**

**# 🛠️ EXPÉRIENCE**

**As-tu déjà été staff sur un serveur Discord ?**

**Si oui, lequel et à quel poste ?**

**Comment réagirais-tu face à une situation compliquée entre membres ?**

**# 🧠 MISE EN SITUATION**

**Un membre spam, que fais-tu ?**

**Un membre est irrespectueux, comment réagis-tu ?**

**Tu ne sais pas gérer une situation, que fais-tu ?**

**# ✨ CONCLUSION**

**Pourquoi devrions-nous te choisir ?**

**As-tu quelque chose à ajouter ?**

**Bonne chance pour ta candidature 💚**
""")


bot.run(TOKEN)