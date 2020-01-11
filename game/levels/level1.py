"""
Level 1
"""
import pygame
from game.levels.base import BaseLevel
from game.spirites.brick import Brick
from game.levels.level2 import Level2
from game.utils.constans import TOP_OFFSET, BRICK_WIDTH, BRICK_HEIGHT


class Level1(BaseLevel):
    """
    Level 1
    """

    def __init__(self, top_offset=TOP_OFFSET):
        """
        create level 1
        :param top_offset:
        """
        super().__init__(top_offset)
        self.name = 'Level 1'
        self.next_level = Level2

    def create_level(self):
        """
        create level
        :return bricks:
        """

        colors = ("cyan", "green", "orange", "white", "pink")
        bricks = pygame.sprite.Group()

        for i, color in enumerate(colors):
            for j in range(14):
                bricks.add(Brick(color, j * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))

        return bricks
