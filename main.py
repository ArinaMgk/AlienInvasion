# UTF-8 RFX [Python] SPA-4 CRLF
# pygame 2.5.2 (SDL 2.28.3, Python 3.9.13)
# Learn base on <Python Crash Course, 2nd Edition ...>
import sys
import pygame as pyg
from settings import Settings
from player import Player
from bullet import Bullet
from ghost import Ghost
from button import Button
from stats import GameStats
from time import sleep
from scoreboard import Scoreboard

GHOST_HEIGHT = GHOST_WIDTH = 60
PLAYER_HEIGHT = 60

class AlienInvasion:
    """《外星人入侵》管理游戏资源和行为的类 """
    def __init__(self):
        pyg.init()
        self.setting = Settings()
        self.stats = GameStats(self)
        #: set window size
        if 1 == 1:
            self.screen = pyg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        else:
            # full screen
            self.screen = pyg.display.set_mode((0,0), pyg.FULLSCREEN)
            self.setting.screen_width = self.screen.get_rect().width
            self.setting.screen_height = self.screen.get_rect().height
        self.flag_active = False

        pyg.display.set_caption("Alien Invasion [Arina studying Python Pygame]")
        self.player = Player(self)
        self.bullets = pyg.sprite.Group()

        self.ghost_xnumber = self.setting.screen_width // (GHOST_WIDTH * 2)
        self.ghost_ynumber = (self.setting.screen_height - PLAYER_HEIGHT) // 2 // (GHOST_HEIGHT * 2)
        self.ghosts = pyg.sprite.Group()
        for j in range(self.ghost_ynumber):
            for i in range(self.ghost_xnumber):
                self.ghosts.add(Ghost(self, GHOST_WIDTH * (i*2+1), self.screen.get_height() - GHOST_HEIGHT * (1+2*j)))
                self.stats.shipleft += 1
        self.stats.shipmax = self.stats.shipleft

        self.play_btn = Button(self, "Start")
        self.scoreboard = Scoreboard(self)

    def run_game(self):
        self.lose = 0
        while self.ghosts:
            self._check_events()
            if self.flag_active:
                self.player.evolve()

                self.bullets.update()
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom > self.screen.get_height():
                        self.bullets.remove(bullet)

                self.ghosts.update()
                for ghost in self.ghosts:
                    if ghost.rect.top < PLAYER_HEIGHT:
                        self.lose += 1
                        self.ghosts.remove(ghost)

            self._update_screen()
        self.flag_active = False
        print(f"Thanks for your playing. You lose is {self.lose}.")

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

            elif event.type == pyg.MOUSEBUTTONDOWN:
                cursor = pyg.mouse.get_pos()
                if self.play_btn.rect.collidepoint(cursor) and ~self.flag_active:
                    self.flag_active = True
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)

        self.player.on_blit()
        for bullet in self.bullets.sprites():
            bullet.on_draw()

        # 是否有子弹射中鬼桑
        collsions = pyg.sprite.groupcollide(self.bullets,self.ghosts,True,True)
        if(collsions):
            self.stats.shipleft -= 1
            self.scoreboard.on_update()

        self.ghosts.draw(self.screen)
        self.scoreboard.on_draw()

        if not self.flag_active:
            self.play_btn.on_draw()

        pyg.display.flip()  # re-chrome

    def _fire(self):
        bullet = Bullet(self, self.player, self.player.bullet_speed, self.player.bullet_color, self.player.bullet_width, self.player.bullet_height)
        self.bullets.add(bullet)


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
