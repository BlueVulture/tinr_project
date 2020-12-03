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
    def __init__(self, parent, args):
        super().__init__(parent, args)

