from data.Interface import *
from components.GuiComponents import *


class MenuManager:
    menus = {}
    currentMenu = None
    prevMenu = None

    def __init__(self, game):
        self.game = game
        self.generateMenus()
        Menu(self.game).components.append(None)
        print(self.menus)

    def update(self):
        for c in self.currentMenu.components:
            c.update()

    def setMenu(self, menu):
        print(menu)
        if menu is "back" and self.prevMenu:
            print("Wrong")
            self.currentMenu = self.prevMenu
            self.prevMenu = None
        elif menu:
            print("Right")
            self.prevMenu = self.currentMenu
            self.currentMenu = self.menus[menu]
        else:
            print("Why")
            self.currentMenu = None

    def render(self, debug):
        if self.currentMenu:
            for c in self.currentMenu.components:
                c.render(debug=debug)

    def generateMenus(self):
        for k, m in menuInterfaces.items():
            menu = Menu(self.game)
            font, fontSize = None, None
            if "font" in m.keys():
                font = m["font"]

            if "fontSize" in m.keys():
                fontSize = m["fontSize"]

            if font and fontSize:
                menu.setFont(font, fontSize)

            components = []
            for i, c in m["components"].items():
                args = c["args"]
                args["name"] = c["name"]
                args["id"] = i
                component = eval(c["type"])(menu, args, self.game.gameDisplay.screen)
                components.append(component)

            menu.components = components
            menu.name = k
            self.menus[k] = menu


class Menu:
    components = []

    def __init__(self, game):
        self.game = game
        pg.font.init()
        self.gameFont = pg.font.SysFont("monospace", 15)
        self.name = ""

    def setFont(self, font, size):
        fontPath = RESOURCES + "fonts\\" + font
        self.gameFont = pg.font.Font(fontPath, size)
        for c in self.components:
            c.resetFont()

    def getElement(self, name=None, id=None):
        if name:
            for c in self.components:
                if c.name == name:
                    return c
        elif id:
            for c in self.components:
                if c.id == id:
                    return c
