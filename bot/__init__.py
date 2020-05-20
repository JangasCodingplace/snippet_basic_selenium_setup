from . import *

"""
DIR INITIALIZATION
"""
import os
BOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BOT_DIR,'assets')

if not os.path.exists(ASSETS_DIR):
    os.mkdir(ASSETS_DIR)
