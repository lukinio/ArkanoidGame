from game.utils.constans import *
from game.utils.utility import *


class ArkanoidGame(object):
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = self._create_screen()
        self._running = True

    @classmethod
    def _create_screen(cls):
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(DISPLAY_CAPTION)
        pygame.mouse.set_visible(False)
        return pygame.display.get_surface()

    def main_loop(self):
        while self._running:
            self._screen.fill(GAME_BACKGROUND)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self._running = False

            pygame.display.flip()
            self._clock.tick(FPS)


if __name__ == '__main__':
    arkanoid = ArkanoidGame()
    arkanoid.main_loop()
