import unittest

from main import reverse_words


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual('ehT kciuq nworb xof spmuj revo eht yzal .god',
                         reverse_words('The quick brown fox jumps over the lazy dog.'))
        self.assertEqual('elppa',
                         reverse_words('apple'))
        self.assertEqual('a b c d',
                         reverse_words('a b c d'))
        self.assertEqual('elbuod  decaps  sdrow',
                         reverse_words('double  spaced  words'))
        self.assertEqual('desserts stressed',
                         reverse_words('stressed desserts'))
        self.assertEqual('olleh olleh',
                         reverse_words('hello hello'))
