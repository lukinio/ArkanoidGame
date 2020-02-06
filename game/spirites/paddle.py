"""
Paddle
"""
from abc import abstractmethod
import pygame
from game.spirites.bullet import Bullet
from game.utils.constans import WIDTH, PADDLE_IMG, PADDLE_SPEED, PADDLE_EXPAND_IMG, PADDLE_LASER_IMG
from game.utils.utility import load_img
from game.event import EVENT_MANAGER


class Paddle(pygame.sprite.Sprite):
    """
    class represent player
    """

    def __init__(self, pos_x, pos_y):
        """
        create player
        :param pos_x:
        :param pos_y:
        """
        super().__init__()
        self._image, self._rect = load_img(PADDLE_IMG)
        self._rect.x, self._rect.y = pos_x, pos_y

        self._area = pygame.display.get_surface().get_rect()
        self.paddle_velocity = pygame.math.Vector2()
        self.paddle_velocity[:] = 0, 0

        self._state = None

    def update(self):
        """
        update position of paddle sprite
        :return:
        """
        new_pos = self.rect.move(int(self.paddle_velocity.x), 0)
        if not self._area.contains(new_pos):
            if new_pos.x < 0:
                new_pos.x = 0
            elif new_pos.x > WIDTH - self._rect.width:
                new_pos.x = WIDTH - self._rect.width
        self._rect = new_pos

    def move_left(self):
        """
        move paddle to left
        :return:
        """
        self.paddle_velocity.x -= PADDLE_SPEED

    def move_right(self):
        """
        move paddle to right
        :return:
        """
        self.paddle_velocity.x += PADDLE_SPEED

    def stop_move(self):
        """
        stop moving paddle
        :return:
        """
        self.paddle_velocity.x = 0

    @property
    def rect(self):
        """
        get position of image
        :return rect:
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        set position of image
        :param rect:
        :return:
        """
        self._rect = rect

    @property
    def image(self):
        """
        :return image:
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        set image
        :param image:
        :return:
        """
        self._image = image

    @property
    def state(self):
        """
        :return state:
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        set state
        :param state:
        :return:
        """
        self._state = state


class PaddleState:
    """
    abstract class to represent paddle in different state
    """
    def __init__(self, game):
        """
        :param game:
        """
        self._game = game

    @abstractmethod
    def apply(self):
        """
        do some stuff depending on state
        :return:
        """

    @abstractmethod
    def turn_off(self):
        """
        back to normal state of paddle
        and turn off bonus
        :return:
        """

    @property
    def game(self):
        """
        :return game:
        """
        return self._game


class NormalPaddle(PaddleState):
    """
    class represent player in base state
    """

    def __init__(self, game):
        """
        :param game:
        """
        super().__init__(game)
        self.apply()

    def apply(self):
        pos = self.game.paddle.rect.center
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_IMG)
        self.game.paddle.rect.center = pos

    def turn_off(self):
        pass


class ExpandPaddle(PaddleState):
    """
    class represent bigger paddle
    """

    def __init__(self, game):
        """
        :param game:
        """
        super().__init__(game)
        self.apply()

    def apply(self):
        pos = list(self.game.paddle.rect.center)
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_EXPAND_IMG)
        width = self.game.paddle.image.get_width() / 2
        if pos[0] < width:
            pos[0] = width
        elif pos[0] > WIDTH - width:
            pos[0] = WIDTH - width
        self.game.paddle.rect.center = pos

    def turn_off(self):
        self.game.paddle.state = NormalPaddle(self.game)


class LaserPaddle(PaddleState):
    """
    class represent paddle which can shoot with bullets
    """

    def __init__(self, game):
        """
        :param game:
        """
        super().__init__(game)
        self.apply()
        EVENT_MANAGER.subscribe(pygame.KEYDOWN, self.shoot)

    def apply(self):
        pos = self.game.paddle.rect.center
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_LASER_IMG)
        self.game.paddle.rect.center = pos

    def turn_off(self):
        EVENT_MANAGER.unsubscribe(pygame.KEYDOWN, self.shoot)
        self.game.paddle.state = NormalPaddle(self.game)

    def shoot(self, event):
        """
        :param event:
        :return:
        """
        if event.key == pygame.K_SPACE:
            bullet = Bullet(self.game.paddle.rect.center)
            bullet.add_collide_sprites(self.game.level.bricks, on_collide=self.game.brick_collide)
            self.game.all_spirits.add(bullet)
