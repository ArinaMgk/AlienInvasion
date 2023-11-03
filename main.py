# ASCII RFX [Python]
# Learn base on <Python Crash Course, 2nd Edition ...>
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
        pyg.display.set_caption("Alien Invasion [Arina studying Python Pygame]")
        self.player = Player(self)

    def run_game(self):
        while True:
            self._check_events()
            self.player.evolve()
            self._update_screen()

    def _check_events(self):
        """ 响应键盘和鼠标事件 """
        for event in pyg.event.get():
            if event.type == pyg.QUIT:  # User close the main window
                sys.exit()# or the window will be closed
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    self.player.mov_direction = 1
                elif event.key == pyg.K_RIGHT:
                    self.player.mov_direction = 2
                elif event.key == pyg.K_q:
                    sys.exit()
            elif event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT:
                    self.player.mov_direction = 0
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.player.on_blit()
        pyg.display.flip()  # re-chrome


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
