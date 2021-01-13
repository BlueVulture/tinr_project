import pygame as pg
from config.Settings import *
from physics.Math import subTuples, sumTuples


class Camera:
    def __init__(self, width, height):
        self.rect = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.rect.topleft)

    def applyPosition(self, position):
        return position[0] + self.rect.x, position[1] + self.rect.y

    def screenToWorld(self, position):
        worldCenter = ((self.rect.x+(-self.width/2))*-1, (self.rect.y+(-self.height/2))*-1)
        screenCenter = (self.width/2, self.height/2)
        offset = subTuples(position, screenCenter)

        return sumTuples(worldCenter, offset)

    def update(self, target):
        # print(self.camera)
        x = -target.rect.x - target.rect.width/2 + int(WIDTH / 2)
        y = -target.rect.y - target.rect.height/2 + int(HEIGHT / 2)
        # x = -target.rect.x - target.rect.width / 2 + int(WIDTH / 2)
        # y = -target.rect.y - target.rect.height / 2 + int(HEIGHT / 2)

        # limit scrolling to map size
        # x = min(0, x)  # left
        # y = min(0, y)  # top
        # x = max(-(self.width - WIDTH), x)  # right
        # y = max(-(self.height - HEIGHT), y)  # bottom
        self.rect.x = x
        self.rect.y = y
