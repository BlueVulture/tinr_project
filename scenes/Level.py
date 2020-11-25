from random import randrange
from entities.Player import *
from config.Settings import TILESIZE
from scenes.Level import *
from scenes.Scene import *
from entities.Tile import *

class Level:
    scene = Scene()

    def __init__(self, tilemap, objectmap, scene, game):
        self.tilemap = TILEMAPS + tilemap
        self.objectmap = TILEMAPS + objectmap
        self.scene = scene
        self.game = game

        self.readTiles()
        self.readObjects()
    
    def readTiles(self):
        t = None
        name, tileName = "", ""
        with open(self.tilemap, "rt") as f:
            for row, line in enumerate(f):
                for column, tile in enumerate(line):
                    rotation = randrange(4)
                    if(tile == "."):
                        name, tileName = "grass", "grass_tile_1"
                    elif(tile == ","):
                        name, tileName = "grass", "grass_tile_2"

                    t = Tile(row*TILESIZE, column*TILESIZE, name, self.game.tiles[tileName], self.game, rotation)
                    self.scene.addTile(self.scene, t)


    def readObjects(self):
        e = None
        with open(self.objectmap, "rt") as f:
            for row, line in enumerate(f):
                for column, tile in enumerate(line):
                    if(tile == "P"):
                        e = Player(row*TILESIZE, column*TILESIZE, "player", self.game.chars["npc"], self.game)
                    elif(tile == "C"):
                        e = Entity(row*TILESIZE, column*TILESIZE, "campfire", self.game.objects["campfire"], self.game)

                    if(tile != "." and tile != "\n"):
                        self.scene.addObject(self.scene, e)
                        print(e)