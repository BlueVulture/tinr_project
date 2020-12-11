def boxCheck(object):
    """ Check if object has BoxCollider """
    if "BoxCollider" in object.components.keys():
        return True
    return False


def circleCheck(object):
    """ Check if object has CircleCollider """
    if "CircleCollider" in object.components.keys():
        return True
    return False


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
                for o2 in self.scene.objects:
                    if "Rigidbody" in o2.components.keys() and o != o2:
                        self.collisionCheck(o, o2)

    def collisionCheck(self, object1, object2):
        # AABB - AABB collision check
        if boxCheck(object1) and boxCheck(object2):
            rect1 = object1.components["BoxCollider"].rect
            rect2 = object2.components["BoxCollider"].rect

            if (rect1.x < rect2.x + rect2.width and
                    rect1.x + rect1.width > rect2.x and
                    rect1.y < rect2.y + rect2.height and
                    rect1.y + rect1.height > rect2.y):
                self.resolveCollision(object1, object2)
        # AABB - Circle collision check
        if circleCheck(object1) and boxCheck(object2) or circleCheck(object2) and boxCheck(object1):
            pass

    def resolveCollision(self, object1, object2):
        if object1.components["Rigidbody"].mass == 0:
            collider = object2
            collide = object1
        else:
            collider = object1
            collide = object2

        rect1 = collider.components["BoxCollider"].rect
        rect2 = collide.components["BoxCollider"].rect

        right = rect1.x - (rect2.x + rect2.width)
        left = rect2.x - (rect1.x + rect1.width)
        up = rect2.y - (rect1.y + rect1.height)
        down = rect1.y - (rect2.y + rect2.height)

        minDir = max(right, left, up, down)

        # print(str(collider.x) + " " + str(collider.y))

        if minDir == right:
            collider.x -= right
        elif minDir == left:
            collider.x += left
        elif minDir == up:
            collider.y += up
        elif minDir == down:
            collider.y -= down

        rect1.x = collider.x
        rect1.y = collider.y

        # print(str(collider.x) + " " + str(collider.y))
        #
        # print("   " + str(up))
        # print(str(left) + "  " + str(right))
        # print("   " + str(down))
        #
        # print(rect1)
        # print(rect2)


