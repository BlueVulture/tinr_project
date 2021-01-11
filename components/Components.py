import pygame as pg
from config.Settings import *
from physics.Math import euclidean, clamp


class Component:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args
        self.disabled = False
        self.disabledUpdateDone = False

    def init(self):
        pass

    def action(self):
        pass

    def update(self):
        pass

    def physicsUpdate(self):
        pass

    def interact(self):
        pass

    def draw(self):
        pass

    def disabledUpdate(self):
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
        if object.name == "player" and colType == "box":
            self.parent.game.level.scene.removeEntity(self.parent, self.parent.id)


class Interactable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.fontSize = self.checkArgs("fontSize", 50)
        self.font = self.checkArgs("font", GAME_FONT)
        self.gameFont = pg.font.SysFont(self.font, self.fontSize)
        self.text = self.checkArgs("text", "text")
        self.label = self.gameFont.render(self.text, True, WHITE)
        self.disabled = False

    def collisionDetected(self, object, colType=None):
        if not self.disabled:
            if object.name == "player" and colType == "circle":
                x = self.parent.x + self.parent.rect.width/2 - self.label.get_rect().width/2
                self.parent.game.renderer.addToQueue(self.label, (x, self.parent.y - self.fontSize))
                for e in self.parent.game.events:
                    if e.type == pg.KEYDOWN:
                        if e.key == INTERACT_KEY:
                            print("Interact")
                            for k, c in self.parent.components.items():
                                c.interact()

    # def disable(self):
    #     self.disabled = True


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
        self.maxVolume = self.checkArgs("volume")
        if self.maxVolume:
            pg.mixer.Sound.set_volume(self.sound, self.maxVolume)
        self.channel = None
        self.player = self.parent.game.player
        self.distance = self.checkArgs("distance", 300)

    def disabledUpdate(self):
        if self.channel:
            self.channel.stop()
        self.channel = None
        self.currentTime = 0

    def update(self):
        if self.parent.game.settings["sound"]:
            if self.player.name != "player":
                self.player = self.parent.game.player

            d = euclidean(self.parent.getPosition(), self.player.getPosition())
            v = clamp(((self.distance - d)/self.distance), 0, 1)
            self.setVolume(v*self.maxVolume)

            if self.play:
                if self.currentTime == 0:
                    print("Playing sound " + self.parent.name)
                    self.playSound()
                    self.currentTime += self.dt
                elif self.currentTime > self.time:
                    self.currentTime = 0
                else:
                    self.currentTime += self.dt

    def playSound(self):
        self.channel = pg.mixer.Sound.play(self.sound)

    def playSoundOnRepeat(self):
        if self.parent.game.settings["sound"]:
            if self.currentTime == 0:
                self.channel = pg.mixer.Sound.play(self.sound)
                self.currentTime += self.dt
            elif self.currentTime > self.time:
                self.currentTime = 0
            else:
                self.currentTime += self.dt

    def setVolume(self, v):
        if self.channel:
            self.channel.set_volume(v)


class MusicPlayer(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        file = self.checkArgs("sound")
        if file is not None:
            self.sound = self.parent.game.music[file]

        self.volume = self.checkArgs("volume")
        if self.volume:
            pg.mixer.Sound.set_volume(self.sound, self.volume)

        self.channel = None
        self.time = pg.mixer.Sound.get_length(self.sound)
        self.currentTime = 0
        self.dt = self.parent.game.dt

    def update(self):
        if self.parent.game.settings["music"]:
            if self.channel:
                if self.channel.get_volume() <= 0:
                    self.setVolume(self.volume)
            if self.currentTime == 0:
                self.channel = pg.mixer.Sound.play(self.sound)
                self.currentTime += self.dt
            elif self.currentTime >= self.time:
                self.currentTime = 0
            else:
                self.currentTime += self.dt
        else:
            self.setVolume(0)

    def playSound(self):
        self.channel = pg.mixer.Sound.play(self.sound)

    def stop(self):
        if self.channel:
            self.channel.stop()

    def setVolume(self, v):
        if self.channel:
            self.channel.set_volume(v)


class SceneChange(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.target = self.checkArgs("scene")
        self.tilemap = self.checkArgs("map")

    def collisionDetected(self, object, colType=None):
        if object.name == "player" and colType == "box":
            self.parent.game.setLevel(self.target, self.tilemap)


class SwitchState(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.state = self.checkArgs("state")
        self.offImage = self.checkArgs("offImage")
        self.onImage = self.checkArgs("onImage")
        self.components = self.checkArgs("components")

    def interact(self):
        if self.state:
            self.turnOff()
        else:
            self.turnOn()

    def turnOn(self):
        self.parent.changeImage(self.onImage)
        for c in self.components:
            self.parent.components[c].disabled = False
        self.state = True

    def turnOff(self):
        self.parent.changeImage(self.offImage)
        for c in self.components:
            self.parent.components[c].disabled = True
        self.state = False

