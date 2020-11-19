from entities.Player import *
from config.Settings import TILESIZE
from scenes.Level import *
from scenes.Scene import *
from entities.Tile import *


class Town(Level):
    def __init__(self, tilemap, objectmap, scene, game):
        Level.__init__(self, tilemap, objectmap, scene, game)
        self.readTiles()
        self.readObjects()


    def readTiles(self):
        with open(self.tilemap, "rt") as f:
            for row, line in enumerate(f):
                for column, tile in enumerate(line):
                    if(tile == "."):
                        t = Tile(row*TILESIZE, column*TILESIZE, "grass", self.game.tiles["grass_tile"], self.game)

                        self.scene.addTile(self.scene, t)

        # print(self.game.tiles)

    def readObjects(self):
        with open(self.objectmap, "rt") as f:
            for row, line in enumerate(f):
                for column, tile in enumerate(line):
                    # print(tile)
                    if(tile == "P"):
                        e = Player(32, 32, "player", self.game.chars["player"], self.game)

                        self.scene.addObject(self.scene, e)
                        # print("?")

       