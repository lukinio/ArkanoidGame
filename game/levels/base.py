from abc import abstractmethod


class BaseLevel(object):

    def __init__(self, top_offset):
        self.top_offset = top_offset

        self.name = 'set name to this level!'
        self.bricks = self.create_level()
        self._bricks_destroyed = 0

    @property
    def complete(self):
        return self._bricks_destroyed == len(self.bricks)

    def brick_destroyed(self):
        self._bricks_destroyed += 1

    @abstractmethod
    def create_level(self):
        pass
