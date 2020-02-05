"""
Test module
"""
from unittest import TestCase
from game.event import EVENT_MANAGER


class TestEventManager(TestCase):
    """
    class which testing eventManager
    """

    def test_subscribe_one_listener(self):
        """
        function testing subscribe method
        :return:
        """
        def listener():
            pass
        EVENT_MANAGER.subscribe('test_listener', listener)
        self.assertIn(listener, EVENT_MANAGER._listeners['test_listener'])

    def test_subscribe_many_listeners(self):
        """
        function testing subscribe method
        :return:
        """
        def listener():
            pass

        def listener1():
            pass

        def listener2():
            pass

        EVENT_MANAGER.subscribe('test_listeners', listener, listener1, listener2)

        self.assertIn(listener, EVENT_MANAGER._listeners['test_listeners'])
        self.assertIn(listener1, EVENT_MANAGER._listeners['test_listeners'])
        self.assertIn(listener2, EVENT_MANAGER._listeners['test_listeners'])

    def test_subscribe_any_listener(self):
        """
        function testing subscribe method
        :return:
        """
        with self.assertRaises(AssertionError):
            EVENT_MANAGER.subscribe('test_any_listener')

    def test_unsubscribe_one_listener(self):
        """
        function test unsubscribe method
        :return:
        """
        def listener():
            pass

        EVENT_MANAGER.subscribe('test_listener', listener)
        EVENT_MANAGER.unsubscribe(listener)
        self.assertNotIn(listener, EVENT_MANAGER._listeners['test_listener'])

    def test_unsubscribe_many_listeners(self):
        """
        function test unsubscribe method
        :return:
        """
        def listener():
            pass

        def listener1():
            pass

        def listener2():
            pass

        EVENT_MANAGER.subscribe('test_listeners', listener, listener1, listener2)
        EVENT_MANAGER.unsubscribe(listener, listener1, listener2)

        self.assertNotIn(listener, EVENT_MANAGER._listeners['test_listeners'])
        self.assertNotIn(listener1, EVENT_MANAGER._listeners['test_listeners'])
        self.assertNotIn(listener2, EVENT_MANAGER._listeners['test_listeners'])

    def test_unsubscribe_any_listener(self):
        """
        function test unsubscribe method
        :return:
        """
        with self.assertRaises(AssertionError):
            EVENT_MANAGER.unsubscribe()
