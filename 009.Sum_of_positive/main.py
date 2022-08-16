"""https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python"""


# def positive_sum(arr):
#     summ = 0
#     for num in arr:
#         if num > 0:
#             summ += num
#     return summ

# Best practices
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


if __name__ == '__main__':
    print(f'<<<{positive_sum([1,2,3,4,5])} should be equal 15>>>')
