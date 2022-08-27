"""Initialize all cogs here"""

from . import (
    cat,
    dog,
    general,
    sudoku
)


async def setup(bot):
  """Setup all cogs"""

  await general.setup(bot)
  await cat.setup(bot)
  await dog.setup(bot)
  await sudoku.setup(bot)
