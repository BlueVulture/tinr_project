import datetime
from components.Components import *
import pygame as pg
from random import *
from physics.Math import *


class enemyAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt

    def update(self):
        pass

    def collisionDetected(self, collider):
        # print("Enemy in sights!")
        self.moveTowards(collider)

    def moveTowards(self, object):
        if "player" in object.tags:
            direction = pg.Vector2(0, 0)
            direction.x = object.x - self.parent.x
            direction.y = object.y - self.parent.y

            if direction.length() != 0:
                direction = direction.normalize()

            self.parent.x += direction.x * self.speed * self.dt
            self.parent.y += direction.y * self.speed * self.dt

            self.parent.rect.x = self.parent.x
            self.parent.rect.y = self.parent.y


class animalAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt

    def update(self):
        pass

    def collisionDetected(self, collider):
        # print("Enemy in sights!")
        self.moveAway(collider)

    def moveAway(self, object):
        if "player" in object.tags:
            direction = pg.Vector2(0, 0)
            direction.x = self.parent.x - object.x
            direction.y = self.parent.y - object.y

            if direction.length() != 0:
                direction = direction.normalize()

            self.parent.x += direction.x * self.speed * self.dt
            self.parent.y += direction.y * self.speed * self.dt

            self.parent.rect.x = self.parent.x
            self.parent.rect.y = self.parent.y


class wanderingAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt
        self.target = (self.parent.x, self.parent.y)
        self.current = (self.parent.x, self.parent.y)

    def update(self):
        seed(pg.time.get_ticks())
        if self.aroundTarget(32):
            self.target = (self.current[0] + (randrange(64, 65, 1) * randomNegative(self.current[0])), self.current[1] +
                           (randrange(64, 65, 1) * randomNegative(self.current[1])))
        else:
            self.moveTowards(self.target)

    def moveTowards(self, position):
        direction = pg.Vector2(0, 0)
        direction.x = position[0] - self.parent.x
        direction.y = position[1] - self.parent.y

        if direction.length() != 0:
            direction = direction.normalize()

        self.parent.x += direction.x * self.speed * self.dt
        self.parent.y += direction.y * self.speed * self.dt

        self.parent.rect.x = self.parent.x
        self.parent.rect.y = self.parent.y

        self.current = self.parent.getPosition()

    def collisionDetected(self, collider):
        pass

    def aroundTarget(self, distance):
        # print((self.current, self.target))
        if abs(euclidean(self.current, self.target)) < distance:
            return True
        return False
