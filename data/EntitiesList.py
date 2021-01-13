from data.ImageList import *
from data.SoundList import *

# Object tags to entities

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
    "cameraPoint": {
        "class": "Entity",
        "name": "cameraPoint",
        "image": None,
        "tags": ["static"],
        "components": {
        }
    },
    "campfire": {
        "class": "Entity",
        "name": "campfire",
        "image": "campfire_1",
        "scale": (0.75, 0.75),
        "tags" : ["static"],
        "components": {
            "Interactable": {
                "text": "\'E\'"
            },
            "Rigidbody": {
                "active": True,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "Animated": {
                "images": [1369, 1370, 1371, 1372],
                "time": 1
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 75
            },
            "SoundEffect": {
                "play": True,
                "time": "length",
                "sound": "campfire_s",
                "volume": 0.5,
                "distance": 300
            },
            "ParticleSystem": {
                "vector": (0, -1),
                "offset": (0, 0),
                "angle": 30,
                "particle": 3171,
                "speed": 100,
                "timeToLive": 2,
                "frequency": 10,
                "size": (0.25, 0.25)
            },
            "SwitchState": {
                "state" : True,
                "offImage": 1368,
                "onImage": 1369,
                "components": [
                    "Animated",
                    "SoundEffect",
                    "ParticleSystem"
                ]

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
            },
            "Damageble": {
                "health": 10,
                "guiHealthContainer": "player_health"
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
                "circle": 200
            },
            "EnemyAI": {
                "speed": 200,
                "damage": 0.5,
                "weapon": SWORD
            },
            "Damageble": {
                "health": 1
            }
        }
    },
    "enemy_throw": {
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
                "circle": 250
            },
            "RangedEnemyAI": {
                "speed": 128,
                "damage": 2,
                "weapon": AXE,
                "projImage": AXE_THROW
            },
            "Damageble": {
                "health": 1
            }
        }
    },
    "orc_boss": {
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
                "circle": 250
            },
            "RangedEnemyAI": {
                "speed": 128,
                "damage": 10,
                "weapon": AXE,
                "projImage": AXE_THROW
            },
            "Damageble": {
                "health": 1
            }
        }
    },
    "projectile": {
        "class": "Entity",
        "name": "projectile",
        "image": None,
        "tags": ["projectile"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "CircleCollider": {
                "kinematic": True,
                "circle": 32
            },
            "Projectile": {
                "speed": 300,
            },
            "Rotatable": {
                "angleChange": 10,
                "continous": True
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
                "speed": 150,
                "damage": 2
            }
        }
    },
    "bunny": {
        "class": "Entity",
        "name": "neutral",
        "image": None,
        "scale": (0.5, 0.5),
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
                "speed": 256
            },
            # "SoundEffect": {
            #     "play": True,
            #     "time": 3,
            #     "sound": "pig_s",
            #     "volume": 0.5
            # }
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
                "speed": 128,
                "dialog": [
                    "Oof, this heat!",
                    "I heard the princess was kidnaped...",
                    "Are you new in town?",
                    "What's with 42 anyways?",
                    "The bandits have been giving us a hard time lately...",
                    "Have a fine day!"
                ]
            },
            "Interactable": {
                "text": "\'E\'"
            },
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
    },
    "consumable": {
        "class": "Entity",
        "name": "consumable",
        "image": None,
        "tags": ["static", "removable"],
        "components": {
            "Rigidbody": {
                "active": False,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "Consumable": {
            },
        }
    },
    "house": {
        "class": "Entity",
        "name": "enterHouse",
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
            "SceneChange": {
                "scene": "House",
                "map": "house_map.json",
                "position": 0
            }
        }
    },
    "town": {
        "class": "Entity",
        "name": "Town",
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
            "SceneChange": {
                "scene": "Town",
                "map": "town_map.json",
                "position": 1
            }
        }
    },
    "cave": {
        "class": "Entity",
        "name": "Cave",
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
            "SceneChange": {
                "scene": "Cave",
                "map": "cave_map.json",
                "position": 0
            }
        }
    },
    "castle": {
        "class": "Entity",
        "name": "Castle",
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
            "SceneChange": {
                "scene": "Castle",
                "map": "castle_map.json",
                "position": 0
            }
        }
    },
    "npc_2": {
        "class": "Entity",
        "name": "neutral",
        "image": None,
        "tags": ["neutral"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 150
            },
            "Interactable": {
                "text": "\'E\'"
            },
            "InteractableAI": {
                "dialog": [
                    "Hello wanderer! How are you?",
                    "Oh? You're looking for the princess?",
                    "You should probably talk to our innkeeper.",
                    "She knows much, and is probably the only one who can help you.",
                    "You'll find her in the inn, middle of town."
                ]
            }
        }
    },
    "npc_3": {
        "class": "Entity",
        "name": "neutral",
        "image": None,
        "tags": ["neutral"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 0
            },
            "BoxCollider": {
                "kinematic": True
            },
            "CircleCollider": {
                "kinematic": False,
                "circle": 150
            },
            "Interactable": {
                "text": "\'E\'"
            },
        }
    },
    "arrow": {
        "class": "Entity",
        "name": "projectile",
        "image": None,
        "tags": ["projectile"],
        "components": {
            "Rigidbody": {
                "active": True,
                "mass": 1
            },
            "CircleCollider": {
                "kinematic": True,
                "circle": 32
            },
            "Projectile": {
                "speed": 600,
            },
            "Rotatable": {
                "continous": False
            },
            "SoundEffect": {
                "play": True,
                "time": 9999,
                "sound": "bow",
                "volume": 1
            },
            "Damageble": {
                "health": 1
            }
        }
    },
    "torch": {
        "class": "Entity",
        "name": "torch",
        "image": None,
        "scale": (1, 1),
        "tags": ["static"],
        "components": {
            "Animated": {
                "images": [473, 474],
                "time": 1
            },
            "SoundEffect": {
                "play": True,
                "time": "length",
                "sound": "campfire_s",
                "volume": 0.25,
                "distance": 200
            },
            "ParticleSystem": {
                "vector": (0, -1),
                "offset": (0, 0),
                "angle": 25,
                "particle": 3171,
                "speed": 100,
                "timeToLive": 1,
                "frequency": 5,
                "size": (0.25, 0.25)
            },
        }
    },
}
