from .logging import Logging
from .premium_check import PremiumCheck
from .config import Config

def setup(bot):
    bot.add_cog(Logging(bot))
    bot.add_cog(PremiumCheck(bot))
    bot.add_cog(Config(bot))