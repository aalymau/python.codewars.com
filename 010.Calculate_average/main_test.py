import unittest

from main import find_average


class MyTestCase(unittest.TestCase):
    def test_find_average(self):
        self.assertEqual(2, find_average([1, 2, 3]))
        self.assertEqual(0, find_average([]))
        self.assertEqual(-0.5, find_average([2, -3]))
