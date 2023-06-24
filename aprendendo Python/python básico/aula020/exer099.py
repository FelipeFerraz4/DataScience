def header(phase):
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)


def maior(* nums):
    biggest = 0
    for i, number in enumerate(nums):
        if i == 0 or number > biggest:
            biggest = number
    return biggest


# Main program
header('Maior')
big = maior(1, 2, 3, 4)
print(f'O maio foi {big}')
big = maior(1, 2, 3)
print(f'O maio foi {big}')
big = maior()
print(f'O maio foi {big}')
















# def maior(nums):
#     biggest = 0
#     for i, number in enumerate(nums):
#         if i == 0 or number > biggest:
#             biggest = number
#     return biggest
#
#
# # Main program
# header('Maior valor')
# num = []
# while True:
#     num.append(int(input('Digite um número: ')))
#     while True:
#         confirmation = str(input('Would you like to continue, Y/N: ')).strip().upper()[0]
#         if confirmation in 'YN':
#             break
#     if confirmation in 'N':
#         break
# m = maior(num)
# print(f'O maior é {m}')
