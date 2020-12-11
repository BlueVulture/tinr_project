class Component:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args

    def action(self):
        pass

    def update(self):
        pass


class Consumable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Interactable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)

