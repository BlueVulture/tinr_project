from random import *
from config.Settings import *
from config.EntitiesList import *
from entities.Generator import Generator
from entities.Player import Player
from entities.Tile import *
from scenes.Level import *
from scenes.Scene import *
import copy
import json


class Level:
    scene = Scene()

    def __init__(self, tilemap, game, scene=None):
        self.tilemap = TILEMAPS + tilemap
        # self.objectmap = TILEMAPS + objectmap
        self.game = game
        self.generator = Generator(self.game, debug=True)
        if scene:
            self.scene = scene

    def buildLevel(self):
        print(self.scene)
        self.readTilemap()

    def readTilemap(self):
        with open(self.tilemap, "rt") as f:
            data = json.load(f)

        height = data["height"]
        width = data["width"]

        for z, layer in enumerate(data["layers"]):
            if layer["type"] == "tilelayer" and layer["visible"]:
                t = layer["properties"][0]["value"]
                # print(t)

                for pos, obj in enumerate(layer["data"]):
                    obj -= 1
                    if obj >= 0:
                        row = int(pos / width)
                        column = int(pos % width)

                        # tile = Tile((column * TILESIZE, row * TILESIZE), "tile", self.game.all_images[obj], self.game)
                        tile = self.generator.generate(None, position=(column * TILESIZE, row * TILESIZE), oArgs={"obj": obj}, type="tile")
                        self.scene.addEntity(tile, t, z, tile.id)

            elif layer["type"] == "objectgroup":
                for obj in layer["objects"]:
                    x = (obj["x"]/IMAGE_TILESIZE)*TILESIZE
                    y = (obj["y"]/IMAGE_TILESIZE)*TILESIZE
                    name = obj["name"]
                    entityType = obj["type"]
                    t = layer["properties"][0]["value"]
                    w = (obj["width"]/IMAGE_TILESIZE)*TILESIZE
                    h = (obj["height"] / IMAGE_TILESIZE) * TILESIZE

                    if "gid" in obj.keys():
                        img = obj["gid"]
                    else:
                        img = None

                    # print(obj)
                    entity = self.generator.generate(entityType, (x, y), rectangle=(x, y, w, h), gid=img, n=name)
                    if entity:
                        self.scene.addEntity(entity, t, z-1, entity.id, updatable=True)
