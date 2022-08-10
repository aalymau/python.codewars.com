import unittest
from random import randint

from main import array_diff


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
        self.assertEqual(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

    @staticmethod
    def array_sol(a, b):
        return [item for item in a if item not in b]

    def test_array_diff(self):
        for _ in range(40):
            a_len, b_len = randint(0, 20), randint(0, 20)
            a = [randint(0, 40) - 20 for i in range(a_len)]
            b = [randint(0, 40) - 20 for i in range(b_len)]
            exp = self.array_sol(a[:], b[:])
            print(f"Testing for array_diff({repr(a)}, {repr(b)})")
            self.assertEqual(array_diff(a[:], b[:]), exp, "Failed")
