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
    ";": "stone_2",
    "\n": None
}


# Entities
entities = {
    "rooster": {
        "class": "Entity",
        "name": "rooster",
        "image": "rooster",
        "scale": (0.75, 0.75),
        "components": {
            "Movable": {
                "vector": pg.Vector2(0, 0)
            },
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {}
        }
    },
    "campfire": {
        "class": "Entity",
        "name": "campfire",
        "image": "campfire_1",
        "scale": (0.75, 0.75),
        "components": {
            "Interactable": {},
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {},
            "Animated": {
                "images": [],
                "time": 1
            }
        }
    },
    "player": {
        "class": "Player",
        "name": "player",
        "image": "jester",
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {}
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
