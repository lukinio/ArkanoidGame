from game.utils.constans import *
from game.utils.utility import *


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self._image, self._rect = load_img(PADDLE_IMG)
        self._rect.x, self._rect.y = x, y

        self._area = pygame.display.get_surface().get_rect()
        self.move_pos = [0, 0]

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

    @property
    def image(self):
        return self._image
