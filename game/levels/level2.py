from game.levels.base import *
from game.spirites.brick import *
from game.utils.constans import TOP_OFFSET


class Level2(BaseLevel):

    def __init__(self, top_offset=TOP_OFFSET):
        super().__init__(top_offset)
        self.name = 'Level 2'

    def create_level(self):

        colors = ("gold", "silver")
        bricks = pygame.sprite.Group()

        for i, color in enumerate(colors):
            for j in range(14):
                bricks.add(Brick(color, j * BRICK_WIDTH, i * BRICK_HEIGHT + self.top_offset))

        return bricks
