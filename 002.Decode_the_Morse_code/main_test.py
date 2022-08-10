import unittest

from main import decode_morse


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        print('Example from description\n')
        self.assertEqual('HEY JUDE', decode_morse('.... . -.--   .--- ..- -.. .'))
        print('Basic Morse decoding\n')
        self.assertEqual('A', decode_morse('.-'))
        self.assertEqual('E', decode_morse('.'))
        self.assertEqual('I', decode_morse('..'))
        self.assertEqual('EE', decode_morse('. .'))
        self.assertEqual('E E', decode_morse('.   .'))
        self.assertEqual('SOS', decode_morse('...---...'))
        self.assertEqual('SOS', decode_morse('... --- ...'))
        self.assertEqual('S O S', decode_morse('...   ---   ...'))
        print('Complex tests\n')
        self.assertEqual(decode_morse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   '
                                      '..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- '
                                      '--.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE '
                                                                           'LAZY DOG.')
