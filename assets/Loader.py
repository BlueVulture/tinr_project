from data.ImageList import *
from data.SoundList import *


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


def loadOther(sheet):
    assets = {}
    for image, position in otherImages.items():
        if type(position) is tuple:
            assets[image] = sheet.imageAt((TM_COL * position[0], TM_ROW * position[1], TM_COL, TM_ROW))

    return assets


def loadSounds():
    assets = {}
    for key, sound in sounds.items():
        assets[key] = pg.mixer.Sound(SOUNDS + sound)

    return assets


def loadMusic():
    assets = {}
    for key, music in musics.items():
        assets[key] = pg.mixer.Sound(MUSIC + music)

    return assets


def loadSheet(sheet, assets, offset=0):
    tilesize = sheet.tilesize
    count = 0
    for y in range(0, sheet.height, tilesize+offset):
        for x in range(0, sheet.width, tilesize+offset):
            assets.append(sheet.imageAt((x, y, TM_COL, TM_ROW)))
            count += 1

    return count



