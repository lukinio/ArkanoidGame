"""
Bullet - laser
"""
import pygame
from game.utils.constans import BULLET_IMG, BULLET_SPEED
from game.utils.utility import load_img


class Bullet(pygame.sprite.Sprite):
    """
    class represent laser bullets
    """

    def __init__(self, rect):
        """
        create bullet
        :param rect:
        """
        super().__init__()
        self.image, self.rect = load_img(BULLET_IMG)
        self.rect.x, self.rect.y = rect[0], rect[1]
        self._area = pygame.display.get_surface().get_rect()
        self._bricks_sprites = pygame.sprite.Group()
        self.brick_collide = None

    def add_collide_sprites(self, sprite, on_collide=None):
        """
        add collide sprites
        :param sprite:
        :param on_collide:
        :return:
        """
        self._bricks_sprites.add(sprite)
        self.brick_collide = on_collide

    def remove_collide_sprites(self, sprite):
        """
        remove collide sprites
        :param sprite:
        :return:
        """
        self._bricks_sprites.remove(sprite)

    def remove_all_collide_sprites(self):
        """
        remove all collide sprites
        :return:
        """
        self._bricks_sprites.empty()

    def update(self):
        """
        update position of bullet sprite
        :return:
        """
        self.rect = self.rect.move(0, BULLET_SPEED)

        collide_bricks = pygame.sprite.spritecollide(self, self._bricks_sprites, False)
        if collide_bricks:
            self.kill()
            for brick in collide_bricks:
                self.brick_collide(brick)

        if not self._area.contains(self.rect):
            self.kill()
