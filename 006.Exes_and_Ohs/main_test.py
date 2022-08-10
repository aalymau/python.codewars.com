import unittest

from main import xo


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertTrue(xo('xo'))
        self.assertTrue(xo('xo0'))
        self.assertFalse(xo('xxxoo'))
        self.assertTrue(xo(''))
