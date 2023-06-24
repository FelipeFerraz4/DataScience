numbers = [[], []]  # numbers[0] -> even, numbers[1] -> odd
for i in range(0, 7):
    num = float(input('Type a number: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
numbers[0].sort()
print(f'Even: {numbers[0]}')
numbers[1].sort()
print(f'Odd: {numbers[1]}')
print('END')
