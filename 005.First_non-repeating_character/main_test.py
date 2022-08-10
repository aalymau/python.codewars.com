import unittest

from main import first_non_repeating_letter


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual('a', first_non_repeating_letter('a'))
        self.assertEqual('t', first_non_repeating_letter('stress'))
        self.assertEqual('e', first_non_repeating_letter('moonmen'))
        self.assertEqual('', first_non_repeating_letter(''))
        self.assertEqual('', first_non_repeating_letter('abba'))
        self.assertEqual('', first_non_repeating_letter('aa'))
        self.assertEqual('#', first_non_repeating_letter('~><#~><'))
        self.assertEqual('w', first_non_repeating_letter('hello world, eh?'))
        self.assertEqual('T', first_non_repeating_letter('sTreSS'))
        self.assertEqual(',', first_non_repeating_letter('Go hang a salami, I"m a lasagna hog!'))
