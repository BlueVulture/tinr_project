from config.Settings import *
from entities.Entity import Entity
from pygame import *
import pygame as pg

class Rooster(Entity):
    def __init__(self, x, y, name, image, game):
        Entity.__init__(self, x, y, name, image, game)
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        # print(self.rect)
        if (self.is_collided_with(self.game.level.scene.objects[0])):
            self.scene.removeObject(self.scene, self)
        
    def getPosition(self):
        return (self.x, self.y)

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

