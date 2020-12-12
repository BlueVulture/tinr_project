import pygame as pg


class Circle:
    def __init__(self, position, radius):
        self.x = position[0]
        self.y = position[1]
        self.radius = radius
        self.r = self.radius
        self.position = (self.x, self.y)

    def draw(self, screen, color, thicness):
        pg.draw.circle(screen, color, (self.x, self.y), self.radius, thicness)
