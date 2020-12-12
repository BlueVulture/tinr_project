from components.Components import *
from physics.CustomShapes import *


class Movable(Component):
    """ Physics component for moving object """

    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.vector = self.checkArgs("vector")

    def physicsUpdate(self):
        self.parent.x += self.vector.x * self.parent.game.dt
        self.parent.y += self.vector.y * self.parent.game.dt


class Rotatable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)

    def physicsUpdate(self):
        pass


class Rigidbody(Component):
    """ Physics component for collisions """
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.mass = self.checkArgs("mass")
        self.active = self.checkArgs("active")
        self.colliders = []

    def physicsUpdate(self):
        pass


class BoxCollider(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        if "rect" in args.keys():
            self.rect = args["rect"]
        else:
            self.rect = parent.rect

        self.kinematic = self.checkArgs("kinematic")

    def physicsUpdate(self):
        pass

    def action(self):
        # print(self.rect)
        pass


class CircleCollider(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        rect = self.parent.rect
        if "circle" in args.keys():
            self.circle = Circle((rect.x+int(rect.width/2), rect.y+int(rect.height/2)), args["circle"])
        else:
            self.circle = Circle((rect.x+int(rect.width/2), rect.y+int(rect.height/2)), rect.width/2)

        self.kinematic = self.checkArgs("kinematic")

    def physicsUpdate(self):
        self.circle.x = self.parent.x + int(self.parent.rect.width/2)
        self.circle.y = self.parent.y + int(self.parent.rect.height/2)

    def detected(self, collider):
        # print("Detected")
        for k, c in self.parent.components.items():
            c.collisionDetected(collider)

    def action(self):
        # print(self.circle)
        pass


class TransformComponent(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.parent.rect.x = self.parent.x
        self.parent.rect.y = self.parent.y
