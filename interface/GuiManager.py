from components.GuiComponents import *
from config.Settings import *


class Gui:
    components = []

    def __init__(self, game):
        self.game = game
        pg.font.init()
        self.gameFont = pg.font.SysFont("monospace", 15)

    def setFont(self, font, size):
        fontPath = RESOURCES + "fonts\\" + font
        self.gameFont = pg.font.Font(fontPath, size)
        for c in self.components:
            c.resetFont()

    def addTextBox(self, position, text):
        self.components.append(TextBox(self, {"text": text, "position": position}))

    def addButton(self, position, text):
        self.components.append(Button(self, {"text": text, "position": position}))

    def getElement(self, name=None, id=None):
        if name:
            for c in self.components:
                if c.name == name:
                    return c
        elif id:
            for c in self.components:
                print(c.id, id)
                if c.id == id:
                    return c


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
        gui = Gui(self.game)

        for k, o in interfaceList.items():
            c = self.addComponent(gui, k, o)
            print(c)
            gui.components.append(c)

        return gui

    def addComponent(self, gui, k, o):
        args = o["args"]
        args["name"] = o["name"]
        args["id"] = k
        component = eval(o["type"])(gui, args, self.game.gameDisplay.screen)
        return component

