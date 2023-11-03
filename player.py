# UTF-8 RFX [Python]
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
        self.mov_direction = 0 # [0 or 3 kept] [1 left] [2 right]
        self.posi = float(self.rect.x)
        self.speed = 1.0

        # bullet
        self.bullet_speed = 1
        self.bullet_color = (160, 60, 60)
        self.bullet_width = 5
        self.bullet_height = 15


    def evolve(self):
        if self.mov_direction == 1 and self.rect.left > 0:
            self.posi -= self.speed
        elif self.mov_direction == 2 and self.rect.right < self.screen_rect.right:
            self.posi += self.speed

        self.rect.x = self.posi

    def on_blit(self):
        self.screen.blit(self.image, self.rect)
