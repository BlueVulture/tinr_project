from entities.Player import *
from config.Settings import TILESIZE
from scenes.Level import *
from scenes.Scene import *
from entities.Tile import *


class Town(Level):
    def __init__(self, tilemap, objectmap, game, scene=None):
        Level.__init__(self, tilemap, objectmap, game, scene)
        


    

       