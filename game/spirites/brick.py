from game.utils.utility import *
from game.utils.constans import *
from collections import defaultdict

BrickHitNeed = defaultdict(lambda: 1)
BrickHitNeed.update({
    "gold": 2,
    "silver": 2,
})

BrickValue = {
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


class Brick(pygame.sprite.Sprite):

    def __init__(self, brick_color, x, y):
        super().__init__()
        self._color = brick_color
        self.image, self.rect = load_img(SRC+'brick_{}.png'.format(brick_color))
        self.rect.x, self.rect.y = x, y
        self._hit_counter = 0

    @property
    def color(self):
        return self._color

    def hit(self):
        self._hit_counter += 1
