import pygame as pg
from pygame import *
from config.Settings import *
from interface.GuiManager import *


class Renderer:
    def __init__(self, game, grid=False, debug=False):
        self.game = game
        self.screen = game.gameDisplay.screen
        self.grid = grid
        self.debug = debug
        self.camera = None
        self.guiRenderer = None

    def setGuiRenderer(self, guiRenderer):
        self.guiRenderer = guiRenderer

    def setCamera(self, camera):
        self.camera = camera

    def draw(self, entity):
        if entity.image:
            self.screen.blit(entity.image, self.camera.apply(entity))

    def render(self):
        self.screen.fill(BLACK)
        # for t in self.game.level.scene.tiles:
        #    self.draw(t)

        for layer in self.game.level.scene.layers:
            if layer:
                for t in layer:
                    self.draw(t)

        if self.grid:
            self.drawGrid()

        for o in self.game.level.scene.updatable:
            # pass
            # self.draw(o)
            if self.debug:
                self.drawColliders(o)

        if self.guiRenderer:
            self.guiRenderer.render(self.debug)

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
