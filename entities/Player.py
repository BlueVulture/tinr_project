import pygame as pg

from config.Settings import *
from entities.Entity import Entity
from entities.Rooster import Rooster


class Player(Entity):
    def __init__(self, position, name, image, game):
        Entity.__init__(self, position, name, image, game)
        self.vx, self.vy = 0, 0
        self.down = False

    def update(self):
        self.move()
        # print(self.x, self.y)

    def move(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        # if self.vx != 0 and self.vy != 0:
        #     self.vx *= 0.7071
        #     self.vy *= 0.7071

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        self.rect.x = self.x
        self.rect.y = self.y
