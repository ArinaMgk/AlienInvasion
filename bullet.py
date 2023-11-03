# UTF-8 RFX [Python]

import pygame as pyg
from pygame.sprite import Sprite

class Bullet(Sprite):
    # move down and sent by player
    def __init__(self, game, sender, b_speed, b_color, b_width, b_height):
        super().__init__()
        self.screen = game.screen
        self.speed = b_speed
        self.color = b_color
        self.rect = pyg.Rect(sender.posi + sender.rect.width / 2, sender.rect.height, b_width, b_height)

        self.posi_y = float(self.rect.y)

    def update(self): # special-identifier called by Sprite
        self.posi_y += self.speed
        self.rect.y = self.posi_y

    def on_draw(self):
        pyg.draw.rect(self.screen, self.color, self.rect)
