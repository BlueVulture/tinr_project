from renderer.DisplayManager import DisplayManager
from pygame import *
import pygame as pg
from reloadr import autoreload
import numpy as np
from random import random
import configparser
import math


@autoreload
def load():
    pass


@autoreload
def init():
    pass


@autoreload
def update():
    print("Yeah!")   


@autoreload
def draw():   
    display.update()


assets = {};
data = {};

clock = time.Clock()

WINSIZE = [1024, 512]
screen = DisplayManager(WINSIZE, "Game", "medievalEnvironment_03.png")

init()
load()

clock.tick()

done = False
while not done:
    clock.tick(60)
    pg.event.get()
    update()
    draw()
