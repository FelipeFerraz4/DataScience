listNumber = []
biggest = smaller = 0
for i in range(0, 5):
    listNumber.append(float(input('Type a number: ')))
    if i == 0:
        biggest = listNumber[i]
        smaller = listNumber[i]
    if biggest < listNumber[i]:
        biggest = listNumber[i]
    if smaller > listNumber[i]:
        smaller = listNumber[i]
print(listNumber)
print(f'the biggest is {biggest} and the position: ', end='')
for i, number in enumerate(listNumber):
    if number == biggest:
        print(i, end=' ')
print(f'\nThe smaller is {smaller} and the position: ', end='')
for i, number in enumerate(listNumber):
    if number == smaller:
        print(i, end=' ')
