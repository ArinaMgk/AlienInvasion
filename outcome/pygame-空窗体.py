import sys
import pygame as pyg

class AlienInvasion:
    """《外星人入侵》管理游戏资源和行为的类 """
    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode((800,600))
        pyg.display.set_caption("Alien Invasion [Alice studying Python]")
        self.bg_color = (250, 230, 210)

    def run_game(self):
        while True:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:# User close the main window
                    sys.exit()
            self.screen.fill(self.bg_color)
            pyg.display.flip()# re-chrome



if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
