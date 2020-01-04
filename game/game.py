from game.levels.level1 import Level1
from game.spirites.ball import Ball
from game.spirites.bonus import ExpandBonus
from game.spirites.brick import BrickValue, BrickHitNeed
from game.spirites.paddle import Paddle
from game.utils.constans import *
from game.utils.utility import load_img
from game.event import eventManager
from game.state import InitializeState


class Game(object):

    def __init__(self, level_class=Level1, life=3):
        self._screen = pygame.display.get_surface()
        self._paddle = Paddle(PADDLE_X, PADDLE_Y)
        self._ball = Ball(BALL_X, BALL_Y)
        self._level = level_class()
        self._life = life
        self._score = 0

        self._life_img, _ = load_img(LIFE_IMG)
        wd = self._life_img.get_width()
        ht = self._life_img.get_height()
        self._life_rect = [(i*wd, ht) for i in range(1, life+1)]

        self.create_listeners()
        self._all_spirits = pygame.sprite.Group()
        self._state = InitializeState(self)

    def run(self):
        self._state.apply()
        self._check_life()

    def _check_life(self):
        for i, rect in enumerate(self._life_rect):
            if i < self._life:
                self._screen.blit(self._life_img, rect)

    def brick_collide(self, brick):
        brick.hit()
        if brick.hit_counter >= BrickHitNeed[brick.color]:
            self._score += BrickValue[brick.color]
            self._all_spirits.add(ExpandBonus(brick, self._paddle))
            brick.kill()

    def back_to_start(self):
        self._paddle.rect.x = PADDLE_X
        self._paddle.rect.y = PADDLE_Y
        self._ball.rect.x = BALL_X
        self._ball.rect.y = BALL_Y
        self._ball.moving = False

    def create_listeners(self):

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

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def ball(self):
        return self._ball

    @property
    def all_spirits(self):
        return self._all_spirits

    @property
    def paddle(self):
        return self._paddle

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life):
        self._life = life

    @property
    def screen(self):
        return self._screen

    @property
    def score(self):
        return self._score
