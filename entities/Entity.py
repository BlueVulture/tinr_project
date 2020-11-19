from config.Settings import *
from pygame import *
import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, name, image, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.name = name
        self.image = image

    def update(self):
        # print((self.x, self.y))
        pass

    def getPosition(self):
        return (self.x, self.y)