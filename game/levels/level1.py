from game.levels.base import *
from game.spirites.brick import *


class Level1(BaseLevel):

    def __init__(self, top_offset):
        super().__init__(top_offset)
        self.name = 'Level 1'

    def create_level(self):

        colors = ("cyan", "green", "orange", "white", "pink")
        bricks = pygame.sprite.Group()

        for i, color in enumerate(colors):
            for j in range(14):
                bricks.add(Brick(color, j * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))

        return bricks
