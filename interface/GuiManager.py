import pygame as pg
from interface.GuiComponents import *
from config.Settings import *


class GuiScene:
    components = []

    def __init__(self, game):
        self.game = game
        pg.font.init()
        self.gameFont = pg.font.SysFont("monospace", 15)

    def setFont(self, font, size):
        fontPath = RESOURCES + "fonts\\" + font
        self.gameFont = pg.font.Font(fontPath, size)

    def addTextBox(self, position, text):
        self.components.append(TextDisplay(self, {"text": "test", "position": (0, 0)}))


class GuiRenderer:
    def __init__(self, gui, game):
        self.game = game
        self.gui = gui

    def render(self, debug=False):
        for c in self.gui.components:
            c.render(debug=debug)


class GuiGenerator:
    def __init__(self, game):
        self.game = game

    def generate(self, interfaceList):
        gui = GuiScene(self.game)

        for o in interfaceList:
            args = o["args"]
            args["name"] = o["name"]
            args["id"] = o["id"]
            component = eval(o["type"])(gui, args, self.game.gameDisplay.screen)
            gui.components.append(component)

        return gui

