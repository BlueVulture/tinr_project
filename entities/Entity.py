import pygame as pg
from config.Settings import *


class Entity(pg.sprite.Sprite):
    """ Entity """
    def __init__(self, position, name, image, game, entityID, scale=(1, 1), rect=None):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.name = name
        self.tags = []
        self.scale = scale
        self.image = image
        self.id = entityID

        self.x = position[0]
        self.y = position[1]

        if self.image is None:
            self.rect = pg.Rect(self.x, self.y, TILESIZE*self.scale[0], TILESIZE*self.scale[1])
            if rect:
                self.rect = pg.Rect(rect)
        else:
            preScale = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(preScale.width*scale[0]), int(preScale.height*scale[1])))
            self.rect = self.image.get_rect()

        if scale < (1, 1):
            self.x = position[0] + (TILESIZE - self.rect.width)/2
            self.y = position[1] + (TILESIZE - self.rect.height)/2

        self.rect.x = self.x
        self.rect.y = self.y

        self.components = {}
        self.game = game
        self.scene = self.game.level.scene

    def init(self):
        pass

    def update(self):
        for key, c in self.components.items():
            c.update()

    def getPosition(self):

        return round(self.x, 2), round(self.y, 2)

    def addComponent(self, component, args=None):
        if args is None:
            self.components[component.__name__] = component
        else:
            self.components[component.__name__] = component(self, args)

    def changeImage(self, image):
        if type(image) == str:
            self.image = self.game.named_images[image]
        else:
            self.image = self.game.all_images[image]

        preScale = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(preScale.width * self.scale[0]), int(preScale.height * self.scale[1])))


    def addTag(self, tag):
        self.tags.append(tag)