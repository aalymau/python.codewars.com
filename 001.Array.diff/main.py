"""https://www.codewars.com/kata/523f5d21c841566fde000009/train/python"""


# def array_diff(a, b):
#     c = []
#     for i in range(len(a)):
#       if a[i] not in b:
#         c.append(a[i])
#     return c

# the best solution
def array_diff(a, b):
    return [x for x in a if x not in b]


if __name__ == '__main__':
    print(array_diff([1, 2], [3]))
