import pathlib

# Load from
RESOURCES = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\resources\\"
TILEMAPS = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\tilemaps\\generated\\"

# Basic window variables
WIDTH = 1024
HEIGHT = 512
WINSIZE = [WIDTH, HEIGHT]
TITLE = "Game"
FPS = 60
ICON = "medievalEnvironment_03.png"

# Basic game variables
TILESIZE = 64
PLAYER_SPEED = 375
TM_ROW = 16
TM_COL = 16

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Entities
rooster = {
    "name": "rooster",
    "components": {
        "Movable": {
            "Vector": (10, 20)
        }
    }
}
