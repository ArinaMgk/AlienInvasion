import pygame.font
import pygame.font as pgf

class Button:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.scr_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.color_back = (10, 100, 10)
        self.color_text = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的 rect 对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.scr_rect.center

        #按钮的标签只需要创建一次
        self.msg_image = self.font.render(msg, True, self.color_text, self.color_back)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def on_draw(self):
        self.screen.fill(self.color_back, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

