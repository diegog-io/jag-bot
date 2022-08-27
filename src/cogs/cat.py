"""A module dedicated to cats"""

import requests
from discord.ext import commands


class CatCog(commands.Cog):
  """Everything needed to add the following cat commands"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  async def cat(self, ctx):
    """Sends a cat image where requested"""

    res = requests.get('https://api.thecatapi.com/v1/images/search')
    data = res.json()[0]
    image = data['url']
    await ctx.channel.send(image)

  @commands.command(pass_context=True, name='cat-fact')
  async def cat_fact(self, ctx):
    """Sends a fact about cats where requested"""

    res = requests.get('https://cat-fact.herokuapp.com/facts/random')
    data = res.json()
    fact = data['text']
    await ctx.channel.send(fact)


async def setup(bot):
  """Eases the setup of the cog. to be used in /src/bot.py"""

  await bot.add_cog(CatCog(bot))
