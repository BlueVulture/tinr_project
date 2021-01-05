from data.EntitiesList import *
from components.PhysicsComponents import *
from entities.Tile import Tile
from entities.Entity import *
from entities.Player import *
from components.Components import *
from components.AIComponents import *
from components.PhysicsComponents import *
from components.GuiComponents import *


class Generator:
    def __init__(self, game, debug=False):
        self.game = game
        self.debug = debug
        self.count = 0

    def generate(self, entity, position=None, oArgs=None, rectangle=None, gid=None, n=None, type=None):
        if self.debug and DEBUG:
            # print(entity)
            pass

        if type is "tile":
            obj = oArgs["obj"]
            entityID = self.count
            self.count += 1
            return Tile(position, "tile", self.game.all_images[obj], self.game, entityID)
        elif entity not in entities.keys():
            return None

        e = entities[entity]
        if position is None:
            if "position" in e.keys():
                position = e[position]
            else:
                position = DEFAULT_POSITION

        if "scale" in e.keys():
            scale = e["scale"]
        else:
            scale = (1, 1)

        entityClass = eval(e["class"])
        image = None

        if e["image"]:
            image = self.game.named_images[e["image"]]
        elif gid:
            image = self.game.all_images[gid-1]

        if e["name"]:
            name = e["name"]
        else:
            name = n

        entityID = self.count
        self.count += 1

        generated = entityClass(position, name, image, self.game, entityID, scale=scale, rect=rectangle)

        for c, args in e["components"].items():
            component = eval(c)
            generated.addComponent(component, args)

        for t in e["tags"]:
            generated.addTag(t)

        generated.init()

        if self.debug and DEBUG:
            print(entities[entity])
            print(generated.rect)

        return generated
