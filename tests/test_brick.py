"""
Test module
"""
from unittest import TestCase
from unittest.mock import patch

import pygame

from game.spirites.brick import Brick
from game.spirites.ball import Ball


class TestBrick(TestCase):
    """
    class which testing Brick
    """

    def setUp(self) -> None:
        with patch.object(Ball, "__init__", lambda x, y, z: None):
            ball_mock = Ball(None, None)
            ball_mock._rect = pygame.Rect(0, 0, 10, 10)
            ball_mock._moving = True
            ball_mock.angle = 70
            ball_mock.ball_velocity = pygame.math.Vector2()
            self.ball = ball_mock

        with patch.object(Brick, "__init__", lambda x, y, z, v: None):
            brick_mock = Brick(None, None, None)
            brick_mock.rect = pygame.Rect(100, 100, 43, 21)
            self.brick = brick_mock

    def test_collision_edge_bottom(self):
        """
        method tests reflection from bottom edge
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = 0, 1
        self.ball.topleft = 121, 121

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_right(self):
        """
        method tests reflection from right edge
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = 1, 0
        self.ball.rect.topleft = 143, 110

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_bottom_right_corner(self):
        """
        method tests reflection from bottom-right corner
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = -1, 1
        self.ball.rect.centerx, self.ball.rect.centery = 143, 121

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_top(self):
        """
        method tests reflection from top edge
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = 0, 1
        self.ball.bottomright = 115, 100

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_left(self):
        """
        method tests reflection from left edge
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = 1, 0
        self.ball.rect.bottomright = 100, 115

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_top_left_corner(self):
        """
        method tests reflection from top-left corner
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = -1, 1
        self.ball.rect.centerx, self.ball.rect.centery = 100, 100

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_bottom_left_corner(self):
        """
        method tests reflection from bottom-left corner
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = -1, 1
        self.ball.rect.centerx, self.ball.rect.centery = 100, 121

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)

    def test_collision_edge_top_right_corner(self):
        """
        method tests reflection from top-right corner
        :return:
        """
        expected = pygame.math.Vector2()
        expected[:] = -1, 1
        self.ball.rect.centerx, self.ball.rect.centery = 143, 100

        result = self.brick.collision_edge(self.ball)
        self.assertEqual(result, expected)
