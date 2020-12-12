class Scene:
    entities = []
    objects = [] 
    tiles = []
    characters = []

    def __init__(self):
        pass

    def addTile(self, tile):
        self.entities.append(tile)
        self.tiles.append(tile)

    def addObject(self, object):
        self.entities.append(object)
        self.objects.append(object)

    def addCharacter(self, character):
        self.entities.append(character)
        self.characters.append(character)

    def removeTile(self, tile):
        self.entities.remove(tile)
        self.tiles.remove(tile)

    def removeObject(self, object):
        self.entities.remove(object)
        self.objects.remove(object)

    def removeCharacter(self, character):
        self.entities.remove(character)
        self.characters.remove(character)
