"""https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python"""


# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.strip().split(' '))


# Clever solution
import string

to_jaden_case = string.capwords


if __name__ == '__main__':
    initial_string = "How can mirrors be real if our eyes aren't real"
    print(f'<<<{to_jaden_case(initial_string)}>>>')
