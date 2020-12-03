from components.Components import *


class Movable(Component):
    def __init__(self, parent, args, vector):
        super().__init__(parent, args)
        self.vector = vector

    def update(self):
        self.parent.x += self.vector.x
        self.parent.y += self.vector.y


class Rotatable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Rigidbody(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
