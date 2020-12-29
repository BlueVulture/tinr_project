from components.Components import *
from config.Settings import *
from physics.Math import *


class GuiComponent:
    def __init__(self, parent, args, screen):
        self.parent = parent
        self.args = args
        self.screen = screen
        self.name = self.checkArgs("name")
        self.id = self.checkArgs("id")

    def init(self):
        pass

    def render(self):
        pass

    def update(self):
        pass

    def checkArgs(self, key):
        if key in self.args.keys():
            return self.args[key]
        else:
            return None


class TextDisplay(GuiComponent):
    def __init__(self, parent, args, screen):
        super().__init__(parent, args, screen)
        self.text = self.checkArgs("text")
        self.position = self.checkArgs("position")
        self.centered = self.checkArgs("centered")

    def render(self, debug=False):
        label = self.parent.gameFont.render(self.text, True, BLACK)
        if self.centered:
            position = (self.position[0]-label.get_rect().width/2, self.position[1])
        else:
            position = self.position
        self.screen.blit(label, position)

    def setText(self, text):
        self.text = str(text)


class ImageDisplay(GuiComponent):
    def __init__(self, parent, args, screen):
        super().__init__(parent, args, screen)
        image = self.checkArgs("image")
        self.image = self.parent.game.named_images[image]
        self.position = self.checkArgs("position")
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
        self.background = self.checkArgs("background")
        self.color = self.checkArgs("color")
        image = self.checkArgs("image")
        if image:
            self.image = self.parent.game.named_images[image]
        self.text = self.checkArgs("text")
        self.position = self.checkArgs("position")
        self.size = self.checkArgs("size")

    def render(self, debug=False):
        # print(self.args)
        if self.background:
            pg.draw.rect(self.screen, BLUE, (self.position[0], self.position[1], self.size[0], self.size[1]), 2)
        else:
            pg.draw.rect(self.screen, RED, (self.position[0], self.position[1], self.size[0], self.size[1]), 2)

        if self.text:
            label = self.parent.gameFont.render(self.text, True, BLACK)
            self.screen.blit(label, self.position)

        if debug:
            # pg.draw.rect(self.screen, RED, self.rect, 2)
            pass

    def update(self):
        for e in self.parent.game.events:
            if e.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if positionWithin(pos, (self.position[0], self.position[1], self.size[0], self.size[1])):
                    print("Clicked on button!")
                else:
                    print("Click!")