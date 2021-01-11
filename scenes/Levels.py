from data.LevelList import levels
from scenes.Level import *


class MainMenu(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        for c, args in levels["MainMenu"]["components"].items():
            component = eval(c)
            self.addComponent(component, args)

    def stop(self):
        self.components["MusicPlayer"].stop()

class Town(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True


class House(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True


class Cave(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True


class Castle(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
