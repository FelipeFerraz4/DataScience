listRegister = []
while True:
    while True:
        register = int(input('type a register: '))
        if register not in listRegister:
            break
        else:
            print('Invalid, ', end='')
    listRegister.append(register)
    while True:
        confirmation = str(input('Gostaria de continuar, S/N: ')).strip().upper()
        if confirmation in 'NS':
            break
    if confirmation == 'N':
        break
listRegister.sort()
print(listRegister)
print('END')
