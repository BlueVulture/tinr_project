import pygame as pg

from config.Settings import *
from config.Controls import *


class Component:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args

    def init(self):
        pass

    def action(self):
        pass

    def update(self):
        pass

    def interact(self):
        pass

    def collisionDetected(self, object, colType=None):
        pass

    def checkArgs(self, key, alternative=None):
        if key in self.args.keys():
            return self.args[key]
        elif alternative:
            return alternative
        else:
            return None


class Consumable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)

    def collisionDetected(self, object, colType=None):
        # print(object.name)
        if object.name == "player" and colType is "box":
            self.parent.game.level.scene.removeEntity(self.parent, self.parent.id)


class Interactable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.fontSize = self.checkArgs("fontSize", 25)
        self.font = self.checkArgs("font", "monospace")
        self.gameFont = pg.font.SysFont(self.font, self.fontSize)
        self.text = self.checkArgs("text", "text")
        self.label = self.gameFont.render(self.text, True, BLACK)

    def collisionDetected(self, object, colType=None):
        if object.name == "player" and colType is "circle":
            self.parent.game.renderer.addToQueue(self.label, (self.parent.x, self.parent.y-(self.fontSize+5)))
            for e in self.parent.game.events:
                if e == INTERACT_KEY:
                    for k, c in self.parent.components.items():
                        c.interact()


class Animated(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.images = self.checkArgs("images")
        self.time = self.checkArgs("time")
        self.deltaTime = self.time/len(self.images)
        self.currentFrame = 0
        self.currentTime = 0
        # print(self.deltaTime)

    def update(self):
        self.animate()

    def animate(self):
        # print(str(self.currentTime) + " " + str(self.currentFrame))
        if self.currentTime >= (self.currentFrame+1)*self.deltaTime:
            self.currentFrame += 1
            self.parent.changeImage(self.images[self.currentFrame])
            self.currentTime += self.parent.game.dt
        else:
            self.currentTime += self.parent.game.dt

        if self.currentTime > self.time:
            self.currentFrame = 0
            self.currentTime = 0
            self.parent.changeImage(self.images[self.currentFrame])


class SoundEffect(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        file = self.checkArgs("sound")
        if file is not None:
            self.sound = self.parent.game.sounds[file]

        self.play = self.checkArgs("play")
        self.time = self.checkArgs("time")
        if self.time == "length":
            self.time = pg.mixer.Sound.get_length(self.sound)

        self.currentTime = 0
        self.dt = self.parent.game.dt
        self.volume = self.checkArgs("volume")
        if self.volume:
            pg.mixer.Sound.set_volume(self.sound, self.volume)

    def update(self):
        if self.play:
            if self.currentTime == 0:
                print("Playing sound " + self.parent.name)
                pg.mixer.Sound.play(self.sound)
                self.currentTime += self.dt
            elif self.currentTime > self.time:
                self.currentTime = 0
            else:
                self.currentTime += self.dt

    def playSound(self):
        pg.mixer.Sound.play(self.sound)

    def playSoundOnRepeat(self):
        if self.currentTime == 0:
            # print("sound")
            pg.mixer.Sound.play(self.sound)
            self.currentTime += self.dt
        elif self.currentTime > self.time:
            self.currentTime = 0
        else:
            self.currentTime += self.dt

class MusicComponent(Component):
    pass

