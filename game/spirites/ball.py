import math
import random

from game.utils.constans import *
from game.utils.utility import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.__image, self._rect = load_img(BALL_IMG)
        self.rect.x, self.rect.y = x, y
        self.__moving = False

        self._area = pygame.display.get_surface().get_rect()
        self._collide_sprites = pygame.sprite.Group()
        self.angle = 70

    def add_collide_sprites(self, sprite):
        self._collide_sprites.add(sprite)

    def remove_collide_sprites(self, sprite):
        self._collide_sprites.add(sprite)

    @staticmethod
    def calc_new_pos(rect, angle):
        angle_rad = math.radians(angle)
        return rect.move(BALL_SPEED * math.cos(angle_rad), BALL_SPEED * -math.sin(angle_rad))

    def update(self):
        new_pos = self.calc_new_pos(self._rect, self.angle)
        if not self._area.contains(new_pos):
            if new_pos.y < self.image.get_height():
                self.angle = -(180 - self.angle) % 360
            self.angle = (180 - self.angle) % 360
            new_pos = self.calc_new_pos(self._rect, self.angle)
        self._rect = new_pos

        if pygame.sprite.spritecollide(self, self._collide_sprites, False):
            self.angle = random.randint(45, 135)
            self.rect.y = 540

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self.__image

    @property
    def moving(self):
        return self.__moving

    @moving.setter
    def moving(self, moving):
        self.__moving = moving
