# UTF-8 RFX [Python] SPA-4 CRLF
# pygame 2.5.2 (SDL 2.28.3, Python 3.9.13)
# Learn base on <Python Crash Course, 2nd Edition ...>
import sys
import pygame as pyg
from settings import Settings
from player import Player
from bullet import Bullet

class AlienInvasion:
    """《外星人入侵》管理游戏资源和行为的类 """
    def __init__(self):
        pyg.init()
        self.setting = Settings()
        #: set window size
        if 1 == 1:
            self.screen = pyg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        else:
            # full screen
            self.screen = pyg.display.set_mode((0,0), pyg.FULLSCREEN)
            self.setting.screen_width = self.screen.get_rect().width
            self.setting.screen_height = self.screen.get_rect().height

        pyg.display.set_caption("Alien Invasion [Arina studying Python Pygame]")
        self.player = Player(self)
        self.bullets = pyg.sprite.Group()


    def run_game(self):
        while True:
            self._check_events()

            self.player.evolve()

            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom > self.screen.get_height():
                    self.bullets.remove(bullet)

            self._update_screen()

    def _check_events(self):
        """ 响应键盘和鼠标事件 """
        for event in pyg.event.get():
            if event.type == pyg.QUIT:  # User close the main window
                sys.exit()# or the window will be closed
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    self.player.mov_direction |= 1
                elif event.key == pyg.K_RIGHT:
                    self.player.mov_direction |= 2
                elif event.key == pyg.K_q:
                    sys.exit()
                elif event.key == pyg.K_SPACE:
                    self._fire()

            elif event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT:
                    self.player.mov_direction &= ~1
                elif event.key == pyg.K_RIGHT:
                    self.player.mov_direction &= ~2
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.player.on_blit()
        for bullet in self.bullets.sprites():
            bullet.on_draw()
        pyg.display.flip()  # re-chrome

    def _fire(self):
        bullet = Bullet(self, self.player, self.player.bullet_speed, self.player.bullet_color, self.player.bullet_width, self.player.bullet_height)
        self.bullets.add(bullet)


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
