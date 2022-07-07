"""Sets up and adds the bot to it's servers"""

import logging
from discord.ext import commands
from config import Config
from cogs import setup as set_up_cogs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')
set_up_cogs(bot)

bot.run(Config.discord_key)
