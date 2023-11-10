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
        self.posi_xoffset = 0.0
        self.direction_x = 1 # 0[none] 1[left] 2[right]

        self.speed_x = 0.02
        self.speed_y = -0.05

    def update(self): # special-identifier called by Sprite
        self.posi_y += self.speed_y
        if self.direction_x == 1:
            self.posi_xoffset -= self.speed_x
        elif self.direction_x == 2:
            self.posi_xoffset += self.speed_x

        if abs(self.posi_xoffset) > self.rect.width // 2:
            self.direction_x = int(self.direction_x == 1) + 1

        self.rect.y = self.posi_y
        self.rect.x = self.posi_x + self.posi_xoffset

    def on_draw(self):
        pyg.draw.rect(self.screen, self.color, self.rect)

