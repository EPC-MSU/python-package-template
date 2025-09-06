from unittest import TestCase
from hello_world import say_hello, get_version


class TestHello(TestCase):
    def test_hello_say(self):
        self.assertTrue(say_hello() == "hello")

    def test_get_version(self):
        version = get_version()
        self.assertIsInstance(version, str)
        self.assertTrue(len(version) > 0)
        # Version should be in format like "0.0.1"
        parts = version.split(".")
        self.assertGreaterEqual(len(parts), 2)
