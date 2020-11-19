from config.Settings import *
from entities.Entity import Entity
from pygame import *
import pygame as pg


class Player(Entity):
    def __init__(self, x, y, name, image, game):
        Entity.__init__(self, x, y, name, image, game)
        self.groups = game.all_sprites, game.entities_g
        game.entities_g.add(self)

    def update(self):
        self.x += 100 * 1/FPS