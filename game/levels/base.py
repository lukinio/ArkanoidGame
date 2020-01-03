from abc import abstractmethod
from game.utils.constans import TOP_OFFSET


class BaseLevel(object):

    def __init__(self, top_offset=TOP_OFFSET):
        self.top_offset = top_offset

        self.name = 'set name to this level!'
        self._bricks = self.create_level()
        self.next_level = None

    @property
    def complete(self):
        return len(self._bricks) == 0

    @property
    def bricks(self):
        return self._bricks

    @abstractmethod
    def create_level(self):
        pass
