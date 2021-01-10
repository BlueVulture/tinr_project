from interface.GuiManager import *
from assets.Loader import *
from assets.Spritesheet import *
from interface.MenuManager import *
from renderer.Camera import Camera
from renderer.DisplayManager import *
from renderer.Renderer import Renderer
from physics.PhysicsEngine import *
from scenes.Levels import *


class Game:
    tiles = {}
    chars = {}
    other = {}
    objects = {}
    named_images = {}
    all_images = []
    all_images_offset = []
    sounds = {}
    settings = {}

    events = None
    level = None
    camera = None
    player = None
    physics = None

    paused = False

    def __init__(self):
        pg.init()

        self.end = False
        readSettings(self)

        # Display
        self.gameDisplay = DisplayManager(WINSIZE, TITLE, ICON)

        # Create spritegroup (for pg.Sprite inheritance)
        self.all_sprites = pg.sprite.Group()

        # Set clock
        self.clock = time.Clock()
        self.clock.tick()
        self.dt = self.clock.tick_busy_loop(FPS) / 1000
        # pg.mixer.init()

        # Load all
        self.load()

        # Set up renderer
        self.renderer = Renderer(self, grid=False, debug=True)

        # Set up GUI
        self.gui = GuiGenerator(self).generate(interface)
        self.gui.setFont("pixel.ttf", 32)
        self.renderer.setGuiRenderer(GuiRenderer(self.gui, self))
        self.menuManager = MenuManager(self)
        self.drawGui = False
        self.showMenu = False
        # Initialize
        self.init()

        # Set up physics
        self.physics = PhysicsEngine(self)

        # FPS Counter
        self.fpsCounter = self.gui.getElement(name="FPS")

        # Initial update
        self.events = pg.event.get()
        self.update()

    def load(self):
        """ Load resources """
        # Load sheets
        roguelikeSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
        roguelikeChar = Spritesheet("roguelikeChar_transparent_no_margins.png")
        oneBitSheet = Spritesheet("1bit_sheet_transparent.png")
        tilesSheet = Spritesheet("roguelikeSheet_transparent_fix.png")
        charSheet = Spritesheet("roguelikeChar_transparent_fixed.png")
        objectsSheet = Spritesheet("1bit_sheet_transparent.png")

        # Load images from sheets into dicts
        self.tiles = loadTiles(roguelikeSheet)
        self.chars = loadCharacters(roguelikeChar)
        self.objects = loadObjects(roguelikeSheet)
        self.other = loadOther(oneBitSheet)
        self.named_images = {**self.tiles, **self.chars, **self.objects, **self.other}

        self.all_images_offset.append(loadSheet(tilesSheet, self.all_images, 1))
        self.all_images_offset.append(loadSheet(charSheet, self.all_images, 1))
        self.all_images_offset.append(loadSheet(objectsSheet, self.all_images))
        print(self.all_images_offset)
        self.sounds = loadSounds()

    def init(self):
        """ Initialize gamestate """
        # Set level and build it
        # self.setLevel("Town", "town_map.json")
        pg.mixer.init()
        self.setLevel("MainMenu", "main_menu.json")
        self.menuManager.setMenu("MainMenu")
        self.showMenu = True

        self.drawGui = self.level.gui

        # Diagnostics
        print(self.clock.tick_busy_loop(FPS) / 1000)
        print(self.level.scene.objects)

        # Set camera
        self.camera = Camera(WIDTH, HEIGHT)
        self.renderer.setCamera(self.camera)

        # Set player
        self.setPlayer()

    def setPlayer(self):
        for o in self.level.scene.characters:
            if o.name == "player" or o.name == "cameraPoint":
                self.player = o
                break

    def setLevel(self, level, tilemap):
        self.level = eval(level)(tilemap, self, scene=Scene())
        self.level.buildLevel()
        self.drawGui = self.level.gui
        self.showMenu = False
        self.setPlayer()
        if self.physics:
            self.physics.setScene()
        # print(id(self.level.scene))

    def update(self):
        """ Update logic """
        self.dt = self.clock.tick_busy_loop(FPS) / 1000

        for o in self.level.scene.updatable:
            o.update()

        for o in self.gui.components:
            o.update()

        self.fpsCounter.setText(str(int(self.clock.get_fps())))
        # self.camera.update(self.player)

    def eventsUpdate(self):
        self.events = pg.event.get()
        for e in self.events:
            if e.type == pg.QUIT:
                self.quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    if self.paused:
                        self.unpause()
                    else:
                        self.pause()

    def physicsUpdate(self):
        """ Update physics """
        self.physics.physicsUpdate()

    def draw(self):
        """ Call to renderer """
        self.renderer.render()

    def reset(self):
        pg.mixer.quit()
        self.unpause()
        self.init()

    def gameOver(self):
        print("Game over")
        self.paused = True
        self.menuManager.setMenu("GameOver")
        self.showMenu = True

    def pause(self):
        """ Pause the game """
        self.paused = True
        self.menuManager.setMenu("PauseMenu")
        self.showMenu = True

    def unpause(self):
        """ Unpause the game """
        self.paused = False
        self.menuManager.setMenu(None)
        self.showMenu = False

    def quit(self):
        self.end = True

    def run(self):
        """ Gameloop """
        self.clock.tick(FPS)
        self.eventsUpdate()
        if not self.paused:
            self.update()
            self.physicsUpdate()
            self.camera.update(self.player)

        if self.showMenu:
            self.menuManager.update()
        self.draw()
        if self.end:
            global done
            done = True
            pg.display.quit()


g = Game()

done = False
while not done:
    g.run()
