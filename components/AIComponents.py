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
        self.generator = self.parent.game.level.generator
        self.speed = self.checkArgs("speed")
        if self.speed is None:
            self.speed = 0
        self.dt = self.parent.game.dt
        self.weapon = self.checkArgs("weapon")
        self.camera = self.parent.game.renderer.camera
        self.screen = self.parent.game.renderer.screen
        self.projSpeed = self.checkArgs("projSpeed")
        self.projImage = self.checkArgs("projImage")
        self.reloading = False
        self.timer = Timer(1, self.parent.game)
        self.damage = self.checkArgs("damage")

    def update(self):
        if self.reloading:
            if self.timer.checkTime():
                self.reloading = False

    def draw(self):
        if self.weapon:
            self.screen.blit(self.parent.game.all_images[self.weapon],
                             self.camera.applyPosition((self.parent.x, self.parent.y)))

    def collisionDetected(self, collider, colType=None):
        # print("Enemy in sights!")
        self.rangedWeaponAttack(collider)
        self.moveAway(collider)

    def rangedWeaponAttack(self, object):
        if "player" in object.tags and not self.reloading:
            self.reloading = True
            p = self.generator.generate("projectile", (self.parent.x, self.parent.y), gid=self.projImage + 1)
            direction = pg.Vector2(0, 0)
            direction.x = object.x - self.parent.x
            direction.y = object.y - self.parent.y

            if direction.length() != 0:
                direction = direction.normalize()

            p.components["Projectile"].vector = pg.Vector2(direction)
            p.components["Projectile"].damage = self.damage
            self.parent.game.level.scene.addEntity(p, "object", 3, p.id, updatable=True)

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


class Projectile(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.originalImage = self.parent.image
        self.speed = self.checkArgs("speed")
        self.screen = self.parent.game.renderer.screen
        self.camera = self.parent.game.renderer.camera
        self.timer = Timer(2, self.parent.game)
        self.vector = pg.Vector2(0, 0)
        self.damage = 0
        self.angle = 0
        self.angle_change = 10

    def update(self):
        # print(self.timer.currentTime)
        self.parent.x += self.vector.x * self.speed * self.parent.game.dt
        self.parent.y += self.vector.y * self.speed * self.parent.game.dt

        # orig_rect = self.originalImage.get_rect()
        # rot_image = pg.transform.rotate(self.originalImage, self.angle)
        # rot_rect = orig_rect.copy()
        # rot_rect.center = rot_image.get_rect().center
        # self.parent.image = rot_image.subsurface(rot_rect).copy()

        self.parent.rect.x = self.parent.x
        self.parent.rect.y = self.parent.y
        self.angle += self.angle_change
        self.angle = self.angle % 360

        if self.timer.checkTime():
            self.die()

    def collisionDetected(self, collider, colType=None):
        # print("goteem")
        if collider.name == "player":
            collider.damaged(self.damage)
            self.die()

    def die(self):
        self.parent.game.level.scene.removeEntity(self.parent, self.parent.id)


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
        self.dialog = self.checkArgs("dialog")
        self.fontSize = self.checkArgs("fontSize", 25)
        self.font = self.checkArgs("font", GAME_FONT)
        self.gameFont = pg.font.SysFont(self.font, self.fontSize)
        self.showDialog = False
        self.timer = Timer(4, self.parent.game)
        self.waitTimer = Timer(randrange(0, 5, 1), self.parent.game)
        self.option = 0
        self.stuck = [self.parent.getPosition()]

    def update(self):
        if self.showDialog:
            if self.timer.checkTime():
                self.showDialog = False
                self.parent.components["Interactable"].displayLabel = True
                self.timer.reset()
            else:
                self.displayDialog()

        seed(pg.time.get_ticks())
        if self.aroundTarget(32):
            if self.wait():
                self.newTarget()
        else:
            self.moveTowards(self.target)
            if self.checkIfStuck():
                self.newTarget()

    def newTarget(self):
        self.target = (self.current[0] + (randrange(64, 128, 1) * randomNegative(self.current[0])), self.current[1] +
                       (randrange(64, 65, 1) * randomNegative(self.current[1])))

    def wait(self):
        return self.waitTimer.checkTime()

    def checkIfStuck(self):
        if len(self.stuck) > 75:
            s = n = 0
            for pos in self.stuck:
                s += euclidean(pos, self.parent.getPosition())
                n += 1

            if s / n < 10:
                self.newTarget()

            self.stuck = []
        else:
            self.stuck.append(self.parent.getPosition())

    def interact(self):
        r = randrange(0, len(self.dialog), 1)
        self.option = r
        self.showDialog = True
        self.parent.components["Interactable"].displayLabel = False
        self.timer.reset()

    def displayDialog(self):
        label = self.gameFont.render(self.dialog[self.option], True, WHITE)
        x = self.parent.x - label.get_rect().width / 2 + self.parent.rect.width / 2
        position = (x, self.parent.y - self.fontSize - 10)
        self.parent.game.renderer.addToQueue(label, position)

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


class InteractableAI(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.dialog = self.checkArgs("dialog")
        self.step = 0
        self.fontSize = self.checkArgs("fontSize", 25)
        self.font = self.checkArgs("font", GAME_FONT)
        self.gameFont = pg.font.SysFont(self.font, self.fontSize)
        self.showDialog = False

    def update(self):
        if self.showDialog:
            self.displayDialog()

    def interact(self):
        if self.step == 0:
            self.parent.components["Interactable"].displayLabel = False
            self.step += 1
            self.showDialog = True
        elif self.step >= 1:
            self.step += 1

        if self.step > len(self.dialog):
            self.parent.components["Interactable"].displayLabel = True
            self.showDialog = False
            self.step = 0

    def displayDialog(self, option=0):
        label = self.gameFont.render(self.dialog[self.step - 1], True, WHITE)
        x = self.parent.x - label.get_rect().width / 2 + self.parent.rect.width / 2
        position = (x, self.parent.y - self.fontSize - 10)
        self.parent.game.renderer.addToQueue(label, position)
