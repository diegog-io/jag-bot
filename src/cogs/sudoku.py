"""A sudoku module"""

from datetime import date
from discord.ext import commands, tasks


class SudokuCog(commands.Cog):
  """Everything needed to add the following sudoku commands"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True, name='sudoku')
  async def send_daily_sudoku(self, ctx):
    """retrieves daily sudoku image"""

    d = date.today()
    url = f'http://www.dailysudoku.com/sudoku/png/{d.year}/{d.month:02d}/{d.year}-{d.month:02d}-{d.day}.png'

    await ctx.channel.send(url)


def setup(bot):
  """Eases the setup of the cog. to be used in /src/bot.py"""
  bot.add_cog(SudokuCog(bot))
