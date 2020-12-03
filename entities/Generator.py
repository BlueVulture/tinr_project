from config.EntitiesList import *
from config.Settings import *
from entities.Entity import *
from entities.Player import *
from components.PhysicsComponents import *
# from entities import *


class Generator:
    def __init__(self, game):
        self.game = game

    def generate(self, entity, position=None, oArgs=None):
        print(entity)
        e = entities[entity]
        if position is None:
            if "position" in e.keys():
                position = e[position]
            else:
                position = DEFAULT_POSITION

        entityClass = eval(e["class"])

        generated = entityClass(position, e["name"], self.game.all_images[e["image"]], self.game)
        for c, args in e["components"].items():
            component = eval(c)
            generated.addComponent(component, args)

        print(entities[entity])
        return generated
