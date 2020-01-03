import math
import random

from game.utils.constans import BALL_IMG, BALL_SPEED, PADDLE_SPEED
from game.utils.utility import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self._image, self._rect = load_img(BALL_IMG)
        self.rect.x, self.rect.y = x, y
        self._moving = False
        self.move_pos = [0, 0]

        self._area = pygame.display.get_surface().get_rect()
        self._bricks_sprites = pygame.sprite.Group()
        self._paddle_sprites = pygame.sprite.GroupSingle()
        self.angle = 70
        self.brick_collide = None

    def add_collide_sprites(self, sprite, paddle=False, on_collide=None):
        if paddle:
            self._paddle_sprites.add(sprite)
        else:
            self._bricks_sprites.add(sprite)
            self.brick_collide = on_collide

    def remove_collide_sprites(self, sprite, paddle=False):
        if paddle:
            self._paddle_sprites.remove(sprite)
        else:
            self._bricks_sprites.remove(sprite)

    def remove_all_collide_sprites(self):
        self._bricks_sprites.empty()

    @staticmethod
    def calc_new_pos(rect, angle):
        angle_rad = math.radians(angle)
        return rect.move(BALL_SPEED * math.cos(angle_rad), -BALL_SPEED * math.sin(angle_rad))

    def update(self):
        if self._moving:
            new_pos = self.calc_new_pos(self._rect, self.angle)
            if not self._area.contains(new_pos):
                if new_pos.y < self.image.get_height():
                    self.angle = -(180 - self.angle) % 360
                self.angle = (180 - self.angle) % 360
                new_pos = self.calc_new_pos(self._rect, self.angle)
            self._rect = new_pos

            if pygame.sprite.spritecollide(self, self._paddle_sprites, False):
                self.angle = random.randint(45, 135)
                self.rect.y = 540

            collide_bricks = pygame.sprite.spritecollide(self, self._bricks_sprites, False)
            if collide_bricks:
                self.angle = random.randint(-135, -45)
                for brick in collide_bricks:
                    self.brick_collide(brick)

        else:
            new_pos = self.rect.move(self.move_pos)
            if self._area.contains(new_pos):
                self._rect = new_pos

    def move_left(self):
        self.move_pos[0] = self.move_pos[0] - PADDLE_SPEED

    def move_right(self):
        self.move_pos[0] = self.move_pos[0] + PADDLE_SPEED

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    @property
    def moving(self):
        return self._moving

    @moving.setter
    def moving(self, moving):
        self._moving = moving
