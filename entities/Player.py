from config.Settings import *
from entities.Entity import Entity
from pygame import *
import pygame as pg


class Player(Entity):
    def __init__(self, x, y, name, image, game):
        Entity.__init__(self, x, y, name, image, game)
        self.groups = game.all_sprites, game.entities_g
        game.entities_g.add(self)
        self.vx, self.vy = 0, 0

    def update(self):
        self.move()

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
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

        # self.x += self.vx * self.game.dt
        # self.y += self.vy * self.game.dt