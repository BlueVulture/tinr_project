from components.Components import *
from config.Settings import *
from physics.Math import *
import pygame as pg


class GuiComponent:
    def __init__(self, parent, args, screen):
        self.parent = parent
        self.args = args
        self.screen = screen
        self.name = self.checkArgs("name")
        self.id = self.checkArgs("id")
        self.gameFont = self.parent.gameFont
        self.customFont = False

    def init(self):
        pass

    def render(self):
        pass

    def update(self):
        pass

    def resetFont(self):
        if not self.customFont:
            self.gameFont = self.parent.gameFont

    def checkArgs(self, key, alternative=None):
        if key in self.args.keys():
            return self.args[key]
        elif alternative:
            return alternative
        else:
            return None


class TextBox(GuiComponent):
    def __init__(self, parent, args, screen):
        super().__init__(parent, args, screen)
        self.text = self.checkArgs("text")
        self.position = self.checkArgs("position")
        self.centered = self.checkArgs("centered")
        self.font = self.checkArgs("font")
        self.fontSize = self.checkArgs("fontSize")
        self.textColor = self.checkArgs("textColor", BLACK)
        print(self.checkArgs("name"))

        if self.font and self.fontSize:
            fontPath = RESOURCES + "fonts\\" + self.font
            self.gameFont = pg.font.Font(fontPath, self.fontSize)
            self.customFont = True
        else:
            self.gameFont = self.parent.gameFont

        print(self.font, self.fontSize, self.textColor, self.gameFont, self.customFont)

    def render(self, debug=False):
        label = self.gameFont.render(self.text, True, self.textColor)
        if self.centered:
            position = (self.position[0]-label.get_rect().width/2, self.position[1])
        else:
            position = self.position
        self.screen.blit(label, position)

    def setText(self, text):
        self.text = str(text)


class ImageBox(GuiComponent):
    def __init__(self, parent, args, screen):
        super().__init__(parent, args, screen)
        image = self.checkArgs("image")
        self.image = self.parent.game.named_images[image]
        self.position = self.checkArgs("position")
        self.centered = self.checkArgs("centered")
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def render(self, debug=False):
        self.screen.blit(self.image, self.position)
        if debug:
            pg.draw.rect(self.screen, RED, self.rect, 2)


class Button(GuiComponent):
    def __init__(self, parent, args, screen):
        super().__init__(parent, args, screen)
        self.backgroundColor = self.checkArgs("backgroundColor")
        self.image = self.checkArgs("image")
        self.text = self.checkArgs("text")
        self.switch = self.checkArgs("switch")
        self.position = self.checkArgs("position")
        self.size = self.checkArgs("size")
        self.centered = self.checkArgs("centered")
        self.verticalAlign = self.checkArgs("vertical")
        self.action = self.checkArgs("action")
        self.active = self.checkArgs("active", True)
        self.actionArgs = self.checkArgs("actionArgs", {})
        self.centeredText = self.checkArgs("centeredText")
        self.gameSettings = self.parent.game.settings
        if self.switch:
            self.textAdd = "ON" if self.gameSettings[self.actionArgs["setting"]] else "OFF"
        else:
            self.textAdd = ""

        self.cover = pg.Surface(self.size, pg.SRCALPHA)
        self.cover.set_alpha(128)
        self.cover.fill(DARKGREY)

        if self.backgroundColor:
            self.background = pg.Surface(self.size)
            self.background.fill(self.backgroundColor)
        else:
            self.background = None

        if self.centered:
            self.position = (self.position[0]-self.size[0]/2, self.position[1])

        if self.image:
            self.image = pg.transform.scale(self.image, self.size)

    def render(self, debug=False):
        if self.background:
            self.screen.blit(self.background, self.position)

        if self.image:
            self.screen.blit(self.image, self.position)

        if self.text:
            text = self.text + self.textAdd

            label = self.parent.gameFont.render(text, True, BLACK)
            r = label.get_rect()

            if self.centered or self.centeredText:
                xPosition = self.position[0]+(self.size[0] / 2) - (r.width / 2)
            else:
                xPosition = self.position[0]

            lPosition = (xPosition, self.position[1]+self.size[1]/2 - r.height / 2)
            self.screen.blit(label, lPosition)

        if debug and DEBUG:
            pg.draw.rect(self.screen, BLUE, (self.position[0], self.position[1], self.size[0], self.size[1]), 2)
            pass

        if not self.active:
            self.screen.blit(self.cover, self.position)

    def update(self):
        if self.active:
            for e in self.parent.game.events:
                if e.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if positionWithin(pos, (self.position[0], self.position[1], self.size[0], self.size[1])):
                        print("Clicked on button " + self.id)
                        self.resolveBtnClick()

    def resolveBtnClick(self):
        action = self.action
        if action:
            m = self
            fn = getattr(m, action, self.defaultAction())
            if fn:
                fn()

    def new(self):
        self.parent.game.setLevel("Town", "town_map.json")

    def pause(self):
        game = self.parent.game
        if game.paused:
            game.unpause()
        else:
            game.pause()

    def quit(self):
        self.parent.game.quit()

    def resume(self):
        self.parent.game.unpause()

    def settings(self):
        self.parent.game.menuManager.setMenu("SettingsMenu")

    def back(self):
        self.parent.game.menuManager.setMenu("back")

    def continueGame(self):
        self.parent.game.setLevel("Town", "town_map.json")

    def changeSetting(self):
        setting = self.actionArgs["setting"]
        changeSetting(self.parent.game, setting, switch=True)

        if self.switch:
            self.textAdd = "ON" if self.gameSettings[setting] else "OFF"

    def save(self):
        saveSettings(self.parent.game)
        self.parent.game.menuManager.setMenu("back")

    def reset(self):
        self.parent.game.reset()

    def defaultAction(self):
        pass
