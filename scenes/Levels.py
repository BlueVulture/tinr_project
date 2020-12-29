from scenes.Level import *


class MainMenu(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)


class Town(Level):
    def __init__(self, tilemap, game, scene=None):
        Level.__init__(self, tilemap, game, scene)
        self.gui = True
