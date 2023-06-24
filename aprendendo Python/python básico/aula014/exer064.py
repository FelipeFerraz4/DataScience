number = 0
sumNumber = 0
counter = -1
while number != 999:
    counter += 1
    sumNumber += number
    number = int(input('digite um número: '))
print('Sum of {} number = {}'.format(counter, sumNumber))
