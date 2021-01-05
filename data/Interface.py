from config.Settings import *
import pygame as pg

BUTTON_IMAGE_GREEN = pg.image.load(RESOURCES + "ui\\" + "green_button00.png")
BUTTON_IMAGE_RED = pg.image.load(RESOURCES + "ui\\" + "red_button11.png")
BUTTON_IMAGE_BLUE = pg.image.load(RESOURCES + "ui\\" + "blue_button00.png")
BUTTON_IMAGE_YELLOW = pg.image.load(RESOURCES + "ui\\" + "yellow_button00.png")

interface = {
    "title_text": {
        "type": "TextBox",
        "name": "Title",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2 - 48, 0)
        }
    },
    "heart_1": {
        "type": "ImageBox",
        "name": "H1",
        "args": {
            "image": "heart",
            "position": (0, 0)
        }
    },
    "heart_2": {
        "type": "ImageBox",
        "name": "H2",
        "args": {
            "image": "heart",
            "position": (63, 0)
        }
    },
    "heart_3": {
        "type": "ImageBox",
        "name": "H3",
        "args": {
            "image": "heart",
            "position": (126, 0)
        }
    },
    "position_text": {
        "type": "TextBox",
        "name": "Position",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2, HEIGHT - 64),
            "centered": True
        }
    },
    "test_button": {
        "type": "Button",
        "name": "TestBtn",
        "args": {
            "text": "Test",
            "image": BUTTON_IMAGE_RED,
            "backgroundColor": RED,
            "color": GREEN,
            "size": (128, 64),
            "position": (0, 63)
        }
    },
    "fps_text": {
        "type": "TextBox",
        "name": "FPS",
        "args": {
            "text": "Test",
            "position": (WIDTH - 35, 0),
            "centered": True
        }
    },
    "camera_offset_text": {
        "type": "TextBox",
        "name": "CameraOffset",
        "args": {
            "text": "Test",
            "position": (WIDTH / 2, HEIGHT - 128),
            "centered": True
        }
    },
}

menuInterfaces = {
    "MainMenu": {
        "font": "pixel.ttf",
        "fontSize": 25,
        "components": {
            "titleLabel": {
                "type": "TextBox",
                "name": "Title",
                "args": {
                    "text": "Igra",
                    "position": (WIDTH / 2, 0),
                    "anchor": "center-top",
                    "centered": True,
                    "font": "pixel.ttf",
                    "fontSize": 100,
                    "textColor": BLUE,
                }
            },
            "newBtn": {
                "type": "Button",
                "name": "NewButton",
                "args": {
                    "text": "New",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "backgroundColor": RED,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 150),
                    "centered": True,
                    "action": "new"
                }
            },
            "contBtn": {
                "type": "Button",
                "name": "ContinueButton",
                "args": {
                    "text": "Continue",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 250),
                    "centered": True,
                    "active": False
                }
            },
            "settingsBtn": {
                "type": "Button",
                "name": "SettingsButton",
                "args": {
                    "text": "Settings",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 350),
                    "centered": True,
                    "action": "settings",
                }
            },
            "quitBtn": {
                "type": "Button",
                "name": "QuitButton",
                "args": {
                    "text": "Quit",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 450),
                    "centered": True,
                    "action": "quit"
                }
            }
        }
    },

    "PauseMenu": {
        "font": "pixel.ttf",
        "fontSize": 25,
        "components": {
            "titleLabel": {
                "type": "TextBox",
                "name": "Title",
                "font": "pixel.ttf",
                "fontSize": 50,
                "args": {
                    "text": "Paused",
                    "textColor": WHITE,
                    "position": (WIDTH / 2, 0),
                    "anchor": "center-top",
                    "centered": True
                }
            },
            "resumeBtn": {
                "type": "Button",
                "name": "ResumeButton",
                "args": {
                    "text": "Resume",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "backgroundColor": RED,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 100),
                    "centered": True,
                    "action": "resume"
                }
            },
            "settingsBtn": {
                "type": "Button",
                "name": "SettingsButton",
                "args": {
                    "text": "Settings",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 200),
                    "centered": True,
                    "action": "settings"
                }
            },
            "quitBtn": {
                "type": "Button",
                "name": "QuitButton",
                "args": {
                    "text": "Quit",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 300),
                    "centered": True,
                    "action": "quit"
                }
            }
        }
    },

    "SettingsMenu": {
        "font": "pixel.ttf",
        "fontSize": 25,
        "components": {
            "titleLabel": {
                "type": "TextBox",
                "name": "Title",
                "font": "pixel.ttf",
                "fontSize": 50,
                "args": {
                    "text": "Settings",
                    "textColor": WHITE,
                    "position": (WIDTH / 2, 0),
                    "anchor": "center-top",
                    "centered": True
                }
            },
            "backBtn": {
                "type": "Button",
                "name": "BackButton",
                "args": {
                    "text": "Back",
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 600),
                    "centered": True,
                    "action": "back"
                }
            },
            "musicBtn": {
                "type": "Button",
                "name": "MusicButton",
                "args": {
                    "text": "Music: ",
                    "switch": True,
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 100),
                    "centered": True,
                    "action": "changeSetting",
                    "actionArgs": {
                        "setting": "music"
                    }
                }
            },
            "soundBtn": {
                "type": "Button",
                "name": "SoundButton",
                "args": {
                    "text": "Sound: ",
                    "switch": True,
                    "image": BUTTON_IMAGE_BLUE,
                    "background": None,
                    "color": GREEN,
                    "size": (256, 64),
                    "position": (WIDTH / 2, 200),
                    "centered": True,
                    "action": "changeSetting",
                    "actionArgs": {
                        "setting": "sound"
                    }
                }
            }
        }
    }
}
