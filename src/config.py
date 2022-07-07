"""A module to isolate all configurable variables"""
import os


class Config(object):
  """Contains all configurable variables"""

  discord_key = os.environ.get('DISCORD_KEY')
