import unittest

from main import fake_bin


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual('01011110001100111', fake_bin('45385593107843568'))
        self.assertEqual('101000111101101', fake_bin('509321967506747'))
        self.assertEqual('011011110000101010000011011', fake_bin('366058562030849490134388085'))
        self.assertEqual('01111100', fake_bin('15889923'))
        self.assertEqual('100111001111', fake_bin('800857237867'))
