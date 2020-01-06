import pygame
from game.spirites.bullet import Bullet
from game.utils.constans import WIDTH, PADDLE_IMG, PADDLE_SPEED, PADDLE_EXPAND_IMG, PADDLE_LASER_IMG
from game.utils.utility import load_img
from game.event import eventManager
from abc import abstractmethod


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self._image, self._rect = load_img(PADDLE_IMG)
        self._rect.x, self._rect.y = x, y

        self._area = pygame.display.get_surface().get_rect()
        self.move_pos = [0, 0]

        self._state = None

    def update(self):
        new_pos = self.rect.move(self.move_pos)
        if self._area.contains(new_pos):
            self._rect = new_pos
        pygame.event.pump()

    def move_left(self):
        self.move_pos[0] = self.move_pos[0] - PADDLE_SPEED

    def move_right(self):
        self.move_pos[0] = self.move_pos[0] + PADDLE_SPEED

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state


class PaddleState:
    def __init__(self, game):
        self._game = game

    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @property
    def game(self):
        return self._game


class NormalPaddle(PaddleState):

    def __init__(self, game):
        super().__init__(game)
        self.apply()

    def apply(self):
        pos = self.game.paddle.rect.center
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_IMG)
        self.game.paddle.rect.center = pos

    def turn_off(self):
        pass


class ExpandPaddle(PaddleState):

    def __init__(self, game):
        super().__init__(game)
        self.apply()

    def apply(self):
        pos = list(self.game.paddle.rect.center)
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_EXPAND_IMG)
        wd = self.game.paddle.image.get_width() / 2
        if pos[0] < wd:
            pos[0] = wd
        elif pos[0] > WIDTH - wd:
            pos[0] = WIDTH - wd
        self.game.paddle.rect.center = pos

    def turn_off(self):
        self.game.paddle.state = NormalPaddle(self.game)


class LaserPaddle(PaddleState):

    def __init__(self, game):
        super().__init__(game)
        self.apply()
        eventManager.subscribe(pygame.KEYDOWN, self.shoot)

    def apply(self):
        pos = self.game.paddle.rect.center
        self.game.paddle.image, self.game.paddle.rect = load_img(PADDLE_LASER_IMG)
        self.game.paddle.rect.center = pos

    def turn_off(self):
        eventManager.unsubscribe(pygame.KEYDOWN, self.shoot)
        self.game.paddle.state = NormalPaddle(self.game)

    def shoot(self, event):
        if event.key == pygame.K_SPACE:
            bullet = Bullet(self.game.paddle.rect.center)
            bullet.add_collide_sprites(self.game.level.bricks, on_collide=self.game.brick_collide)
            self.game.all_spirits.add(bullet)
