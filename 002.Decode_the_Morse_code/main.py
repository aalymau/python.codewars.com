"""Dictionary representing the morse code chart"""
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                   'SOS': '...---...'}
MORSE_CODE = {y: x for x, y in MORSE_CODE_DICT.items()}

"""https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python"""


# def decode_morse(morse_code: str):
#     res = ''
#     for word in morse_code.strip(' ').split('   '):
#         for symbol in word.split(' '):
#             res += MORSE_CODE[symbol]
#         res += ' '
#     return res.strip()

# Clever solution
def decode_morse(morse_code):
    return ' '.join(
        ''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))


if __name__ == '__main__':
    print(decode_morse('.... . -.--   .--- ..- -.. .'))
