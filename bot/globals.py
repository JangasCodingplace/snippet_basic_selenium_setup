import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOT_DIR = os.path.join(BASE_DIR,'bot')
ASSETS_DIR = os.path.join(BOT_DIR,'assets')

CHROMIUM_SYSTEM_STRINGS = {
    'linux':{
        'zip_type':'linux64',
        'driver':'chromedriver'
    },
    'linux2':{
        'zip_type':'linux64',
        'driver':'chromedriver'
    },
    'darwin':{
        'zip_type':'mac64',
        'driver':'chromedriver'
    },
    'win32':{
        'zip_type':'win32',
        'driver':'chromedriver.exe'
    }
}