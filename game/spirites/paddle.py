from game.utils.constans import *
from game.utils.utility import *
from abc import abstractmethod


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self._image, self._rect = load_img(PADDLE_IMG)
        self._rect.x, self._rect.y = x, y

        self._area = pygame.display.get_surface().get_rect()
        self.move_pos = [0, 0]

        self._state = NormalPaddle(self)

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
    def __init__(self, paddle):
        self.paddle = paddle

    @abstractmethod
    def apply(self):
        pass


class NormalPaddle(PaddleState):

    def __init__(self, paddle):
        super().__init__(paddle)

    def apply(self):
        pos = self.paddle.rect.center
        self.paddle.image, self.paddle.rect = load_img(PADDLE_IMG)
        self.paddle.rect.center = pos


class ExpandPaddle(PaddleState):

    def __init__(self, paddle):
        super().__init__(paddle)
        self.apply()

    def apply(self):
        pos = self.paddle.rect.center
        self.paddle.image, self.paddle.rect = load_img(PADDLE_EXPAND_IMG)
        self.paddle.rect.center = pos


class LaserPaddle(PaddleState):

    def __init__(self, paddle):
        super().__init__(paddle)
        self.apply()

    def apply(self):
        pos = self.paddle.rect.center
        self.paddle.image, self.paddle.rect = load_img(PADDLE_LASER_IMG)
        self.paddle.rect.center = pos

