"""https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python"""


# def xo(s):
#     if s.lower().count('x') == s.lower().count('o'):
#         return True
#     return False


# Clever solution
def xo(s):
    return s.lower().count('x') == s.lower().count('o')


if __name__ == '__main__':
    print(xo('xO'), 'True expected')
    print(xo(''), 'True expected')
    print(xo('x'), 'False expected')
