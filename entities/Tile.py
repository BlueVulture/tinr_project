import pygame as pg

from entities.Entity import Entity


class Tile(Entity):
    def __init__(self, position, name, image, game, entityID, rotation=0, scale=(1, 1), rect=None):
        Entity.__init__(self, position, name, image, game, entityID)
        
        if rotation:
            self.image = pg.transform.rotate(self.image, 90*rotation)
