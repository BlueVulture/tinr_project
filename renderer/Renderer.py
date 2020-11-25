from config.Settings import *
from pygame import *
import pygame as pg

class Renderer:
    def __init__(self, game, grid=False): 
        self.game = game
        self.screen = game.gameDisplay.screen
        self.grid = grid

    def render(self):
        for t in self.game.level.scene.tiles:
            self.screen.blit(t.image, t.getPosition())

        if(self.grid):
            self.draw_grid()

        # for o in self.game.level.scene.objects:
        #     self.screen.blit(o.image, (o.getPosition()))
        self.game.entities_g.draw(self.screen)

       
        display.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))  