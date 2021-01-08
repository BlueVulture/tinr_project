from math import *
from physics.Math import *


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

    def setScene(self):
        self.scene = self.game.level.scene

    def physicsUpdate(self):
        """ Updates all physical components of objects in the scene. """
        for o in self.scene.updatable:
            # print(o.name)
            if "BoxCollider" in o.components.keys():
                o.components["BoxCollider"].physicsUpdate()

            if "CircleCollider" in o.components.keys():
                o.components["CircleCollider"].physicsUpdate()

            if "Movable" in o.components.keys():
                o.components["Movable"].physicsUpdate()

            if "Rotatable" in o.components.keys():
                o.components["Rotatable"].physicsUpdate()

            if "ParticleSystem" in o.components.keys():
                o.components["ParticleSystem"].physicsUpdate()

            if "Rigidbody" in o.components.keys():
                o.components["Rigidbody"].physicsUpdate()
                if o.components["Rigidbody"].active:
                    for o2 in self.scene.updatable:
                        if "Rigidbody" in o2.components.keys() and o != o2:
                            self.collisionCheck(o, o2)

    def collisionCheck(self, object1, object2):
        """
        Checks for collisions between the given two objects.
        Currently implements two collision types:

        - AABB - AABB collisions
        - AABB - Circle collisions
        """
        # AABB - AABB collision check
        if boxCheck(object1) and boxCheck(object2):
            self.checkAABBColision(object1, object2)

        # AABB - Circle collision check
        if circleCheck(object1) and boxCheck(object2):
            self.checkCircleCollison(object1, object2)

    def checkAABBColision(self, object1, object2):
        rect1 = object1.components["BoxCollider"].rect
        rect2 = object2.components["BoxCollider"].rect

        if (rect1.x < rect2.x + rect2.width and
                rect1.x + rect1.width > rect2.x and
                rect1.y < rect2.y + rect2.height and
                rect1.y + rect1.height > rect2.y):
            self.resolveCollision(object1, object2)

    def checkCircleCollison(self, object1, object2):
        circle = object1.components["CircleCollider"].circle
        rect = object2.components["BoxCollider"].rect

        closestX = clamp(circle.x, rect.x, rect.x + rect.width)
        closestY = clamp(circle.y, rect.y, rect.y + rect.height)

        distanceX = circle.x - closestX
        distanceY = circle.y - closestY

        distanceSquared = (distanceX ** 2) + (distanceY ** 2)
        # print(object1.name + "" + object2.name)
        if distanceSquared < (circle.radius * circle.radius) and not object1.components["CircleCollider"].kinematic:
            object1.components["CircleCollider"].detected(object2)

        if distanceSquared < (circle.radius * circle.radius) and object1.components["CircleCollider"].kinematic:
            object1.components["CircleCollider"].detected(object2)


    def resolveCollision(self, object1, object2):
        """ Collision resolution method. Restricts object movement for active-passive collisions. """
        # TO-DO: active - active
        # IDEA:
        #   normalize mass of both objects (ie. obj1.mass + obj2.mass = 1),
        #   then move BOTH objects by multiplicating their normalized mass
        #   with how much they should move.
        #   Also implement velocity, so then maybe normalized mass + velocity?
        #   Transform component for velocity

        if object1.components["Rigidbody"].mass > object2.components["Rigidbody"].mass:
            collider = object2
            collide = object1
        else:
            collider = object1
            collide = object2

        colliderRigid = collider.components["Rigidbody"]
        collideRigid = collide.components["Rigidbody"]

        if collideRigid.mass == 0:
            colliderWeight = 1
            collideWeight = 0
        else:
            massSum = collideRigid.mass + colliderRigid.mass
            colliderWeight = (colliderRigid.mass / massSum)
            collideWeight = (collideRigid.mass / massSum)

        rect1 = collider.components["BoxCollider"].rect
        rect2 = collide.components["BoxCollider"].rect

        right = rect1.x - (rect2.x + rect2.width)
        left = rect2.x - (rect1.x + rect1.width)
        up = rect2.y - (rect1.y + rect1.height)
        down = rect1.y - (rect2.y + rect2.height)

        minDir = max(right, left, up, down)

        if minDir == right:
            collider.x -= right * colliderWeight
            collide.x += right * collideWeight
        elif minDir == left:
            collider.x += left * colliderWeight
            collide.x -= left * collideWeight
        elif minDir == up:
            collider.y += up * colliderWeight
            collide.y -= up * collideWeight
        elif minDir == down:
            collider.y -= down * colliderWeight
            collide.y += down * collideWeight

        collider.components["BoxCollider"].detected(collide)
        collide.components["BoxCollider"].detected(collider)

        rect1.x = collider.x
        rect1.y = collider.y
        rect2.x = collide.x
        rect2.y = collide.y

        # print(str(collider.x) + " " + str(collider.y))
        #
        # print("   " + str(up))
        # print(str(left) + "  " + str(right))
        # print("   " + str(down))
        #
        # print(rect1)
        # print(rect2)
