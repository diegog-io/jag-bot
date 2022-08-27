"""A module for general tasks/commands"""

import discord
from discord.ext import commands


class GeneralCog(commands.Cog):
  """Everything needed to add the following commands/tasks"""

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    """Sets the status of the bot in discord"""

    await self.bot.change_presence(activity=discord.Game(name='with himself.'))
    print(f'We have logged in as {self.bot.user}')

  @commands.Cog.listener()
  async def on_message(self, message):
    """Sends images if certain words are mentioned in message"""

    if 'jesus' in message.content.lower():
      await message.channel.send('https://media.giphy.com/media/l2SqcLkHQMPLNs3N6/giphy.gif')

    if 'get high' in message.content.lower():
      await message.channel.send('https://media.giphy.com/media/3o6ZteGxdyGycdL5ra/giphy.gif')

  @commands.command(pass_context=True, name='commands')
  async def list_commands(self, ctx):
    """Sends a list of commands"""

    await ctx.channel.send("\
`!commands` provides a list of usable commands \n\
`!clear 5` clears the last 5 messages, if no number is specified the last 100 will be cleared \n\
`!cat` sends a random image of a cat \n\
`!cat-fact` sends a random fact about cats\n\
`!dog` sends a random image of a dog \n\
`!dog-fact` sends a random fact about dogs\n\
`!sudoku` sends a daily sudoku puzzle\n\
\n\
Let jäger#0047 know if you have any suggestions")

  @commands.command(pass_context=True)
  async def clear(self, ctx, arg=100):
    """Clears the previous messages"""
    await ctx.channel.purge(limit=arg+1)

  @commands.command(pass_context=True)
  async def ping(self, ctx):
    await ctx.channel.send('pong');


async def setup(bot):
  """Eases the setup of the cog. to be used in /src/bot.py"""

  await bot.add_cog(GeneralCog(bot))
