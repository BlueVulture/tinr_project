from renderer.Renderer import Renderer
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

    def __init__(self):
        pg.init()
        self.gameDisplay = DisplayManager(WINSIZE, TITLE, ICON)
        
        self.clock = time.Clock()
        self.clock.tick()
        self.init()
        self.renderer = Renderer(self)


    def load(self):
        environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")

        self.tiles = Loader.loadTiles(environmentSheet)
        self.chars = Loader.loadCharacters(charactersSheet)


    def init(self):
        self.load()

        self.all_sprites = pg.sprite.Group()
        self.tiles_g = pg.sprite.Group()
        self.entities_g = pg.sprite.Group()
        
        self.level = Town("town_tile.txt", "town_obj.txt", Scene, self)
        print(self.clock.tick(FPS))
        print(self.clock.tick(FPS)/1000)


    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                display.quit()

        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        self.entities_g.update()
        

    def draw(self): 
        self.renderer.render()


    def run(self):
        self.clock.tick(FPS)
        self.update()
        self.draw()

g = Game()

done = False
while not done:
    g.run()
    
