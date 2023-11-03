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

        # flags
        self.mov_direction = 0 # [0 kept] [1 left] [2 right]
        self.posi = float(self.rect.x)
        self.speed = 0.5

    def evolve(self):
        if self.mov_direction == 1 and self.rect.left > 0:
            self.posi -= self.speed
        elif self.mov_direction == 2 and self.rect.right < self.screen_rect.right:
            self.posi += self.speed

        self.rect.x = self.posi

    def on_blit(self):
        self.screen.blit(self.image, self.rect)
