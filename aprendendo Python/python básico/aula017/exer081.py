confirmation = ''
listNumber = []
count = 0
while True:
    listNumber.append(int(input('type a number: ')))
    count += 1
    while True:
        confirmation = str(input('Would you like to continue, Y/N: ')).strip().upper()[0]
        if confirmation in 'YN':
            break
    if confirmation in 'N':
        break
print(f'typed {count} number')
listNumber.sort(reverse=True)
print(listNumber)
if 5 in listNumber:
    print('5 is on the list')
else:
    print('5 isn\'t on the list')
