from game.utils.constans import *
from game.spirites.paddle import Paddle
from game.event import *


class Game(object):

    def __init__(self):
        self._screen = pygame.display.get_surface()
        self._paddle = Paddle(250, 550)

        self._all_spirits = pygame.sprite.Group()
        self._all_spirits.add(self._paddle)

        self._create_move_listeners()

    def run(self):
        self._screen.fill(GAME_BACKGROUND)
        self._all_spirits.update()
        self._all_spirits.draw(self._screen)

    def _create_move_listeners(self):
        def move_left(event):
            if event.key == pygame.K_LEFT:
                self._paddle.move_left()
        eventManager.subscribe(pygame.KEYDOWN, move_left)

        def move_right(event):
            if event.key == pygame.K_RIGHT:
                self._paddle.move_right()
        eventManager.subscribe(pygame.KEYDOWN, move_right)

        def move_stop(event):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self._paddle.move_pos = [0, 0]
        eventManager.subscribe(pygame.KEYUP, move_stop)
