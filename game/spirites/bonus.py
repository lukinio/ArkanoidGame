"""
Bonus
"""
from abc import abstractmethod
import pygame
from game.spirites.paddle import NormalPaddle, ExpandPaddle, LaserPaddle
from game.utils.constans import BONUS_SPEED, BONUS_LASER_IMG, BONUS_LIFE_IMG, BONUS_EXPAND_IMG
from game.utils.utility import load_img


class Bonus(pygame.sprite.Sprite):
    """
    abstract class represent bonuses falling from brick
    """

    def __init__(self, brick, game):
        """
        :param brick:
        :param game:
        """
        super().__init__()
        self._game = game
        self._image = None
        self._rect = brick.rect
        self._paddle_sprites = pygame.sprite.GroupSingle()
        self._paddle_sprites.add(self._game.paddle)
        self._area = pygame.display.get_surface().get_rect()

    def update(self):
        """
        update position of bonus sprite
        :return:
        """
        self._rect = self._rect.move(0, BONUS_SPEED)
        if pygame.sprite.spritecollide(self, self._paddle_sprites, False):
            self.use_bonus()
            self.kill()

        if not self._area.contains(self._rect):
            self.kill()

    @abstractmethod
    def use_bonus(self):
        """
        use bonus
        :return:
        """

    @property
    def image(self):
        """
        :return image:
        """
        return self._image

    @property
    def rect(self):
        """
        get position of image
        :return rect:
        """
        return self._rect

    @property
    def game(self):
        """
        :return game:
        """
        return self._game


class ExpandBonus(Bonus):
    """
    Bonus which make paddle bigger
    """

    def __init__(self, brick, game):
        """
        :param brick:
        :param game:
        """
        super().__init__(brick, game)
        self._image, _ = load_img(BONUS_EXPAND_IMG)

    def use_bonus(self):
        self.game.paddle.state.turn_off()
        self.game.paddle.state = ExpandPaddle(self.game)


class LifeBonus(Bonus):
    """
    bonus which give player additional life
    """

    def __init__(self, brick, game):
        """
        :param brick:
        :param game:
        """
        super().__init__(brick, game)
        self._image, _ = load_img(BONUS_LIFE_IMG)

    def use_bonus(self):
        self.game.life += 1
        self.game.check_life()
        self.game.paddle.state.turn_off()
        self.game.paddle.state = NormalPaddle(self.game)


class LaserBonus(Bonus):
    """
    bonus which make that player can shoot
    """

    def __init__(self, brick, game):
        super().__init__(brick, game)
        self._image, _ = load_img(BONUS_LASER_IMG)

    def use_bonus(self):
        self.game.paddle.state.turn_off()
        self.game.paddle.state = LaserPaddle(self.game)
