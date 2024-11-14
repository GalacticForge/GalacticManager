import nextcord, asyncio, os
from nextcord.ext import commands

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.status_loop())      
        
    async def status_loop(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await self.bot.change_presence(activity=nextcord.Game(name=f"with {len(self.bot.guilds)} servers"))
            await asyncio.sleep(10)
            await self.bot.change_presence(activity=nextcord.Game(name=f"with {len(self.bot.users)} users"))
            await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(Start(bot))