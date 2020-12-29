from config.Settings import *

interface = [
    {
        "type": "TextDisplay",
        "id": "title_text",
        "name": "Title",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2 - 48, 0)
        }
    },
    {
        "type": "ImageDisplay",
        "id": "heart_1",
        "name": "H1",
        "args": {
            "image": "heart",
            "position": (0, 0)
        }
    },
    {
        "type": "ImageDisplay",
        "id": "heart_2",
        "name": "H2",
        "args": {
            "image": "heart",
            "position": (63, 0)
        }
    },
    {
        "type": "ImageDisplay",
        "id": "heart_3",
        "name": "H3",
        "args": {
            "image": "heart",
            "position": (126, 0)
        }
    },
    {
        "type": "TextDisplay",
        "id": "position_text",
        "name": "Position",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2, HEIGHT - 64),
            "centered": True
        }
    },
    {
        "type": "Button",
        "id": "test_button",
        "name": "TestBtn",
        "args": {
            "text": "Test",
            "image": "",
            "background": None,
            "color": GREEN,
            "size": (128, 64),
            "position": (0, 63)
        }
    },
{
        "type": "TextDisplay",
        "id": "fps_text",
        "name": "FPS",
        "args": {
            "text": "Test",
            "position": (WIDTH-35, 0),
            "centered": True
        }
    },
    {
        "type": "TextDisplay",
        "id": "camera_offset_text",
        "name": "CameraOffset",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2, HEIGHT - 128),
            "centered": True
        }
    },
]
