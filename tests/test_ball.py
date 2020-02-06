"""
Test module
"""
from unittest import TestCase
from unittest.mock import patch

import pygame

from game.spirites.ball import Ball


class TestBall(TestCase):
    """
    class which testing Ball
    """

    def setUp(self) -> None:
        with patch.object(Ball, "__init__", lambda x, y, z: None):
            ball_mock = Ball(None, None)
            ball_mock._rect = pygame.Rect(121, 121, 10, 10)
            ball_mock._moving = True
            ball_mock.angle = 70
            ball_mock.ball_velocity = pygame.math.Vector2()
            self.ball = ball_mock

    def test_calc_new_pos_direct_top_right(self):
        """
        method tests moves ball in top-right direction
        :return:
        """
        expected = [123, 115]
        self.ball.ball_velocity[:] = 1, -1
        result = self.ball.calc_new_pos(self.ball.rect, self.ball.angle)
        self.assertEqual([result.x, result.y], expected)

    def test_calc_new_pos_direct_top_left(self):
        """
        method tests moves ball in top-left direction
        :return:
        """
        expected = [119, 115]
        self.ball.ball_velocity[:] = -1, -1
        result = self.ball.calc_new_pos(self.ball.rect, self.ball.angle)
        self.assertEqual([result.x, result.y], expected)

    def test_calc_new_pos_direct_bottom_right(self):
        """
        method tests moves ball in bottom-right direction
        :return:
        """
        expected = [123, 127]
        self.ball.ball_velocity[:] = 1, 1
        result = self.ball.calc_new_pos(self.ball.rect, self.ball.angle)
        self.assertEqual([result.x, result.y], expected)

    def test_calc_new_pos_direct_bottom_left(self):
        """
        method tests moves ball in bottom-left direction
        :return:
        """
        expected = [119, 115]
        self.ball.ball_velocity[:] = -1, -1
        result = self.ball.calc_new_pos(self.ball.rect, self.ball.angle)
        self.assertEqual([result.x, result.y], expected)
