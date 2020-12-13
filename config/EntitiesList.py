import pygame as pg

# Object tags to entities
from physics.CustomShapes import Circle

entityTags = {
    "P": "player",
    "R": "rooster",
    "C": "campfire",
    "E": "enemy",
    "O": "orc",
    "T": "tree",
    "t": "tent",
    "B": "blacksmith",
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
        "tags" : ["static"],
        "components": {
            "Movable": {
                "vector": pg.Vector2(0, 0)
            },
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            }
        }
    },
    "campfire": {
        "class": "Entity",
        "name": "campfire",
        "image": "campfire_1",
        "scale": (0.75, 0.75),
        "tags" : ["static"],
        "components": {
            "Interactable": {},
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "Animated": {
                "images": ["campfire_1", "campfire_2"],
                "time": 1
            }
        }
    },
    "player": {
        "class": "Player",
        "name": "player",
        "image": "jester",
        "tags" : ["player"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {
                "kinematic": True
            }
        }
    },
    "enemy": {
        "class": "Entity",
        "name": "enemy",
        "image": "barbarian",
        "tags" : ["enemy"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {
                "kinematic": True
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 150
            },
            "enemyAI": {
                "speed": 128
            }
        }
    },
    "orc": {
        "class": "Entity",
        "name": "neutral",
        "image": "orc_base",
        "tags": ["neutral"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {
                "kinematic": True
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 150
            },
            "animalAI": {
                "speed": 128
            }
        }
    },
    "tree": {
        "class": "Entity",
        "name": "tree",
        "image": "tree_1_bot",
        "scale": (1, 1),
        "tags": ["static"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "MultiTile": {
                "parts": {
                    (0, -1): "tree_1_top"
                },
                "size": (1, 2)
            }
        }
    },
    "tent": {
        "class": "Entity",
        "name": "tent",
        "image": "tent_1_bl",
        "scale": (1, 1),
        "tags": ["static"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True,
                "rect": [0, 0, 128, 64]
            },
            "MultiTile": {
                "parts": {
                    (1, 0): "tent_1_br",
                    (0, -1): "tent_1_tl",
                    (1, -1): "tent_1_tr",
                },
                "size": (2, 2)
            }
        }
    },

    "blacksmith": {
        "class": "Entity",
        "name": "neutral",
        "image": "blacksmith",
        "tags": ["neutral"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {
                "kinematic": True
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 150
            },
            "wanderingAI": {
                "speed": 128
            }
        }
    },
}
