import pygame as pg
from config.SoundList import *

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
        "tags": ["static"],
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
            },
            "SoundEffect": {
                "play": True,
                "time": "length",
                "sound": "campfire_s",
                "volume": 0.5
            }
        }
    },
    "player": {
        "class": "Player",
        "name": "player",
        "image": None,
        "tags": ["player"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "BoxCollider": {
                "kinematic": True
            },
            "SoundEffect": {
                "play": False,
                "time": 0.2,
                "sound": "grass_step_s",
                "volume": 1
            }
        }
    },
    "enemy": {
        "class": "Entity",
        "name": "enemy",
        "image": None,
        "tags": ["enemy"],
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
            "EnemyAI": {
                "speed": 128
            }
        }
    },
    "guard": {
        "class": "Entity",
        "name": "enemy",
        "image": None,
        "tags": ["enemy"],
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
            "EnemyAI": {
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
            "AnimalAI": {
                "speed": 128
            },
            "SoundEffect": {
                "play": True,
                "time": 3,
                "sound": "pig_s",
                "volume": 0.5
            }
        }
    },
    "tree": {
        "class": "Entity",
        "name": "tree",
        "image": None,
        "scale": (1, 1),
        "tags": ["static"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
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
            "WanderingAI": {
                "speed": 128
            }
        }
    },
    "npc": {
        "class": "Entity",
        "name": "neutral",
        "image": None,
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
            "WanderingAI": {
                "speed": 128
            }
        }
    },
    "structure": {
        "class": "Entity",
        "name": "structure",
        "image": None,
        "tags": ["static"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
        }
    },
    "bounds": {
        "class": "Entity",
        "name": "bounds",
        "image": None,
        "tags": ["static"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
        }
    }
}
