import pygame as pg

from components.Components import Component
from config.Settings import *


class PlayerMovement(Component):
    def __init__(self, entity):
        self.entity = entity

    def update(self):
        self.entity.vx, self.entity.vy = 0, 0
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.entity.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.entity.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.entity.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.entity.vy = PLAYER_SPEED
        if self.entity.vx != 0 and self.entity.vy != 0:
            self.entity.vx *= 0.7071
            self.entity.vy *= 0.7071

        self.entity.x += self.entity.vx * self.entity.game.dt
        self.entity.y += self.entity.vy * self.entity.game.dt

        self.entity.rect.x = self.entity.x
        self.entity.rect.y = self.entity.y
