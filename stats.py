class GameStats:
    def __init__(self, game):
        self.setting = game.setting
        self.reset()

    def reset(self):
        self.shipleft = 0
        self.shipmax = 0