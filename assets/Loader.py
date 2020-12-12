from pygame import *

from config.Settings import *
from config.ImageList import *

def loadTiles(sheet):
    assets = {}
    for image, position in tileImages.items():
        if type(position) is tuple:
            assets[image] = sheet.imageAt((TM_COL * position[0], TM_ROW * position[1], TM_COL, TM_ROW))

    return assets


def loadCharacters(sheet):
    assets = {}
    for image, position in characterImages.items():
        if type(position) is tuple:
            assets[image] = sheet.imageAt((TM_COL * position[0], TM_ROW * position[1], TM_COL, TM_ROW))

    return assets


def loadObjects(sheet):
    assets = {}
    for image, position in objectImages.items():
        if type(position) is tuple:
            assets[image] = sheet.imageAt((TM_COL * position[0], TM_ROW * position[1], TM_COL, TM_ROW))

    return assets

