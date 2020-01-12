"""
Level 2
"""
import pygame
from game.levels.base import BaseLevel
from game.spirites.brick import Brick
from game.utils.constans import TOP_OFFSET, BRICK_WIDTH, BRICK_HEIGHT


class Level2(BaseLevel):
    """
    Level 2
    """
    def __init__(self, top_offset=TOP_OFFSET):
        """
        create level 2
        :param top_offset:
        """
        super().__init__(top_offset)
        self.name = 'Level 2'

    def _slant_square(self, start_x, stop_x, top_off, colors):
        bricks = pygame.sprite.Group()
        size = stop_x - start_x

        for j in range(start_x, stop_x):
            bricks.add(Brick(colors[0], j * BRICK_WIDTH, (j+top_off) * BRICK_HEIGHT +
                             self.top_offset))

        for k in range(1, size+1):
            for i in range(start_x, stop_x - k):
                bricks.add(Brick(colors[k], (i + k) * BRICK_WIDTH, (i + top_off) * BRICK_HEIGHT +
                                 self.top_offset))
                bricks.add(Brick(colors[k], i * BRICK_WIDTH, (i + top_off + k) * BRICK_HEIGHT +
                                 self.top_offset))

        return bricks

    def create_level(self):
        """
        create level
        :return bricks:
        """

        colors = ("gold", "red", "silver", "cyan", "green")
        bricks = pygame.sprite.Group()

        for i, color in enumerate(colors):
            for j in range(1, 6):
                bricks.add(Brick(color, j * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))
                bricks.add(Brick(color, (j+7) * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))

        bricks.add(self._slant_square(1, 6, 8, colors))
        bricks.add(self._slant_square(8, 13, 1, colors))

        return bricks
