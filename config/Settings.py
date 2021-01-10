import pathlib
import pygame as pg
import json

# Load from
RESOURCES = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\resources\\"
SOUNDS = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\resources\\sounds\\"
TILEMAPS = RESOURCES + "\\tilemaps\\"

# Basic window variables
WIDTH = 1366
HEIGHT = 768
WINSIZE = [WIDTH, HEIGHT]
TITLE = "Game"
FPS = 60
ICON = "medievalEnvironment_03.png"

# Basic game variables
TILESIZE = 64
PLAYER_SPEED = 512
TM_ROW = 16
TM_COL = 16
IMAGE_TILESIZE = 16
DEFAULT_POSITION = (100, 100)
DEBUG = True
GAME_FONT = "fonts\\pixel.ttf"

# Controls
INTERACT_KEY = pg.K_f

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHTGREY = (128, 128, 128)


def changeSetting(game, setting, value=None, switch=False):
    game.settings[setting] = setSetting(game, setting, switch, value)


def setSetting(game, setting, switch, value):
    if switch:
        return not game.settings[setting]
    elif value:
        return value

    return False


def saveSettings(game):
    data = game.settings

    with open('config/settings.json', 'w') as outfile:
        json.dump(data, outfile)


def readSettings(game):
    with open('config/settings.json', 'r') as infile:
        data = json.load(infile)
        game.settings = data
