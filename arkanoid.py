"""
Arkanoid Game write with pygame module
"""
import pygame
from game.utils.constans import WIDTH, HEIGHT, DISPLAY_CAPTION, FPS
from game.event import EVENT_MANAGER
from game.game import Game


class ArkanoidGame:
    """
    Base class
    """
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = self.create_screen()
        self._game = Game()
        self._running = True

        def __quit_listener(_):
            self._running = False
        EVENT_MANAGER.subscribe(pygame.QUIT, __quit_listener)

    @classmethod
    def create_screen(cls):
        """
        method create screen
        :return pygame sufrace:
        """
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(DISPLAY_CAPTION)
        pygame.mouse.set_visible(False)
        return pygame.display.get_surface()

    def main_loop(self):
        """
        main_loop draw all game
        :return None:
        """
        while self._running:
            EVENT_MANAGER.notify()
            self._game.run()
            pygame.display.flip()
            self._clock.tick(FPS)


if __name__ == '__main__':
    ARKANOID = ArkanoidGame()
    ARKANOID.main_loop()
