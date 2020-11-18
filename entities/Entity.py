from pygame import *
import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, name, image):
        self.x = x
        self.y = y
        self.name = name
        self.image = image

    def update(self):
        pass

    def getPosition(self):
        return (self.x, self.y)