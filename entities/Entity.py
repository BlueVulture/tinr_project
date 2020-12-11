import pygame as pg
from config.Settings import *


class Entity(pg.sprite.Sprite):
    """ Entity """
    def __init__(self, position, name, image, game, scale=(1, 1)):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.name = name
        self.scale = scale
        self.image = image

        if image is None:
            self.rect = pg.Rect(self.x, self.y, TILESIZE*self.scale[0], TILESIZE*self.scale[1])
        else:
            preScale = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(preScale.width*scale[0]), int(preScale.height*scale[1])))
            self.rect = self.image.get_rect()
        if scale < (1, 1):
            self.x = position[0] + (TILESIZE - self.rect.width)/2
            self.y = position[1] + (TILESIZE - self.rect.height)/2
        else:
            self.x = position[0]
            self.y = position[1]
        self.rect.x = self.x
        self.rect.y = self.y

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
