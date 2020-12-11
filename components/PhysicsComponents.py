from components.Components import *


class Movable(Component):
    """ Physics component for moving object """

    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.vector = args["vector"]

    def update(self):
        self.parent.x += self.vector.x * self.parent.game.dt
        self.parent.y += self.vector.y * self.parent.game.dt


class Rotatable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Rigidbody(Component):
    """ Physics component for collisions """
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.mass = args["mass"]

    def resolveCollision(self, collider):
        if self.mass == 0:
            return
        else:
            pass


class BoxCollider(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.rect = parent.rect

    def action(self):
        print(self.rect)


class TransformComponent(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.parent.rect.x = self.parent.x
        self.parent.rect.y = self.parent.y
