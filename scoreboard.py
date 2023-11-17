import pygame.font

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screct = self.screen.get_rect()
        self.setting = game.setting

        self.color_text = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.on_update()
    def on_update(self):
        self.score_str = str(self.game.stats.shipmax - self.game.stats.shipleft)
        self.score_img = self.font.render(self.score_str, True, self.color_text, self.setting.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screct.right - 20
        self.score_rect.top = 20

    def on_draw(self):
        self.screen.blit(self.score_img, self.score_rect)