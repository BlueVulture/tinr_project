class Component:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args

    def init(self):
        pass

    def action(self):
        pass

    def update(self):
        pass

    def checkArgs(self, key):
        if key in self.args.keys():
            return self.args[key]
        else:
            return None


class Consumable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Interactable(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)


class Animated(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.images = self.checkArgs("images")
        self.time = self.checkArgs("time")



