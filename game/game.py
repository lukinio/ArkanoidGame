from game.utils.constans import *
from game.spirites.paddle import Paddle
from game.spirites.ball import Ball
from game.event import *
from game.levels.level1 import Level1


class Game(object):

    def __init__(self, level_class=Level1):
        self._screen = pygame.display.get_surface()
        self._paddle = Paddle(250, 550)
        self._ball = Ball(295, 540)
        self._level = level_class(100)
        self._brick = self._level.create_level()

        self._all_spirits = pygame.sprite.Group()
        self._all_spirits.add(self._paddle)
        self._all_spirits.add(self._ball)
        self._all_spirits.add(self._brick)

        self._ball.add_collide_sprites(self._paddle, True)
        self._ball.add_collide_sprites(self._brick)

        self._create_listeners()

    def run(self):
        self._screen.fill(GAME_BACKGROUND)
        self._all_spirits.update()
        self._all_spirits.draw(self._screen)

    def _create_listeners(self):

        def ball_start(event):
            if event.key == pygame.K_SPACE:
                self._ball.moving = True

        # paddle move listeners
        def move_left(event):
            if event.key == pygame.K_LEFT:
                self._paddle.move_left()
                self._ball.move_left()

        def move_right(event):
            if event.key == pygame.K_RIGHT:
                self._paddle.move_right()
                self._ball.move_right()

        eventManager.subscribe(pygame.KEYDOWN, ball_start, move_left, move_right)

        def move_stop(event):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self._paddle.move_pos = [0, 0]
                self._ball.move_pos = [0, 0]

        eventManager.subscribe(pygame.KEYUP, move_stop)
