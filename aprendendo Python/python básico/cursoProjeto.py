try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre !')
