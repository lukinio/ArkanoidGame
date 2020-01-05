import pygame
from game.utils.constans import BULLET_IMG, BULLET_SPEED
from game.utils.utility import load_img


class Bullet(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__()
        self._image, self._rect = load_img(BULLET_IMG)
        self._rect.x, self._rect.y = rect[0], rect[1]
        self._area = pygame.display.get_surface().get_rect()

    def update(self):
        self._rect = self._rect.move(0, BULLET_SPEED)
        if not self._area.contains(self._rect):
            self.kill()

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image
