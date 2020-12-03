import pygame as pg

# Object tags to entities
entityTags = {
    "P": "player",
    "R": "rooster",
    "C": "campfire",
    ".": None,
    "\n": None
}

# Tile tags to entities
tileTags = {
    ".": "grass_1",
    ":": "grass_2",
    ",": "stone_1",
    ";": "stone_2"
}


# Entities
entities = {
    "rooster": {
        "class": "Entity",
        "name": "rooster",
        "image": "rooster",
        "components": {
            "Movable": {
                "vector": pg.Vector2(50, 0)
            }
        }
    },
    "campfire": {
        "class": "Entity",
        "name": "campfire",
        "image": "campfire_on",
        "components": {
            "Interactable": {}
        }
    },
    "player": {
        "class": "Player",
        "name": "player",
        "image": "npc",
        "components": {
        }
    },
    "dog": {
        "class": "Entity",
        "name": "rooster",
        "image": "rooster",
        "components": {
            "Movable": {
                "vector": pg.Vector2(50, 0)
            }
        }
    },
}
