import pygame as pg
from pygame import *
from config.Settings import *


class Renderer:
    def __init__(self, game, grid=False, debug=False):
        self.game = game
        self.screen = game.gameDisplay.screen
        self.grid = grid
        self.debug = debug

    def render(self):
        for t in self.game.level.scene.tiles:
            self.screen.blit(t.image, t.getPosition())

        if self.grid:
            self.drawGrid()

        for o in self.game.level.scene.objects:
            self.screen.blit(o.image, (o.getPosition()))
            if "MultiTile" in o.components.keys():
                multi = o.components["MultiTile"]
                multi.draw(self.screen)

            if self.debug:
                self.drawColliders(o)
        # self.game.entities_g.draw(self.screen)

        display.update()

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def drawColliders(self, object):
        rect = object.rect
        pg.draw.rect(self.screen, RED, (rect.x, rect.y, rect.width, rect.height), 10)

        if "BoxCollider" in object.components.keys():
            object.components["BoxCollider"].draw(self.screen, GREEN, 3)

        if "CircleCollider" in object.components.keys():
            object.components["CircleCollider"].draw(self.screen, BLUE, 3)
