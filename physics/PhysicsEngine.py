class PhysicsEngine:
    def __init__(self, game):
        self.game = game
        self.scene = self.game.level.scene
        pass

    def physicsUpdate(self):
        for o in self.scene.objects:
            if "Movable" in o.components.keys():
                o.components["Movable"].update()

            if "Rotatable" in o.components.keys():
                pass

            if "Rigidbody" in o.components.keys():
                o.components["Rigidbody"].update()


