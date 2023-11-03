import sys
import pygame as pyg
from settings import Settings
from player import Player

class AlienInvasion:
    """《外星人入侵》管理游戏资源和行为的类 """
    def __init__(self):
        pyg.init()
        self.setting = Settings()
        self.screen = pyg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pyg.display.set_caption("Alien Invasion [Arina studying Python]")
        self.player = Player(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """ 响应键盘和鼠标事件 """
        for event in pyg.event.get():
            if event.type == pyg.QUIT:  # User close the main window
                sys.exit()# or the window will be closed

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.player.on_blit()
        pyg.display.flip()  # re-chrome


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
