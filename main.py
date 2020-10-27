from pygame import *
import pygame as pg
from reloadr import autoreload
import numpy as np
from random import random
import configparser
import math


@autoreload
def load():
    assets["grass_tile"] = image.load("assets/tile/medievalTile_57.png")


@autoreload
def init():
    pass


@autoreload
def update():
    pass

    for e in event.get():
        if e.type == pg.QUIT:
            display.quit()


@autoreload
def draw():
    screen.fill(color.THECOLORS["white"])
    screen.blit(assets["grass_tile"], (0, 50))
    draw_grid()
    display.update()


@autoreload
def draw_grid():
    for x in range(0, 1024, 32):
        pg.draw.line(screen, color.THECOLORS["black"], (x, 0), (x, 1024))
    for y in range(0, 1024, 32):
        pg.draw.line(screen, color.THECOLORS["black"], (0, y), (1024, y))


assets = {};
data = {};

clock = time.Clock()

WINSIZE = [1024, 1024]
screen = display.set_mode(WINSIZE)
display.set_caption("Game")
display.set_icon(image.load("assets/meta/medievalEnvironment_03.png"))

init()
load()

clock.tick()

done = False
while not done:
    clock.tick(60)
    update()
    draw()
