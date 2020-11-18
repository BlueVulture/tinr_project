from scenes.Scene import *

class Level:
    scene = Scene()
    tilesImg = {}
    charsImg = {}

    def __init__(self, tilemap, objectmap, scene, tilesImg, charsImg):
        self.tilemap = tilemap
        self.objectmap = objectmap
        self.scene = scene
        self.tilesImg = tilesImg
        self.charsImg = charsImg

    