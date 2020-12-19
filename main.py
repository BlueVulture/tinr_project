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
    all_images = {}
    sounds = {}
    events = None
    level = None

    def __init__(self):
        pg.init()

        # Display
        self.gameDisplay = DisplayManager(WINSIZE, TITLE, ICON)

        # Create spritegroup (for pg.Sprite inheritance)
        self.all_sprites = pg.sprite.Group()

        # Set clock
        self.clock = time.Clock()
        self.clock.tick()
        self.dt = self.clock.tick_busy_loop(FPS) / 1000
        pg.mixer.init(channels=8)

        # Initialize
        self.init()

        # Set up rendered, physics
        self.renderer = Renderer(self, grid=False, debug=True)
        self.physics = PhysicsEngine(self)

    def load(self):
        """ Load resources """
        # Load sheets
        environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")

        # Load images from sheets into dicts
        self.tiles = loadTiles(environmentSheet)
        self.chars = loadCharacters(charactersSheet)
        self.objects = loadObjects(environmentSheet)
        self.all_images = {**self.tiles, **self.chars, **self.objects}
        self.sounds = loadSounds()

    def init(self):
        """ Initialize gamestate """
        # Load all
        self.load()

        # Set level and build it
        self.level = Town("town_tile.txt", "town_obj.txt", self)
        self.level.buildLevel()

        # Diagnostics
        print(self.clock.tick_busy_loop(FPS) / 1000)
        print(self.level.scene.objects)

    def update(self):
        """ Update logic """
        self.events = pg.event.get()
        for e in self.events:
            if e.type == pg.QUIT:
                display.quit()

        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        for o in self.level.scene.objects:
            o.update()

    def physicsUpdate(self):
        """ Update physics """
        self.physics.physicsUpdate()

    def draw(self):
        """ Call to renderer """
        self.renderer.render()

    def run(self):
        """ Gameloop """
        self.clock.tick(FPS)
        self.update()
        self.physicsUpdate()
        self.draw()


g = Game()

done = False
while not done:
    g.run()
