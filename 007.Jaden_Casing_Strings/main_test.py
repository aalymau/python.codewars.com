import unittest

from main import to_jaden_case


class MyTestCase(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual('How Can Mirrors Be Real If Our Eyes Aren"t Real',
                         to_jaden_case('How can mirrors be real if our eyes aren"t real'))
        self.assertEqual('Most Trees Are Blue',
                         to_jaden_case('most trees are blue'))
        self.assertEqual('All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own.',
                         to_jaden_case('All the rules in this world were made by someone no smarter than you. So make '
                                       'your own.'))
        self.assertEqual('School Is The Tool To Brainwash The Youth.',
                         to_jaden_case('School is the tool to brainwash the youth.'))
        self.assertEqual('When You Live Your Whole Life In A Prison Freedom Can Be So Dull.',
                         to_jaden_case('When you Live your Whole life In a Prison freedom Can be So dull.'))
        self.assertEqual('I Watch Twilight Every Night',
                         to_jaden_case('I watch Twilight every night'))
