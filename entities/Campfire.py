from entities.Entity import Entity


class Campfire(Entity):
    def __init__(self, x, y, name, image, game):
        Entity.__init__(self, x, y, name, image, game)

    def update(self):
        pass

    def getPosition(self):
        return self.x, self.y

    def switchState(self):

        if self.image == self.game.objects["campfire_on"]:
            self.image = self.game.objects["campfire_off"]
            print("off!")
        else:
            self.image = self.game.objects["campfire_on"]
            print("on!")
