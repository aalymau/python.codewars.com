import unittest

from main import positive_sum


class MyTestCase(unittest.TestCase):
    def test_positive_sum(self):
        self.assertEqual(15, positive_sum([1, 2, 3, 4, 5]))
        self.assertEqual(13, positive_sum([1, -2, 3, 4, 5]))
        self.assertEqual(9, positive_sum([-1, 2, 3, 4, -5]))
        self.assertEqual(0, positive_sum([]))
        self.assertEqual(0, positive_sum([-1, -2, -3, -4, -5]))
