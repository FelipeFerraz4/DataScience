saque = int(input('Digite o valor do saque: '))
notas50 = saque // 50
saque = saque % 50
notas20 = saque // 20
saque = saque % 20
notas10 = saque // 10
saque = saque % 10
notas1 = saque // 1
if notas50 != 0:
    print(f'São {notas50} notas de 50')
if notas20 != 0:
    print(f'São {notas20} notas de 20')
if notas10 != 0:
    print(f'São {notas10} notas de 10')
if notas1 != 0:
    print(f'São {notas1} notas de 1')
