import pygame as pg
from config.Settings import *


class Camera:
    def __init__(self, width, height):
        self.rect = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.rect.topleft)

    def applyPosition(self, position):
        return position[0] + self.rect.x, position[1] + self.rect.y

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
