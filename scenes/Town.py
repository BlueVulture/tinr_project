from config.Settings import TILESIZE
from scenes.Level import *
from scenes.Scene import *
from entities.Tile import *


class Town(Level):
    def readTiles(self):
        with open(self.tilemap, "rt") as f:
            for row, line in enumerate(f):
                for column, tile in enumerate(line):
                    if(tile == "."):
                        self.scene.addTile(Tile(row*TILESIZE, column*TILESIZE, "grass", self.tilesImg["grass_tile"] ))

    def readObjects(self):
        array = []
        with open(self.objectmap, "rt") as f:
            for line in f:
                array.append(line)

        # for i, line in enumerate(array):
        #     for j, object in enumerate(line):
        #         if()