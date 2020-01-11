"""
Factory to create levels
"""
from abc import abstractmethod
from game.utils.constans import TOP_OFFSET


class BaseLevel:
    """
    Base class for factory
    """

    def __init__(self, top_offset=TOP_OFFSET):
        """
        create base for level
        :param top_offset:
        """
        self.top_offset = top_offset
        self.name = 'set name to this level!'
        self._bricks = self.create_level()
        self.next_level = None

    @property
    def complete(self):
        """
        check if level is complete
        :return boolean:
        """
        return len(self._bricks) == 0

    @property
    def bricks(self):
        """

        :return bricks:
        """
        return self._bricks

    @abstractmethod
    def create_level(self):
        """
        abstract method to create different levels
        :return :
        """
