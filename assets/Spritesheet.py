import pygame as pg
from pygame import *

from config.Settings import *


class Spritesheet:
    def __init__(self, filename, tilesize=16):
        self.sheet = image.load(RESOURCES + "spritesheets\\" + filename)
        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.tilesize = tilesize

    def imageAt(self, rectangle, colorkey=None, scale=None):
        """Load a specific image from a specific rectangle."""
        if scale is None:
            scale = int(TILESIZE / self.tilesize)

        # Loads image from x, y, x+offset, y+offset.
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size, pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        # print(str(rect.width) + " " + str(rect.height))
        image = pg.transform.scale(image, (rect.width * scale, rect.height * scale))

        return image

    def imagesAt(self, rects, colorkey=None, scale=1):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey, scale) for rect in rects]

    def loadStrip(self, rect, image_count, colorkey=None, scale=1):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey, scale)
