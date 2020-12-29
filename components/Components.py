import pygame as pg


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

    def collisionDetected(self, object):
        pass

    def checkArgs(self, key):
        if key in self.args.keys():
            return self.args[key]
        else:
            return None


class Consumable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Interactable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


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


# class MultiTile(Component):
#     def __init__(self, parent, args):
#         super().__init__(parent, args)
#         self.parts = self.checkArgs("parts")
#         self.size = self.checkArgs("size")
#
#     def draw(self, screen, camera):
#         o = self.parent
#         for pos, i in self.parts.items():
#             image = self.parent.game.all_images[i]
#             screen.blit(image, camera.applyPosition((o.x + pos[0] * o.rect.width, o.y + pos[1] * o.rect.height)))


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

