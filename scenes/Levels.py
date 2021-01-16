from data.LevelList import levels
from scenes.Level import *


class MainMenu(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = False
        for c, args in levels["MainMenu"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()


class Town(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
        for c, args in levels["Town"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()


class House(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
        for c, args in levels["House"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()


class Cave(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
        self.music = "cave"
        for c, args in levels["Cave"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()


class Castle(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
        self.music = "castle"
        for c, args in levels["Castle"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()
