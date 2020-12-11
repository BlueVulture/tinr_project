from random import *
from config.Settings import *
from config.EntitiesList import *
from entities.Generator import Generator
from entities.Player import Player
from entities.Tile import *
from scenes.Level import *
from scenes.Scene import *
import copy


class Level:
    scene = Scene

    def __init__(self, tilemap, objectmap, game, scene=None):
        self.tilemap = TILEMAPS + tilemap
        self.objectmap = TILEMAPS + objectmap
        self.game = game
        self.generator = Generator(self.game, debug=True)
        if scene:
            self.scene = scene

    def buildLevel(self):
        print(self.scene)
        self.readTiles()
        self.readObjects()

    def readTiles(self):
        name, tileName = "", ""
        with open(self.tilemap, "rt") as f:
            for row, line in enumerate(f):
                for column, tag in enumerate(line):
                    tile = tileTags[tag]
                    rotation = randrange(4)
                    if tile is not None:
                        t = Tile((column * TILESIZE, row * TILESIZE), name, self.game.tiles[tile], self.game,
                                 rotation)
                        self.scene.addTile(self.scene, t)

    def readObjects(self):
        # e = None
        with open(self.objectmap, "rt") as f:
            for row, line in enumerate(f):
                for column, tag in enumerate(line):
                    obj = entityTags[tag]
                    if obj is not None:
                        # self.scene.addObject(self.scene, e)
                        self.scene.addObject(self.scene, self.generator.generate(obj, (column * TILESIZE, row * TILESIZE)))
                        # print(tag)
