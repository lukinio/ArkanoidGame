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

    def create_level(self):
        """
        create level
        :return bricks:
        """

        colors = ("gold", "silver")
        bricks = pygame.sprite.Group()

        for i, color in enumerate(colors):
            for j in range(1, 13):
                bricks.add(Brick(color, j * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))

        return bricks
