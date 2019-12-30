from game.utils.constans import *
from game.utils.utility import *
from game.event import eventManager
from game.game import Game


class ArkanoidGame(object):
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = self._create_screen()
        self._game = Game()
        self._running = True

        def __quit_listener(_):
            self._running = False
        eventManager.subscribe(pygame.QUIT, __quit_listener)

    @classmethod
    def _create_screen(cls):
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(DISPLAY_CAPTION)
        pygame.mouse.set_visible(False)
        return pygame.display.get_surface()

    def main_loop(self):
        while self._running:
            eventManager.notify()
            self._game.run()
            pygame.display.flip()
            self._clock.tick(FPS)


if __name__ == '__main__':
    arkanoid = ArkanoidGame()
    arkanoid.main_loop()
