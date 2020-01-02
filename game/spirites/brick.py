from game.utils.utility import *
from game.utils.constans import *


class Brick(pygame.sprite.Sprite):

    def __init__(self, brick_color, x, y):
        super().__init__()
        self.color = brick_color
        self.image, self.rect = load_img(SRC+'brick_{}.png'.format(brick_color))
        self.rect.x, self.rect.y = x, y
