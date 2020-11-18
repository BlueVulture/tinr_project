from scenes.Town import Town
from scenes.Scene import Scene
from assets.Loader import Loader
from renderer.DisplayManager import *
from assets.Spritesheet import *
from config.Settings import *
from entities.Player import *
from pygame import *
import pygame as pg
from reloadr import autoreload

class Game():
    tiles = {}
    chars = {}
    data = {}

    def __init__(self):
        pg.init()
        self.D = DisplayManager(WINSIZE, "Game", "medievalEnvironment_03.png")
        self.clock = time.Clock()
        self.clock.tick()
        self.init()


    def load(self):
        environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")

        self.tiles = Loader.loadTiles(environmentSheet)
        self.chars = Loader.loadCharacters(charactersSheet)


    def init(self):
        self.load()
        print(self.tiles)
        self.level = Town("town_tile.txt", "town_obj.txt", Scene, self)
        self.level.readTiles()


    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                display.quit()


    def draw(self): 
        for o in self.level.scene.tiles:
            self.D.screen.blit(self.tiles["grass_tile"], o.getPosition())
        display.update()

    def run(self):
        self.clock.tick(60)
        self.update()
        self.draw()

g = Game()

done = False
while not done:
    g.run()
    
