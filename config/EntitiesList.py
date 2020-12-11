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
                "vector": pg.Vector2(0, 0)
            },
            "Rigidbody": {
                "mass": 0
            },
            "BoxCollider": {

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
            "Rigidbody": {
                "mass": 1
            },
            "BoxCollider": {

            }
        }
    },
    "dog": {
        "class": "Entity",
        "name": "dog",
        "image": "rooster",
        "components": {
            "Movable": {
                "vector": pg.Vector2(50, 0)
            }
        }
    },
}
