from entities.Entity import Entity
from pygame import *
import pygame as pg


class Tile(Entity):
    def __init__(self, x, y, name, image, game, rotation=0):
        self.groups = game.all_sprites, game.tiles_g
        Entity.__init__(self, x, y, name, image, game)
        
        if(rotation):
            self.image = pg.transform.rotate(self.image, 90*rotation)