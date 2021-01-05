SOUND = True

def changeSetting(game, setting, value=None, switch=False):
    game.settings[setting] = setSetting(game, setting, switch, value)


def setSetting(game, setting, switch, value):
    if switch:
        return not game.settings[setting]
    elif value:
        return value

    return False


def saveSettings(game):
    data = game.settings

    with open('config/settings.json', 'w') as outfile:
        json.dump(data, outfile)


def readSettings(game):
    with open('config/settings.json', 'r') as infile:
        data = json.load(infile)
        game.settings = data