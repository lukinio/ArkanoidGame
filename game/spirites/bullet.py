import pygame
from game.utils.constans import BULLET_IMG, BULLET_SPEED
from game.utils.utility import load_img


class Bullet(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__()
        self._image, self._rect = load_img(BULLET_IMG)
        self._rect.x, self._rect.y = rect[0], rect[1]
        self._area = pygame.display.get_surface().get_rect()
        self._bricks_sprites = pygame.sprite.Group()
        self.brick_collide = None

    def add_collide_sprites(self, sprite, on_collide=None):
        self._bricks_sprites.add(sprite)
        self.brick_collide = on_collide

    def remove_collide_sprites(self, sprite):
        self._bricks_sprites.remove(sprite)

    def remove_all_collide_sprites(self):
        self._bricks_sprites.empty()

    def update(self):
        self._rect = self._rect.move(0, BULLET_SPEED)

        collide_bricks = pygame.sprite.spritecollide(self, self._bricks_sprites, False)
        if collide_bricks:
            self.kill()
            for brick in collide_bricks:
                self.brick_collide(brick)

        if not self._area.contains(self._rect):
            self.kill()

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image
