number = int(input('digite a quantidade de elementos da sequência de fibonacci: '))
if number == 0:
    print('Sem números')
elif number == 1:
    print('0', end=' -> ')
elif number == 2:
    print('0', end=' -> ')
    print('1', end=' -> ')
elif number < 0:
    print('Quantidade inválida')
else:
    print('0', end=' -> ')
    print('1', end=' -> ')
    num1 = 0
    num2 = 1
    number -= 2
    while number > 0:
        print('{}'.format(num1+num2), end=' -> ')
        number -= 1
        trade = num2
        num2 = num1 + num2
        num1 = trade
print('END')
