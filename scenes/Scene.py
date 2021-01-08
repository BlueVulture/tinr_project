class Scene:
    # Index of entities
    index = {}

    # All entities
    entities = []

    # Entity types
    structures = []
    objects = []
    tiles = []
    characters = []

    # Interactions with game world
    layers = []
    updatable = []

    def __init__(self):
        self.index = {}
        self.entities = []
        self.structures = []
        self.objects = []
        self.tiles = []
        self.characters = []
        self.layers = []
        self.updatable = []

    def addEntity(self, entity, entityType, layer, entityID=None, updatable=False):
        self.entities.append(entity)
        includedIn = ["self.entities"]

        if len(self.layers) <= layer:
            for x in range((layer - len(self.layers)) + 1):
                self.layers.append([])

        self.layers[layer].append(entity)
        includedIn.append("self.layers[" + str(layer) + "]")

        if entityType == "tile":
            self.tiles.append(entity)
            includedIn.append("self.tiles")
        elif entityType == "object":
            self.objects.append(entity)
            includedIn.append("self.objects")
        elif entityType == "character":
            self.characters.append(entity)
            includedIn.append("self.characters")
        elif entityType == "structure":
            self.structures.append(entity)
            includedIn.append("self.structures")

        if updatable:
            self.updatable.append(entity)
            includedIn.append("self.updatable")

        if entityID:
            self.index[entityID] = includedIn
        else:
            i = len(self.index)
            self.index[entityID] = includedIn

    def removeEntity(self, entity, entityID=None):
        if entityID:
            for i in self.index[entityID]:
                eval(i).remove(entity)
        else:
            lists = [self.entities,
                     self.structures,
                     self.objects,
                     self.tiles,
                     self.characters,
                     self.layers,
                     self.updatable]

            for i in lists:
                if entity in i:
                    i.remove(entity)
