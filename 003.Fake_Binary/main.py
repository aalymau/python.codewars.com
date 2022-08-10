# def fake_bin(x: str):
#     res = ''
#     for symbol in x:
#         if int(symbol) < 5:
#             res += '0'
#         else:
#             res += '1'
#     return res

# the best solution
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


if __name__ == '__main__':
    print(fake_bin('45385593107843568'))
