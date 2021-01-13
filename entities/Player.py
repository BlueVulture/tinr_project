import pygame as pg

from components.Timer import Timer
from config.Settings import *
from data.ImageList import *
from entities.Entity import Entity
from physics.Math import *


class Player(Entity):
    def __init__(self, position, name, image, game, entityID, scale=(1, 1), rect=None):
        Entity.__init__(self, position, name, image, game, entityID, scale=scale, rect=rect)
        self.vx, self.vy = 0, 0
        self.moving = False
        self.sound = None
        self.label = None
        self.health = 10
        self.speed = PLAYER_SPEED
        self.reloading = False
        self.reloadTimer = Timer(1, self.game)
        self.generator = self.game.level.generator
        self.projImage = ARROW
        self.damage = 1

    def init(self):
        self.sound = self.components["SoundEffect"]
        self.label = self.game.gui.getElement(name="Position")
        # self.label = self.game.gui.c

    def damaged(self, damage):
        self.health -= damage

    def update(self):
        self.checkSprint()

        if self.reloading:
            if self.reloadTimer.checkTime():
                self.reloading = False
                self.reloadTimer.reset()
            # print(self.reloadTimer.currentTime)
        else:
            self.checkMouse()

        if self.health <= 0:
            self.game.gameOver()
        self.move()

        if self.sound:
            self.playSound()

        if self.label:
            self.label.setText(self.getPosition())

    def move(self):
        velocity = pg.Vector2((0, 0))
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            velocity.x = -1
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            velocity.x = 1
        if keys[pg.K_UP] or keys[pg.K_w]:
            velocity.y = -1
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            velocity.y = 1

        if velocity.length() != 0:
            velocity = velocity.normalize()

        self.x += velocity.x * self.speed * self.game.dt
        self.y += velocity.y * self.speed * self.game.dt

        self.rect.x = self.x
        self.rect.y = self.y

        if velocity.x != 0 or velocity.y != 0:
            self.moving = True
        else:
            self.moving = False

        # print(velocity)

    def playSound(self):
        if self.moving:
            # print("playing")
            self.sound.playSoundOnRepeat()

    def checkSprint(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LSHIFT]:
            self.speed = PLAYER_SPEED * 2
        else:
            self.speed = PLAYER_SPEED

    def checkMouse(self):
        for e in self.game.events:
            if e.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                pos = self.game.renderer.camera.screenToWorld(pos)
                print("shoot!", pos)
                self.shoot(pos)

    def shoot(self, position):
        self.reloading = True
        p = self.generator.generate("arrow", (self.x, self.y), gid=self.projImage + 1)
        direction = pg.Vector2(0, 0)
        direction.x = position[0] - self.x
        direction.y = position[1] - self.y

        if direction.length() != 0:
            direction = direction.normalize()

        angle = angleBetweenVectors((0, -1), direction)
        print(angle)

        p.components["Projectile"].vector = pg.Vector2(direction)
        p.components["Projectile"].damage = self.damage
        p.components["Rotatable"].setRotation(45-angle)
        p.components["Projectile"].firedFrom = self
        self.game.level.scene.addEntity(p, "object", 3, p.id, updatable=True)
