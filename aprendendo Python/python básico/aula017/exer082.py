listNumber = []
listEven = []
listOdd = []
confirmation = ''
while True:
    listNumber.append(int(input('Type a number: ')))
    while True:
        confirmation = str(input('Would you like to continue, Y/N: ')).strip().upper()[0]
        if confirmation in 'YN':
            break
    if confirmation == 'N':
        break
for number in listNumber:
    if number % 2 == 0:
        listEven.append(number)
    else:
        listOdd.append(number)
print(f'type list: {listNumber}')
print(f'Odd list: {listOdd}')
print(f'Even list: {listEven}')
print('END')
