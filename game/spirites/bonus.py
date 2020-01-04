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
        self._area = pygame.display.get_surface().get_rect()

    def update(self):
        self._rect = self._rect.move(0, BONUS_SPEED)
        collide_paddle = pygame.sprite.spritecollide(self, self._paddle_sprites, False)
        if collide_paddle:
            self.apply()
            self.kill()

        if not self._area.contains(self._rect):
            self.kill()

    @abstractmethod
    def apply(self):
        pass

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect


class ExpandBonus(Bonus):

    def __init__(self, brick, paddle):
        super().__init__(brick, paddle)
        self._image, _ = load_img(EXPAND_IMG)

    def apply(self):
        print("expand")
