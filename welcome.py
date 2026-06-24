import discord
from discord.ext import commands

GIF_URL = "https://media1.tenor.com/m/MTl2RygQbPIAAAAC/billie-billie-eilish.gif"
WELCOME_CHANNEL_ID = 1515772992880377906


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

        if channel is None:
            return

        embed = discord.Embed(
            title="💚 Bienvenue sur BILLIE FR RP",
            description=f"""
✨ Bienvenue {member.mention} !

Tu viens de rejoindre le serveur RP 💚

📌 Pense à :
• Lire le règlement
• Faire tes premiers pas dans le RP
• Ouvrir un ticket si besoin

🚀 Amuse-toi bien parmi nous !
""",
            color=0x39FF14
        )

        embed.set_image(url=GIF_URL)
        embed.set_footer(text="BILLIE FR RP • Welcome System")

        # 💬 MESSAGE + EMBED
        await channel.send(content=f"{member.mention} 👋", embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
