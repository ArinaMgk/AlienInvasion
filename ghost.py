# UTF-8 RFX [Python]

import pygame as pyg
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.image = pyg.image.load("./picture/ghost.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.posi_x = float(self.rect.x)
