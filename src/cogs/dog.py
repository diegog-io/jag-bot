"""A module dedicated to dogs"""

import requests
from discord.ext import commands


class DogCog(commands.Cog):
  """Everything needed to add the following dog commands"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  async def dog(self, ctx):
    """Sends an image of a dog"""

    res = requests.get('https://dog.ceo/api/breeds/image/random')
    data = res.json()
    image = data['message']
    await ctx.channel.send(image)

  @commands.command(pass_context=True, name='dog-fact')
  async def dog_fact(self, ctx):
    """Sends a fact about dogs"""

    res = requests.get('https://dog-api.kinduff.com/api/facts')
    data = res.json()
    fact = data['facts'][0]
    await ctx.channel.send(fact)


async def setup(bot):
  """Eases the setup of the cog. to be used in /src/bot.py"""

  await bot.add_cog(DogCog(bot))
