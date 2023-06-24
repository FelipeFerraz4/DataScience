counter = 0
sumNumber = 0
cont = 'xxx'
while cont != 'N':
    number = int(input('Type a number: '))
    counter += 1
    sumNumber += number
    if counter == 1:
        smaller = number
        biggest = number
    if number < smaller:
        smaller = number
    if number > biggest:
        biggest = number
    cont = str(input('Gostaria de contiinuar, S/N: ')).strip().upper()
print('average = {}'.format(sumNumber/counter))
print('biggest = {}'.format(biggest))
print('smaller = {}'.format(smaller))
