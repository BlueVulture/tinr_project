class Scene:
    entities = []
    objects = [] 
    tiles = []

    def __init__(self):
        pass

    def addTile(self, tile):
        self.entities.append(tile)
        self.tiles.append(tile)

    def addObject(self, object):
        self.entities.append(object)
        self.objects.append(object)

    def removeTile(self, tile):
        self.entities.append(tile)
        self.tiles.remove(tile)

    def removeObject(self, object):
        self.entities.append(object)
        self.objects.remove(object)