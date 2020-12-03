import pygame as pg
from pygame import *

from assets.Loader import *
from assets.Spritesheet import *
from entities.Player import *
from renderer.DisplayManager import *
from renderer.Renderer import Renderer
from scenes.Town import Town
from physics.PhysicsEngine import *


class Game:
    tiles = {}
    chars = {}
    objects = {}
    level = None

    def __init__(self):
        pg.init()

        # Display
        self.gameDisplay = DisplayManager(WINSIZE, TITLE, ICON)

        # Set clock
        self.clock = time.Clock()
        self.clock.tick()
        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        # Initialize
        self.init()

        # Set up rendered, physics
        self.renderer = Renderer(self)
        self.physics = PhysicsEngine(self)

        # Create spritegroup (for pg.Sprite inheritance)
        self.all_sprites = pg.sprite.Group()

    #
    def load(self):
        # Load sheets
        environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")

        # Load images from sheets into dicts
        self.tiles = loadTiles(environmentSheet)
        self.chars = loadCharacters(charactersSheet)
        self.objects = loadObjects(environmentSheet)

    def init(self):
        # Load all
        self.load()

        # Set level and build it
        self.level = Town("town_tile.txt", "town_obj.txt", self)
        self.level.buildLevel()

        # Diagnostics
        print(self.clock.tick(FPS))
        print(self.level.scene.objects)

    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                display.quit()

        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        for o in self.level.scene.objects:
            o.update()

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
