from scenes.Town import Town
from scenes.Scene import Scene
from assets.Loader import Loader
from renderer.DisplayManager import *
from assets.Spritesheet import *
from config.Settings import *
from entities.Player import *
from pygame import *
import pygame as pg
from reloadr import autoreload

tiles = {};
chars = {};
data = {};

@autoreload
def load():
    environmentSheet = Spritesheet("roguelikeSheet_transparent_no_margins.png")
    charactersSheet = Spritesheet("roguelikeChar_transparent_no_margins.png")

    tiles = Loader.loadTiles(environmentSheet)
    chars = Loader.loadCharacters(charactersSheet)


@autoreload
def init():
    load()
    global scene
    scene = Town("town_tile.txt", "town_obj.txt", Scene, tiles, chars)
    scene.readTiles()

@autoreload
def update():
    pass


@autoreload
def draw(): 
    for o in scene.scene.tiles:
        D.screen.blit(tiles["grass_tile"], (10, 10))
    D.update()


clock = time.Clock()

WINSIZE = [1024, 512]
D = DisplayManager(WINSIZE, "Game", "medievalEnvironment_03.png")

init()
load()

clock.tick()

done = False
while not done:
    clock.tick(60)
    pg.event.get()
    update()
    draw()
