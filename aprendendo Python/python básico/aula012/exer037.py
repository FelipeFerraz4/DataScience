number = int(input('type a number integer: '))
base = int(input('1 - binario\n2 - octal\n3 - hexadecimal\nbase: '))
if base == 1:
    number = str(bin(number))[2:]
    print('binario é {}'.format(number))
elif base == 2:
    number = str(oct(number))[2:]
    print('octal é {}'.format(number))
elif base == 3:
    number = str(hex(number))[2:]
    print('hexadecimal é {}'.format(number))
else:
    print('base inválida')
