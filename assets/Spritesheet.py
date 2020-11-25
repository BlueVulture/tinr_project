from pygame import *
import pygame as pg
from config.Settings import *

class Spritesheet:
    def __init__(self, filename, tilesize=16):
        self.sheet = image.load(RESOURCES + filename)
        self.tilesize = tilesize

    def imageAt(self, rectangle, colorkey = None, scale=None):
        """Load a specific image from a specific rectangle."""
        if(scale == None):
            scale = int(TILESIZE/self.tilesize)
        
        # Loads image from x, y, x+offset, y+offset.
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert() 
        image.blit(self.sheet, (0, 0), rect)
        image = pg.transform.scale(image, (rect[2]*scale, rect[3]*scale))

        return image

    def imagesAt(self, rects, colorkey = None, scale = 1):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey, scale) for rect in rects]

    def loadStrip(self, rect, image_count, colorkey = None, scale = 1):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey, scale)