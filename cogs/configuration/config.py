import nextcord, time, os, asyncio, json
from nextcord.ext import commands
from .colors import Colors

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.start_time = time.time()
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.configuration_check())

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"{Colors.INFO()} Joined guild {guild.name} ({guild.id}).")
        await self.configuration_check()

    async def configuration_check(self):
        while True:        
            for guild in self.bot.guilds:
                if not os.path.exists(f"assets/config/{guild.id}.json"):
                    with open(f"assets/config/{guild.id}.json", "w") as f:
                        f.write(json.dumps({
                            "guild": {
                                "guild_name": guild.name,
                                "guild_id": str(guild.id),
                                "owner_name": str(guild.owner),
                                "owner_id": str(guild.owner_id),
                                "guild_prefix": "=",
                                "guild_language": "EN-US",
                                "premium": False,
                                "premium_expires": None,
                                "galacticforge": False,
                                "join_date": int(guild.me.joined_at.timestamp()),
                                "features": {
                                    "logging": {
                                        "enabled": False,
                                        "channel": None
                                    },
                                }
                            }
                        }, indent=4))
                    print(f"{Colors.SUCCESS()} Created configuration file for {guild.name} ({guild.id}).")
                else:
                    pass
            await asyncio.sleep(3600)

def setup(bot):
    bot.add_cog(Config(bot))
