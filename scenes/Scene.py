class Scene:
    objects = [] 
    tiles = []

    def addTile(self, tile):
        self.tiles.append(tile)

    def addObject(self, object):
        self.objects.append(object)