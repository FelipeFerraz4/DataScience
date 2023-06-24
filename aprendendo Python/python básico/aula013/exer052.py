primo = int(input('type a number: '))
cont = 0
for i in range(primo, 0, -1):
    if primo % i == 0:
        cont += 1
if cont == 2:
    print('{}Esse número é primo{}'.format('\033[0:32m', '\033[m'))
else:
    print('{}Esse número não é primo{}'.format('\033[0:31m', '\033[m'))
