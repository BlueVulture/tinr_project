class Scene:
    entities = []
    structures = []
    objects = []
    tiles = []
    characters = []
    layers = []
    updatable = []

    def __init__(self):
        pass

    def addEntity(self, entity, entityType, layer, updatable=False):
        self.entities.append(entity)
        if len(self.layers) <= layer:
            for x in range((layer-len(self.layers))+1):
                self.layers.append([])

        self.layers[layer].append(entity)

        if entityType == "tile":
            self.tiles.append(entity)
        elif entityType == "object":
            self.objects.append(entity)
        elif entityType == "character":
            self.characters.append(entity)
        elif entityType == "structure":
            self.structures.append(entity)

        if updatable:
            self.updatable.append(entity)

    def addTile(self, tile):
        self.entities.append(tile)
        self.tiles.append(tile)

    def addObject(self, object):
        self.entities.append(object)
        self.objects.append(object)

    def addStructure(self, structure):
        self.structures.append(structure)
        self.objects.append(structure)

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

    def removeStructure(self, structure):
        self.structures.remove(structure)
        self.objects.remove(structure)
