import pygame as pg

from entities.Entity import Entity


class Tile(Entity):
    def __init__(self, x, y, name, image, game, rotation=0):
        Entity.__init__(self, x, y, name, image, game)
        
        if(rotation):
            self.image = pg.transform.rotate(self.image, 90*rotation)