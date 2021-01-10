from components.Components import *
from physics.CustomShapes import *
from components.Timer import *
from physics.Math import *


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
        self.originalImage = self.parent.image
        self.angle = 0
        self.angleChange = self.checkArgs("angleChange")

    def physicsUpdate(self):
        orig_rect = self.originalImage.get_rect()
        rot_image = pg.transform.rotate(self.originalImage, self.angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.parent.image = rot_image.subsurface(rot_rect).copy()

        self.angle += self.angleChange
        self.angle = self.angle % 360


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
            rect = args["rect"]
            self.rect = pg.Rect(parent.x + rect[0], parent.y + rect[1], rect[2], rect[3])
        else:
            self.rect = parent.rect

        self.kinematic = self.checkArgs("kinematic")

    def physicsUpdate(self):
        pass

    def action(self):
        # print(self.rect)
        pass

    def drawCollider(self, screen, color, outline, camera):
        position = camera.applyPosition((self.rect.x, self.rect.y))
        pg.draw.rect(screen, color, (position[0], position[1], self.rect.width, self.rect.height), outline)

    def detected(self, collider):
        # print("Detected")
        for k, c in self.parent.components.items():
            c.collisionDetected(collider, colType="box")


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
            c.collisionDetected(collider, colType="circle")

    def action(self):
        # print(self.circle)
        pass

    def drawCollider(self, screen, color, outline, camera):
        self.circle.draw(screen, color, outline, camera)


class TransformComponent(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.parent.rect.x = self.parent.x
        self.parent.rect.y = self.parent.y


class ParticleSystem(Component):
    def __init__(self, parent, args):
        super().__init__(parent, args)
        self.vector = self.checkArgs("vector")
        self.offset = self.checkArgs("offset")
        self.angle = self.checkArgs("angle")
        self.particle = self.checkArgs("particle")
        if self.particle:
            self.particle = self.parent.game.all_images[self.particle]

        self.speed = self.checkArgs("speed")
        self.timeToLive = self.checkArgs("timeToLive")
        self.frequency = self.checkArgs("frequency")
        self.size = self.checkArgs("size", (1, 1))
        self.timer = Timer(1/self.frequency, self.parent.game)
        self.particles = []
        self.spawnParticle()

    def disabledUpdate(self):
        self.particles = []

    def physicsUpdate(self):
        time = self.timer.checkTime()
        if time:
            self.spawnParticle()

        for p in self.particles:
            p.update()

    def spawnParticle(self):
        x = self.parent.x + self.parent.rect.width/2
        y = self.parent.y + self.parent.rect.height/2
        vector = randomAngle(self.vector, self.angle)
        self.particles.append(Particle(self, x, y, vector, self.particle, self.speed, self.timeToLive, self.size))

    def draw(self):
        for p in self.particles:
            p.draw()


class Particle:
    def __init__(self, parent, x, y, vector, image, speed, ttl, scale=None):
        self.parent = parent
        self.vector = pg.Vector2(vector)
        self.image = image
        self.speed = speed
        self.screen = self.parent.parent.game.renderer.screen
        self.camera = self.parent.parent.game.renderer.camera
        self.ttl = ttl
        self.timer = Timer(self.ttl, self.parent.parent.game)
        if scale:
            preScale = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(preScale.width * scale[0]), int(preScale.height * scale[1])))
        self.rect = self.image.get_rect()
        self.x = x - self.rect.width/2
        self.y = y - self.rect.height/2
        # self.cover = pg.Surface((32, 32))
        # self.cover.fill(BLACK)

    def update(self):
        self.x += self.vector.x * self.speed * self.parent.parent.game.dt
        self.y += self.vector.y * self.speed * self.parent.parent.game.dt
        if self.timer.checkTime():
            self.die()

    def draw(self):
        self.screen.blit(self.image, self.camera.applyPosition((self.x, self.y)))

    def die(self):
        self.parent.particles.remove(self)
