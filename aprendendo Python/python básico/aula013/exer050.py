s = 0
for i in range(0, 6, 1):
    numbers = int(input('type a number integer: '))
    if numbers % 2 == 0:
        s += numbers
print('sum of the numbers even = {}'.format(s))
