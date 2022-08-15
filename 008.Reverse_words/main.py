"""https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python"""


def reverse_words(text):
    return ' '.join(word[::-1] for word in text.strip().split(' '))


if __name__ == '__main__':
    test_string = "pine apple"
    print(f'<<<{reverse_words(test_string)}>>>')
