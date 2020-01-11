"""
Ball
"""
import math
import random
import pygame
from game.utils.constans import BALL_IMG, BALL_SPEED
from game.utils.utility import load_img


class Ball(pygame.sprite.Sprite):
    """
    class represent ball
    """
    angle = 70

    def __init__(self, pos_x, pos_y):
        """
        :param pos_x:
        :param pos_y:
        """
        super().__init__()
        self._image, self._rect = load_img(BALL_IMG)
        self.rect.x, self.rect.y = pos_x, pos_y
        self._moving = False
        self.move_pos = [0, 0]

        self._area = pygame.display.get_surface().get_rect()
        self._bricks_sprites = pygame.sprite.Group()
        self._paddle_sprites = pygame.sprite.GroupSingle()
        self.brick_collide = None

    def add_paddle_spirit(self, paddle):
        """
        add collide spirit paddle
        :param paddle:
        :return:
        """
        self._paddle_sprites.add(paddle)

    def remove_paddle_spirit(self, paddle):
        """
        remove paddle spirit
        :param paddle:
        :return:
        """
        self._paddle_sprites.remove(paddle)

    def add_brick_sprites(self, bricks, on_collide=None):
        """
        add collide sprites bricks
        :param bricks:
        :param on_collide:
        :return:
        """
        self._bricks_sprites.add(bricks)
        self.brick_collide = on_collide

    def remove_brick_sprites(self, sprite):
        """
        remove brick spirit
        :param sprite:
        :return:
        """
        self._bricks_sprites.remove(sprite)

    def remove_all_collide_sprites(self):
        """
        remove all collide sprites
        :return:
        """
        self._paddle_sprites.empty()
        self._bricks_sprites.empty()

    @staticmethod
    def calc_new_pos(rect, angle):
        """
        calc new position for ball
        :param rect:
        :param angle:
        :return:
        """
        angle_rad = math.radians(angle)
        return rect.move(BALL_SPEED * math.cos(angle_rad), -BALL_SPEED * math.sin(angle_rad))

    def update(self):
        """
        update position of ball
        :return:
        """
        if self._moving:
            new_pos = self.calc_new_pos(self._rect, Ball.angle)
            if not self._area.contains(new_pos):
                if new_pos.y < self.image.get_height():
                    Ball.angle = -(180 - Ball.angle) % 360
                Ball.angle = (180 - Ball.angle) % 360
                new_pos = self.calc_new_pos(self._rect, Ball.angle)
            self._rect = new_pos

            paddle = pygame.sprite.spritecollide(self, self._paddle_sprites, False)
            if paddle:
                pad = paddle[0]
                self.rect.bottom = pad.rect.top
                Ball.angle = random.randint(45, 135)

            collide_bricks = pygame.sprite.spritecollide(self, self._bricks_sprites, False)
            if collide_bricks:
                Ball.angle = random.randint(-135, -45)
                for brick in collide_bricks:
                    self.brick_collide(brick)

        else:
            paddle = pygame.sprite.spritecollide(self, self._paddle_sprites, False)
            self._rect.x = paddle[0].rect.x + 45

    @property
    def rect(self):
        """
        get position of image
        :return rect:
        """
        return self._rect

    @property
    def image(self):
        """
        :return image:
        """
        return self._image

    @property
    def moving(self):
        """
        true if ball moving
        :return boolean:
        """
        return self._moving

    @moving.setter
    def moving(self, moving):
        """
        set if ball is moving
        :param moving:
        :return:
        """
        self._moving = moving
