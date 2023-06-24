from random import randint


def header(phase):
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)


def sorteio(number):
    for i in range(0, 5):
        number.append(randint(1, 100))


def somapar(listnumber):
    soma = 0
    for i in listnumber:
        if i % 2 == 0:
            soma += i
    return soma


# Main Program
header('Soma dos pares sorteados')
num = []
sorteio(num)
print(num)
somaP = somapar(num)
print(f'A soma dos números pares é {somaP}')
