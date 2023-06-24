number = counter = sumNumber = 0
while number != 999:
    number = float(input('Type a number, stop at 999: '))
    if number == 999:
        break
    counter += 1
    sumNumber += number
print(f'Numbers typed = {counter}')
print(f'Sum = {sumNumber}')
