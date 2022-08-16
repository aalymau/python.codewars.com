"""https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python"""


# def find_average(numbers):
#     if len(numbers) == 0:
#         return 0.0
#     else:
#         return sum(x for x in numbers) / len(numbers)

# Best practices
def find_average(array):
    return sum(array) / len(array) if array else 0


if __name__ == '__main__':
    print(f'<<<{find_average([1, 2, 3])} should be equal 2>>>')
