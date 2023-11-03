import pygame as pyg

class Player:
    """ 玩家类 """
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pyg.image.load("./picture/reimu.png")
        self.rect = self.image.get_rect()
        # set position top-mid(p2), or at p0 point
        self.rect.midtop = self.screen_rect.midtop

    def on_blit(self):
        self.screen.blit(self.image, self.rect)
