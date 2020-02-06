"""
Test module
"""
from unittest import TestCase
from unittest.mock import patch

import pygame

from game.spirites.bonus import Bonus


class TestBonus(TestCase):
    """
    class which test bonuses
    """

    def setUp(self) -> None:
        with patch.object(Bonus, "__init__", lambda x, y, z: None):
            bonus_mock = Bonus(None, None)
            bonus_mock._rect = pygame.Rect(330, 540, 32, 16)
            bonus_mock._area = pygame.Rect(0, 0, 600, 600)
            bonus_mock._paddle_sprites = pygame.sprite.GroupSingle()
            self.bonus = bonus_mock

    def test_update(self):
        """
        test falling bonus
        :return:
        """
        expected = 542
        self.bonus.update()
        self.assertEqual(self.bonus.rect.y, expected)
