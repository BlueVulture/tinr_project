import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, name, image, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.components = []
        self.game = game
        self.scene = self.game.level.scene

    def update(self):
        for c in self.components:
            c.action()

    def getPosition(self):
        return self.x, self.y

    def addComponent(self, component, args):
        self.components.append(component(self, args))
