"""
Brick
"""
from collections import defaultdict
from random import shuffle, randint
import pygame
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
        self._has_bonus = LUCKY_BRICK[randint(0, 2)]
        self._bonus = None

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
