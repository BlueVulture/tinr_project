import pygame as pg
from config.Settings import *


class Entity(pg.sprite.Sprite):
    """ Entity """
    def __init__(self, position, name, image, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = position[0]
        self.y = position[1]
        self.name = name
        self.image = image
        if image is None:
            self.rect = pg.Rect(self.x, self.y, TILESIZE, TILESIZE)
        else:
            self.rect = self.image.get_rect()
        self.components = {}
        self.game = game
        self.scene = self.game.level.scene

    def update(self):
        pass

    def getPosition(self):
        return self.x, self.y

    def addComponent(self, component, args=None):
        if args is None:
            self.components[component.__name__] = component
        else:
            self.components[component.__name__] = component(self, args)
