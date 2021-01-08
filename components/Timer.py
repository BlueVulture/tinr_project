class Timer:
    def __init__(self, t, game):
        self.t = t
        self.game = game
        self.currentTime = 0

    def checkTime(self):
        if self.currentTime >= self.t:
            self.currentTime = 0
            return True
        else:
            self.currentTime += (self.game.dt * 1000)
            return False

