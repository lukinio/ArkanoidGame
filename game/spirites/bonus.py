from game.spirites.paddle import ExpandPaddle
from game.utils.constans import *
from game.utils.utility import load_img
from abc import abstractmethod


class Bonus(pygame.sprite.Sprite):

    def __init__(self, brick, paddle):
        super().__init__()
        self._image = None
        self._rect = brick.rect
        self._paddle_sprites = pygame.sprite.GroupSingle()
        self._paddle_sprites.add(paddle)
        self._paddle = paddle
        self._area = pygame.display.get_surface().get_rect()

    def update(self):
        self._rect = self._rect.move(0, BONUS_SPEED)
        if pygame.sprite.spritecollide(self, self._paddle_sprites, False):
            self.use_bonus()
            self.kill()

        if not self._area.contains(self._rect):
            self.kill()

    @abstractmethod
    def use_bonus(self):
        pass

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    @property
    def paddle(self):
        return self._paddle


class ExpandBonus(Bonus):

    def __init__(self, brick, paddle):
        super().__init__(brick, paddle)
        self._image, _ = load_img(EXPAND_IMG)

    def use_bonus(self):
        self.paddle.state = ExpandPaddle(self.paddle)