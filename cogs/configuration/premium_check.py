import json, os, time, nextcord, asyncio
from nextcord.ext import commands
from .colors import Colors

class PremiumCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.premium_check())
    
    # Check if the guild is a premium guild
    @nextcord.slash_command(name="premium", description="Check if the guild is a premium guild.")
    async def premium(self, ctx):
        if os.path.exists(f"assets/config/{ctx.guild.id}.json"):
            with open(f"assets/config/{ctx.guild.id}.json", "r") as f:
                data = f.read()
            config = json.loads(data)
            if "guild" in config:
                if config["guild"]["premium_expires"]:
                    await ctx.send(f"This guild is a premium guild. Premium ends at {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(config["guild"]["premium_expires"]))}.")
                else:
                    await ctx.send("This guild is not a premium guild.")
            else:
                await ctx.send("This guild is not a premium guild.")
        else:
            await ctx.send("This guild is not a premium guild.")
    
    # Set the guild as a premium guild
    @nextcord.slash_command(name="set_premium", description="Set the guild as a premium guild.", dm_permission=False, default_member_permissions=nextcord.Permissions(administrator=True))
    async def set_premium(self, interaction: nextcord.Interaction, premium_duration: int):
        if interaction.user.id != "942460873614712863":
            if os.path.exists(f"assets/config/{interaction.guild.id}.json"):
                with open(f"assets/config/{interaction.guild.id}.json", "r") as f:
                    data = f.read()
                config = json.loads(data)
                if "guild" in config:
                    if config["guild"]["premium"] == False:
                        config["guild"]["premium"] = True
                        config["guild"]["premium_expires"] = round(time.time() + (premium_duration * 86400))
                        with open(f"assets/config/{interaction.guild.id}.json", "w") as f:
                            f.write(json.dumps(config, indent=4))
                        await interaction.response.send_message(f"{interaction.guild.name} is now a premium guild for {premium_duration} days.")
                    else:
                        config["guild"]["premium_expires"] += round(premium_duration * 86400)
                        with open(f"assets/config/{interaction.guild.id}.json", "w") as f:
                            f.write(json.dumps(config, indent=4))
                        await interaction.response.send_message(f"{interaction.guild.name} is now a premium guild for {premium_duration} more days. Premium ends at {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(config["guild"]["premium_expires"]))}.")
                else:
                    await interaction.response.send_message(f"{interaction.guild.name} is not a premium guild.")
            else:
                await interaction.response.send_message(f"{interaction.guild.name} is not a premium guild.")
        else:
            await interaction.response.send_message("You are not allowed to run this command.")

    # Remove the guild as a premium guild
    @nextcord.slash_command(name="remove_premium", description="Remove the guild as a premium guild.", dm_permission=False, default_member_permissions=nextcord.Permissions(administrator=True))
    async def remove_premium(self, interaction: nextcord.Interaction):
        if interaction.user.id != "942460873614712863":
            if os.path.exists(f"assets/config/{interaction.guild.id}.json"):
                with open(f"assets/config/{interaction.guild.id}.json", "r") as f:
                    data = f.read()
                config = json.loads(data)
                if "guild" in config:
                    if config["guild"]["premium"]:
                        config["guild"]["premium"] = False
                        config["guild"]["premium_expires"] = None
                        with open(f"assets/config/{interaction.guild.id}.json", "w") as f:
                            f.write(json.dumps(config, indent=4))
                        await interaction.response.send_message(f"{interaction.guild.name} is no longer a premium guild.")
                    else:
                        await interaction.response.send_message(f"{interaction.guild.name} is not a premium guild.")
                else:
                    await interaction.response.send_message(f"{interaction.guild.name} is not a premium guild.")
            else:
                await interaction.response.send_message(f"{interaction.guild.name} is not a premium guild.")
        else:
            await interaction.response.send_message("You are not allowed to run this command.")

    # Check if the guild is a premium guild every 60 seconds and reset the premium status if the premium expires
    async def premium_check(self):
        while True:
            for guild in self.bot.guilds:
                if os.path.exists(f"assets/config/{guild.id}.json"):
                    with open(f"assets/config/{guild.id}.json", "r") as f:
                        data = f.read()
                    config = json.loads(data)
                    if "guild" in config:
                        if config["guild"]["premium"]:
                            if config["guild"]["premium_expires"] < time.time():
                                config["guild"]["premium"] = False
                                config["guild"]["premium_expires"] = None
                                with open(f"assets/config/{guild.id}.json", "w") as f:
                                    f.write(json.dumps(config, indent=4))
                                print(f"{Colors.WARNING()} Guild {guild.name} ({guild.id}) premium status has been reset.")
                            else:
                                pass
            await asyncio.sleep(60)
        
def setup(bot):
    bot.add_cog(PremiumCheck(bot))