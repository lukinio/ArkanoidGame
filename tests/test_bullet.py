"""
Test module
"""
from unittest import TestCase
from unittest.mock import patch

import pygame

from game.spirites.bullet import Bullet


class TestBullet(TestCase):
    """
    class tests bullet
    """

    def setUp(self) -> None:
        with patch.object(Bullet, "__init__", lambda x, y: None):
            bullet_mock = Bullet(None)
            bullet_mock.rect = pygame.Rect(330, 200, 6, 25)
            bullet_mock._area = pygame.Rect(0, 0, 600, 600)
            bullet_mock._bricks_sprites = pygame.sprite.Group()
            self.bullet = bullet_mock

    def test_update(self):
        """
        test shooting bullet
        :return:
        """
        expected = 190
        self.bullet.update()
        self.assertEqual(self.bullet.rect.y, expected)
