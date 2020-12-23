import pygame as pg
from pygame import *

from config.Interface import *
from interface.GuiManager import *
from assets.Loader import *
from assets.Spritesheet import *
from entities.Player import *
from renderer.Camera import Camera
from renderer.DisplayManager import *
from renderer.Renderer import Renderer
from scenes.Town import Town
from physics.PhysicsEngine import *


class Game:
    tiles = {}
    chars = {}
    other = {}
    objects = {}
    all_images = {}
    sounds = {}
    events = None
    level = None
    camera = None
    player = None

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
        pg.mixer.init()

        # Load all
        self.load()

        # Set up renderer
        self.renderer = Renderer(self, grid=False, debug=True)

        # Set up GUI
        self.gui = GuiGenerator(self).generate(interface)
        self.gui.setFont("pixel.ttf", 32)
        self.renderer.setGuiRenderer(GuiRenderer(self.gui, self))

        # Initialize
        self.init()

        # Set up physics
        self.physics = PhysicsEngine(self)

    def load(self):
        """ Load resources """
        # Load sheets
        environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")
        otherSheet = Spritesheet("1bit_sheet_transparent.png")

        # Load images from sheets into dicts
        self.tiles = loadTiles(environmentSheet)
        self.chars = loadCharacters(charactersSheet)
        self.objects = loadObjects(environmentSheet)
        self.other = loadOther(otherSheet)
        self.all_images = {**self.tiles, **self.chars, **self.objects, **self.other}
        self.sounds = loadSounds()

    def init(self):
        """ Initialize gamestate """
        # Set level and build it
        self.level = Town("town_tile.txt", "town_obj.txt", self)
        self.level.buildLevel()

        # Diagnostics
        print(self.clock.tick_busy_loop(FPS) / 1000)
        print(self.level.scene.objects)

        # Set camera
        self.camera = Camera(WIDTH, HEIGHT)
        self.renderer.setCamera(self.camera)

        # Set player
        for o in self.level.scene.objects:
            if o.name == "player":
                self.player = o

    def update(self):
        """ Update logic """
        self.events = pg.event.get()
        for e in self.events:
            if e.type == pg.QUIT:
                display.quit()

        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        for o in self.level.scene.objects:
            o.update()

        for o in self.gui.components:
            o.update()

        # self.camera.update(self.player)

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
        self.camera.update(self.player)
        self.draw()


g = Game()

done = False
while not done:
    g.run()
