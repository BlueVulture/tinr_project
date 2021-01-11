class Timer:
    def __init__(self, t, game):
        self.t = t * 1000
        self.game = game
        self.currentTime = 0

    def checkTime(self):
        if self.currentTime >= self.t:
            self.currentTime = 0
            return True
        else:
            self.currentTime += (self.game.dt * 2000)
            return False

    def reset(self):
        self.currentTime = 0

