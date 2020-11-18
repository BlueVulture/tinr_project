class Scene:
    objects = [] 
    tiles = []

    def __init__(self):
        pass

    def addTile(self, tile):
        self.tiles.append(tile)

    def addObject(self, object):
        self.objects.append(object)