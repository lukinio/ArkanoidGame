"""
Brick
"""
from collections import defaultdict
from random import shuffle, randint
import pygame
from pygame.math import Vector2
from game.spirites.bonus import ExpandBonus, LifeBonus, LaserBonus
from game.utils.utility import load_img
from game.utils.constans import SRC, LUCKY_BRICK

BRICK_HIT_NEED = defaultdict(lambda: 1)
BRICK_HIT_NEED.update({
    "gold": 2,
    "silver": 2,
})

BRICK_VALUE = {
    "gold": 200,
    "silver": 100,
    "green": 90,
    "blue": 80,
    "yellow": 75,
    "cyan": 70,
    "red": 60,
    "orange": 50,
    "white": 25,
    "pink": 30
}

BONUSES = [ExpandBonus, LifeBonus, LaserBonus]


class Brick(pygame.sprite.Sprite):
    """
    class represent enemy to destroy
    """

    t_left, t_right, b_left, b_right = Vector2(), Vector2(), Vector2(), Vector2()
    ball_center = Vector2()

    horizontal, vertical, corner = Vector2(), Vector2(), Vector2()
    vertical[:] = 1, 0
    horizontal[:] = 0, 1
    corner[:] = -1, 1

    def __init__(self, brick_color, pos_x, pos_y):
        """
        Create Brick
        :param brick_color:
        :param pos_x:
        :param pos_y:
        """

        super().__init__()
        self._color = brick_color
        self.image, self.rect = load_img(SRC+'brick_{}.png'.format(brick_color))
        self.rect.x, self.rect.y = pos_x, pos_y
        self._hit_counter = 0
        shuffle(LUCKY_BRICK)
        self._has_bonus = LUCKY_BRICK[randint(0, len(LUCKY_BRICK)-1)]
        self._bonus = None

    def collision_edge(self, ball):
        """
        checks which edge has collided with ball and returns vector to reflect
        :param ball:
        :return Vector2:
        """
        Brick.t_left[:] = self.rect.left, self.rect.top
        Brick.t_right[:] = self.rect.right, self.rect.top
        Brick.b_left[:] = self.rect.left, self.rect.bottom
        Brick.b_right[:] = self.rect.right, self.rect.bottom
        Brick.ball_center[:] = ball.rect.centerx, ball.rect.centery

        vec1 = Brick.t_right - Brick.b_left
        vec2 = Brick.b_right - Brick.t_left

        ball_vec1 = Brick.ball_center - Brick.b_left
        ball_vec2 = Brick.ball_center - Brick.t_left

        check_point_vec1 = vec1.cross(ball_vec1)
        check_point_vec2 = vec2.cross(ball_vec2)

        if check_point_vec1 > 0:
            if check_point_vec2 > 0:
                return Brick.horizontal  # bounce from bottom side of brick
            if check_point_vec2 < 0:
                return Brick.vertical    # bounce from right side of brick
            return Brick.corner          # bounce from bottom-right-corner of brick

        if check_point_vec1 < 0:
            if check_point_vec2 > 0:
                return Brick.vertical    # bounce from left side of brick
            if check_point_vec2 < 0:
                return Brick.horizontal  # bounce from top side of brick
            return Brick.corner          # bounce from top-left-corner of brick

        return Brick.corner              # bounce from bottom-left/top-right-corner of brick

    @property
    def has_bonus(self):
        """
        check if brick has some bonus
        :return boolean:
        """
        return self._has_bonus

    @property
    def bonus(self):
        """
        if brick has a bonus
        :return Bonus:
        """
        if self.has_bonus:
            shuffle(BONUSES)
            self._bonus = BONUSES[randint(0, 2)]
        return self._bonus

    @property
    def color(self):
        """
        color of brick
        :return String:
        """
        return self._color

    @property
    def hit_counter(self):
        """
        how many times brick was hit
        :return int:
        """
        return self._hit_counter

    def hit(self):
        """
        increase hit_counter by 1
        :return None:
        """
        self._hit_counter += 1
