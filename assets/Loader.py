from pygame import *
import pygame as pg
from config.Settings import *

class Loader:

    def loadTiles(sheet):
        assets = {}
        assets["grass_tile_1"] = sheet.imageAt((TM_COL*5, 0, TM_COL, TM_ROW))
        assets["grass_tile_2"] = sheet.imageAt((TM_COL*5, TM_ROW*1, TM_COL, TM_ROW))
        assets["dirt_tile"] = sheet.imageAt((TM_COL*6, 0, TM_COL, TM_ROW))
        assets["stone_tile"] = sheet.imageAt((TM_COL*7, 0, TM_COL, TM_ROW))

        return assets

    def loadCharacters(sheet):
        assets = {}
        assets["npc"] = sheet.imageAt((0, 6*TM_ROW, TM_COL, TM_ROW))
        assets ["player"] = image.load(RESOURCES + "characters/medievalUnit_01.png")

        return assets

    def loadObjects(sheet):
        assets = {}
        assets ["campfire"] = sheet.imageAt((TM_COL*14, TM_ROW*8, TM_COL, TM_ROW), scale=3)

        return assets