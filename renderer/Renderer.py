import pygame as pg
from pygame import *
from config.Settings import *
from interface.GuiManager import *
from physics.Math import *


class Renderer:
    def __init__(self, game, grid=False, debug=False):
        self.game = game
        self.screen = game.gameDisplay.screen
        self.grid = grid
        self.debug = debug
        self.camera = None
        self.guiRenderer = None
        self.cover = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
        self.cover.set_alpha(128)
        self.cover.fill(BLACK)
        self.delayed = []

    def setGuiRenderer(self, guiRenderer):
        self.guiRenderer = guiRenderer

    def setCamera(self, camera):
        self.camera = camera

    def draw(self, entity):
        if entity.image and self.isOnScreen(entity):
            self.screen.blit(entity.image, self.camera.apply(entity))

    def drawSurface(self, surface, position):
        self.screen.blit(surface, self.camera.applyPosition(position))

    def addToQueue(self, surface, position):
        """ Add surface to queue for later bliting """
        self.delayed.append((surface, position))

    def render(self):
        self.screen.fill(BLACK)

        for layer in self.game.level.scene.layers:
            if layer:
                for t in layer:
                    self.draw(t)

        for o in self.game.level.scene.updatable:
            for k, c in o.components.items():
                # if o.name == "campfire":
                #     print(o.name)
                c.draw()

        if self.grid:
            self.drawGrid()

        if self.debug and DEBUG:
            self.drawColliders()

        for q in self.delayed:
            self.drawSurface(q[0], q[1])

        self.drawGui()
        self.drawMenu()

        self.delayed = []
        display.update()

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def drawGui(self):
        if self.guiRenderer and self.game.drawGui:
            if self.debug and DEBUG:
                self.guiRenderer.render(True)
            else:
                self.guiRenderer.render(False)

    def drawMenu(self):
        if self.game.paused:
            self.screen.blit(self.cover, (0, 0))

        if self.game.showMenu:
            self.game.menuManager.render(self.debug)
            if self.debug and DEBUG:
                pg.draw.line(self.screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

    def drawColliders(self):
        # rect = object.rect
        # rPos = self.camera.applyPosition((rect.x, rect.y))
        # pg.draw.rect(self.screen, RED, (rPos[0], rPos[1], rect.width, rect.height), 10)
        for o in self.game.level.scene.updatable:
            if "BoxCollider" in o.components.keys():
                o.components["BoxCollider"].drawCollider(self.screen, GREEN, 3, self.camera)

            if "CircleCollider" in o.components.keys():
                o.components["CircleCollider"].drawCollider(self.screen, BLUE, 3, self.camera)

    def isOnScreen(self, entity):
        c = self.camera
        m = (TILESIZE * 2)  # Margin - needed especially with (x, y)
        return positionWithin(entity.rect, (-c.rect.x - m, -c.rect.y - m, c.width + m, c.height + m))
