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
        self.posi_y = float(self.rect.y)

        self.speed_x = 0.3
        self.speed_y = -0.1

    def update(self): # special-identifier called by Sprite
        self.posi_y += self.speed_y
        self.rect.y = self.posi_y

    def on_draw(self):
        pyg.draw.rect(self.screen, self.color, self.rect)

