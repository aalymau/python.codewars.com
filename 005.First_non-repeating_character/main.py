"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python"""


def first_non_repeating_letter(string):
    for c in string:
        if string.lower().count(c.lower()) < 2:
            return c
    return ""


if __name__ == '__main__':
    print(first_non_repeating_letter('sTreSS'))
