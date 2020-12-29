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
        self.game.gui.getElement(name="CameraOffset").setText(str(self.camera.rect.x) + " " + str(self.camera.rect.y))
        self.screen.fill(BLACK)

        for layer in self.game.level.scene.layers:
            if layer:
                for t in layer:
                    self.draw(t)

        if self.grid:
            self.drawGrid()

        for o in self.game.level.scene.updatable:
            if self.debug and DEBUG:
                self.drawColliders(o)

        for q in self.delayed:
            self.drawSurface(q[0], q[1])

        if self.guiRenderer:
            if self.debug and DEBUG:
                self.guiRenderer.render(True)
            else:
                self.guiRenderer.render(False)

        if self.game.paused:
            self.screen.blit(self.cover, (0, 0))
        # gameFont = pg.font.SysFont("monospace", 15)
        # self.drawText(gameFont.render("text", True, BLACK), (832, 3000))

        self.delayed = []
        display.update()

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def drawColliders(self, object):
        # rect = object.rect
        # rPos = self.camera.applyPosition((rect.x, rect.y))
        # pg.draw.rect(self.screen, RED, (rPos[0], rPos[1], rect.width, rect.height), 10)

        if "BoxCollider" in object.components.keys():
            object.components["BoxCollider"].draw(self.screen, GREEN, 3, self.camera)

        if "CircleCollider" in object.components.keys():
            object.components["CircleCollider"].draw(self.screen, BLUE, 3, self.camera)

    def isOnScreen(self, entity):
        c = self.camera
        m = (TILESIZE * 2)  # Margin - needed especially with (x, y)
        return positionWithin(entity.rect, (-c.rect.x - m, -c.rect.y - m, c.width + m, c.height + m))
