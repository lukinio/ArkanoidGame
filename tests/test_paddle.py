"""
Test module
"""
from unittest import TestCase
from unittest.mock import patch

import pygame

from game.spirites.paddle import Paddle


class TestPaddle(TestCase):
    """
    class which tests paddle
    """

    def setUp(self) -> None:
        with patch.object(Paddle, "__init__", lambda x, y, z: None):
            paddle_mock = Paddle(None, None)
            paddle_mock._rect = pygame.Rect(300, 550, 79, 20)
            paddle_mock._area = pygame.Rect(0, 0, 600, 600)
            paddle_mock.paddle_velocity = pygame.math.Vector2()
            self.paddle = paddle_mock

    def test_move_left(self):
        """
        moving left
        :return:
        """
        expected = 293
        self.paddle.paddle_velocity.x = -7
        self.paddle.update()
        self.assertEqual(self.paddle.rect.x, expected)

    def test_move_right(self):
        """
        moving right
        :return:
        """
        expected = 307
        self.paddle.paddle_velocity.x = 7
        self.paddle.update()
        self.assertEqual(self.paddle.rect.x, expected)
