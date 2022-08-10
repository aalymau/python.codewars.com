import unittest

from main import maps


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual([2, 4, 6], maps([1, 2, 3]))
        self.assertEqual([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual([], maps([]))
