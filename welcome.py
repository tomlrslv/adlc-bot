import discord
from discord.ext import commands

GIF_URL = "https://media1.tenor.com/m/MTl2RygQbPIAAAAC/billie-billie-eilish.gif"


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # 🎯 salon "bienvenue"
        channel = discord.utils.get(member.guild.text_channels, name="bienvenue")

        if channel is None:
            return

        embed = discord.Embed(
            title="💚 Bienvenue sur BILLIE FR RP",
            description=f"""
✨ Salut {member.mention} !

Bienvenue sur le serveur RP 💚

📌 Pense à :
• Lire le règlement
• Faire ta candidature staff si tu veux rejoindre l'équipe
• Ouvrir un ticket si besoin

🚀 Amuse-toi bien parmi nous !
""",
            color=0x39FF14
        )

        embed.set_image(url=GIF_URL)
        embed.set_footer(text="BILLIE FR RP • Welcome System")

        await channel.send(content=member.mention, embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
