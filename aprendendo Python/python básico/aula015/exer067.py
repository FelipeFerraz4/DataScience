number = 0
while number >= 0:
    number = int(input('Type a number: '))
    if number < 0:
        break
    print('-' * 20)
    print('--Tabuada--')
    for i in range(0, 11):
        print(f'{number} x {i:>2} = {number*i}')
    print('-' * 20)
