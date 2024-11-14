import nextcord, time, os, json
from nextcord.ext import commands
from .colors import Colors

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.start_time = time.time()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Colors.INFO()} Booted up successfully! Ping is {round(self.bot.latency * 1000)}ms. Logged in as {self.bot.user}.")

    async def send_command_feedback(self, command_name, success=True, error_message=None):
        feedback_channel = None
        for guild in self.bot.guilds:
            if os.path.exists(f"assets/config/{guild.id}.json"):
                with open(f"assets/config/{guild.id}.json", "r") as f:
                    data = f.read()
                config = json.loads(data)
                if "feedback_channel" in config:
                    feedback_channel = guild.get_channel(config["feedback_channel"])
        if feedback_channel:
            if success:
                await feedback_channel.send(f"[SUCCES] Command `{command_name}` ran successfully!")
                print(f"{Colors.SUCCESS()} Command `{command_name}` ran successfully!")
            else:
                await feedback_channel.send(f"[ERROR] <@942460873614712863> Command `{command_name}` failed with error: {error_message}")
                print(f"{Colors.ERROR()} Command `{command_name}` failed with error: {error_message}")
        else:
            print(f"{Colors.ERROR()} No feedback channel found in any guild configuration file.")


def setup(bot):
    bot.add_cog(Logging(bot))
