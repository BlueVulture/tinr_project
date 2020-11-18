from pygame import *
import pygame as pg
from reloadr import autoreload
import numpy as np
from random import random
import configparser
import math


x, y = 50, 200

@autoreload
def load():
    assets["grass_tile"] = image.load("assets/tiles/medievalTile_57.png")
    assets["unit_1"] = image.load("assets/characters/medievalUnit_01.png")
    assets["structure_1"] = image.load("assets/structures/medievalStructure_18.png")


@autoreload
def init():
    pass


@autoreload
def update():
    for e in event.get():
        if e.type == pg.QUIT:
            display.quit()

        # handle MOUSEBUTTONUP
        if e.type == pg.MOUSEBUTTONUP:
            pos = mouse.get_pos()
            print(pos)
            unit_size = assets["unit_1"].get_size()           
            global x, y 
            x, y = (pos[0]-unit_size[0]/2, pos[1]-unit_size[1]/2)
            # screen.blit(assets["unit_1"], (pos[0]-unit_size[0]/2, pos[1]-unit_size[1]/2))
        

@autoreload
def draw():
    draw_grid()
    screen.blit(assets["unit_1"], (x, y))
    screen.blit(assets["structure_1"], (128, 256))
    
    display.update()


@autoreload
def draw_grid():
    for x in range(0, 1024, 128):
        for y in range(0, 1024, 128):
            screen.blit(assets["grass_tile"], (x, y))

    for x, y in zip(range(0, 1024, 128), range(0, 1024, 128)):
        pg.draw.line(screen, color.THECOLORS["black"], (x, 0), (x, 1024))
        pg.draw.line(screen, color.THECOLORS["black"], (0, y), (1024, y))

    
    # for y in range(0, 1024, 128):
    #     pg.draw.line(screen, color.THECOLORS["black"], (0, y), (1024, y))


assets = {};
data = {};

clock = time.Clock()

WINSIZE = [1024, 512]
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
