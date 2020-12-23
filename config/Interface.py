from config.Settings import *

interface = [
    {
        "type": "TextDisplay",
        "id": 0,
        "name": "Title",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2 - 48, 0)
        }
    },
    {
        "type": "ImageDisplay",
        "id": 1,
        "name": "H1",
        "args": {
            "image": "heart",
            "position": (0, 0)
        }
    },
    {
        "type": "ImageDisplay",
        "id": 2,
        "name": "H2",
        "args": {
            "image": "heart",
            "position": (63, 0)
        }
    },
{
        "type": "ImageDisplay",
        "id": 3,
        "name": "H3",
        "args": {
            "image": "heart",
            "position": (63, 0)
        }
    },
    {
        "type": "TextDisplay",
        "id": 4,
        "name": "Position",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2, HEIGHT - 64),
            "centered": True
        }
    },
    {
        "type": "Button",
        "id": 5,
        "name": "TestBtn",
        "args": {
            "text": "Test",
            "image": "",
            "background": None,
            "color": GREEN,
            "size": (128, 64),
            "position": (0, 63)
        }
    }
]
