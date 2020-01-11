"""
module docstring
"""
from collections import defaultdict
import pygame


class EventManager:
    """
    class supporting events in pygame
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._listeners = defaultdict(list)
        return cls._instance

    def notify(self):
        """
        support all event
        :return:
        """
        for event in pygame.event.get():
            for listener in self._listeners[event.type]:
                listener(event)

    def subscribe(self, event_type, *listeners):
        """
        start supporting some listeners
        :param event_type:
        :param listeners:
        :return None:
        """
        self._listeners[event_type] += listeners

    def unsubscribe(self, *listeners):
        """
        stop supporting some listeners
        :param listeners:
        :return None:
        """
        for _, evt_listeners in self._listeners.items():
            for listener in evt_listeners:
                if listener in listeners:
                    evt_listeners.remove(listener)


EVENT_MANAGER = EventManager()
