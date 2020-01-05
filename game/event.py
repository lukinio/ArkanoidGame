import pygame
from collections import defaultdict


class EventManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._listeners = defaultdict(list)
        return cls._instance

    def notify(self):
        for event in pygame.event.get():
            try:
                listeners = self._listeners[event.type]
            except KeyError:
                raise Exception("No listeners subscribe for this event")
            else:
                for listener in listeners:
                    listener(event)

    def subscribe(self, event_type, *listeners):
        self._listeners[event_type] += listeners

    def unsubscribe(self, *listeners):
        for _, evt_listeners in self._listeners.items():
            for l in evt_listeners:
                if l in listeners:
                    evt_listeners.remove(l)


eventManager = EventManager()