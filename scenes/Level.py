from random import *
from config.Settings import *
from config.EntitiesList import *
from entities.Campfire import Campfire
from entities.Generator import Generator
from entities.Player import Player
from entities.Rooster import Rooster
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
                for column, tile in enumerate(line):
                    rotation = randrange(4)
                    if tile == ".":
                        name, tileName = "grass", "grass_tile_1"
                    elif tile == ",":
                        name, tileName = "grass", "grass_tile_2"

                    t = Tile((column * TILESIZE, row * TILESIZE), name, self.game.tiles[tileName], self.game, rotation)
                    self.scene.addTile(self.scene, t)

    def readObjects(self):
        e = None
        with open(self.objectmap, "rt") as f:
            for row, line in enumerate(f):
                for column, tag in enumerate(line):
                    obj = entityTags[tag]
                    if obj is not None:
                        # self.scene.addObject(self.scene, e)
                        self.scene.addObject(self.scene, self.generator.generate(obj, (column * TILESIZE, row * TILESIZE)))
                        # print(tag)
