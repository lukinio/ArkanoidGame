"""
Game
"""
import pygame
from game.levels.level1 import Level1
from game.spirites.ball import Ball
from game.spirites.bonus import NormalPaddle
from game.spirites.brick import BRICK_VALUE, BRICK_HIT_NEED
from game.spirites.paddle import Paddle
from game.utils.utility import load_img
from game.event import EVENT_MANAGER
from game.state import InitializeState
from game.utils.constans import (PADDLE_X, PADDLE_Y, BALL_X, BALL_Y, LIFE_IMG)


class Game:
    """
    class represent whole game which hold all element
    """

    def __init__(self, level_class=Level1, life=3):
        """
        :param level_class:
        :param life:
        """
        self._screen = pygame.display.get_surface()
        self._paddle = Paddle(PADDLE_X, PADDLE_Y)
        self._ball = Ball(BALL_X, BALL_Y)
        self._level = level_class()
        self._life = life
        self._score = 0

        self._life_img, _ = load_img(LIFE_IMG)
        self._life_rect = None
        self.check_life()

        self.create_listeners()
        self._all_spirits = pygame.sprite.Group()
        self._state = InitializeState(self)
        self._paddle.state = NormalPaddle(self)

    def run(self):
        """
        method which call draw all sprites depends on state
        :return:
        """
        self._state.apply()
        self._show_life()

    def _show_life(self):
        """
        display player life on screen
        :return:
        """
        for i, rect in enumerate(self._life_rect):
            if i < self._life:
                self._screen.blit(self._life_img, rect)

    def check_life(self):
        """
        set proper number of rect for player lifes
        :return:
        """
        width = self._life_img.get_width()
        self._life_rect = [(i*width, width) for i in range(1, self._life+1)]

    def brick_collide(self, brick):
        """
        :param brick:
        :return:
        """
        brick.hit()
        if brick.hit_counter >= BRICK_HIT_NEED[brick.color]:
            self._score += BRICK_VALUE[brick.color]
            if brick.has_bonus:
                self._all_spirits.add(brick.bonus(brick, self))
            brick.kill()

    def back_to_start(self):
        """
        set paddle and ball on start position
        :return:
        """
        self._paddle.rect.x = PADDLE_X
        self._paddle.rect.y = PADDLE_Y
        self._ball.rect.x = BALL_X
        self._ball.rect.y = BALL_Y
        self._ball.moving = False

    def create_listeners(self):
        """
        create listeners to control sprites
        :return:
        """

        def ball_start(event):
            if event.key == pygame.K_SPACE:
                self._ball.moving = True

        # paddle move listeners
        def move_left(event):
            if event.key == pygame.K_LEFT:
                self._paddle.move_left()

        def move_right(event):
            if event.key == pygame.K_RIGHT:
                self._paddle.move_right()

        EVENT_MANAGER.subscribe(pygame.KEYDOWN, ball_start, move_left, move_right)

        def move_stop(event):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self._paddle.move_pos = [0, 0]
                self._ball.move_pos = [0, 0]

        EVENT_MANAGER.subscribe(pygame.KEYUP, move_stop)

    @property
    def state(self):
        """
        get state of game
        :return state:
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        set state of game
        :param state:
        :return:
        """
        self._state = state

    @property
    def level(self):
        """
        :return level:
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        set level
        :param level:
        :return:
        """
        self._level = level

    @property
    def ball(self):
        """
        get ball spirit
        :return spirit:
        """
        return self._ball

    @property
    def all_spirits(self):
        """
        get all sprites on screen
        :return pygame Group:
        """
        return self._all_spirits

    @property
    def paddle(self):
        """
        get paddle spirit
        :return spirit:
        """
        return self._paddle

    @property
    def life(self):
        """
        get number of life
        :return int:
        """
        return self._life

    @life.setter
    def life(self, life):
        """
        set life of player
        :param life:
        :return:
        """
        self._life = life

    @property
    def screen(self):
        """
        get screen
        :return pygame surface:
        """
        return self._screen

    @property
    def score(self):
        """
        get number of points
        :return int:
        """
        return self._score
