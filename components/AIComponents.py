import datetime
from components.Components import *
import pygame as pg
from random import *

from components.PhysicsComponents import Rigidbody, CircleCollider
from components.Timer import Timer
from physics.Math import *


class EnemyAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt
        self.weapon = self.checkArgs("weapon")
        self.camera = self.parent.game.renderer.camera
        self.screen = self.parent.game.renderer.screen

    def update(self):
        pass

    def draw(self):
        if self.weapon:
            self.screen.blit(self.parent.game.all_images[self.weapon],
                             self.camera.applyPosition((self.parent.x, self.parent.y)))

    def collisionDetected(self, collider, colType=None):
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


class RangedEnemyAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt
        self.weapon = self.checkArgs("weapon")
        self.camera = self.parent.game.renderer.camera
        self.screen = self.parent.game.renderer.screen
        self.vector = self.checkArgs("vector")
        self.projSpeed = self.checkArgs("projSpeed")

    def update(self):
        pass

    def draw(self):
        if self.weapon:
            self.screen.blit(self.parent.game.all_images[self.weapon],
                             self.camera.applyPosition((self.parent.x, self.parent.y)))

    def collisionDetected(self, collider, colType=None):
        # print("Enemy in sights!")
        self.rangedWeaponAttack(collider)

    def rangedWeaponAttack(self, object):
        if "player" in object.tags:
            direction = pg.Vector2(0, 0)
            direction.x = object.x - self.parent.x
            direction.y = object.y - self.parent.y

            if direction.length() != 0:
                direction = direction.normalize()

            p = self.Projectile(self, self.weapon, self.vector, self.projSpeed)
            self.parent.game.level.scene.addEntity(p, object, 3, updatable=True)


class Projectile:
    def __init__(self, parent, image, vector, speed):
        self.parent = parent
        self.image = image
        self.vector = vector
        self.speed = speed
        self.timer = Timer(5 * 1000, self.parent.parent.game)
        self.components = []
        self.components.append(Rigidbody)
        self.components.append(CircleCollider)

    def update(self):
        if self.timer.checkTime():
            self.die()

    def collisionDetected(self, collider, colType=None):
        # print("Enemy in sights!")
        self.rangedWeaponAttack(collider)

    def die(self):
        self.parent.parent.game.level.scene.removeEntity(self)


class AnimalAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt
        self.target = (self.parent.x, self.parent.y)
        self.current = (self.parent.x, self.parent.y)
        self.danger = False

    def update(self):
        if not self.danger:
            seed(pg.time.get_ticks())
            if self.aroundTarget(32):
                self.target = (
                self.current[0] + (randrange(32, 64, 1) * randomNegative(self.current[0])), self.current[1] +
                (randrange(32, 64, 1) * randomNegative(self.current[1])))
            else:
                self.moveTowards(self.target)

        self.danger = False

    def aroundTarget(self, distance):
        # print((self.current, self.target))
        if abs(euclidean(self.current, self.target)) < distance:
            return True
        return False

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

    def collisionDetected(self, collider, colType=None):

        self.moveAway(collider)

    def moveAway(self, object):
        if "player" in object.tags:
            direction = pg.Vector2(0, 0)
            direction.x = self.parent.x - object.x
            direction.y = self.parent.y - object.y

            if direction.length() != 0:
                direction = direction.normalize()

            self.parent.x += direction.x * (self.speed * 1.5) * self.dt
            self.parent.y += direction.y * (self.speed * 1.5) * self.dt

            self.parent.rect.x = self.parent.x
            self.parent.rect.y = self.parent.y

            self.target = (0, 0)
            self.danger = True


class WanderingAI(Component):
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

    def collisionDetected(self, collider, colType=None):
        pass

    def aroundTarget(self, distance):
        # print((self.current, self.target))
        if abs(euclidean(self.current, self.target)) < distance:
            return True
        return False
