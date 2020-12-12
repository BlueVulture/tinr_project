from components.Components import *
import pygame as pg


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
        print("Enemy in sights!")
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