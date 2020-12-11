from components.PhysicsComponents import Movable
import pygame as pg
from entities.Entity import Entity


class Rooster(Entity):
    def __init__(self, position, name, image, game):
        Entity.__init__(self, position, name, image, game)
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        pass
        # print(self.rect)
        # if self.is_collided_with(self.game.level.scene.objects[0]):
        #     self.addComponent(Movable, {"vector": pg.Vector2(50, 0)})

    # def is_collided_with(self, sprite):
    #     return self.rect.colliderect(sprite.rect)

