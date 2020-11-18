from scenes.Scene import *
from config.Settings import *

class Level:
    scene = Scene()

    def __init__(self, tilemap, objectmap, scene, game):
        self.tilemap = TILEMAPS + tilemap
        self.objectmap = TILEMAPS + objectmap
        self.scene = scene
        self.game = game
    