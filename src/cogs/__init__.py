"""Initialize all cogs here"""

from . import (
    cat,
    dog,
    general,
    sudoku
)


def setup(bot):
  """Setup all cogs"""

  general.setup(bot)
  cat.setup(bot)
  dog.setup(bot)
  sudoku.setup(bot)
