def header(phase):
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)

def aumentar(valor, aumento, formatado=False):
    resultado = valor * (1 + (aumento/100))
    if formatado:
        return real(resultado)
    return resultado


def diminuir(valor, reduz, formatado=False):
    resultado = valor * (1 - (reduz/100))
    if formatado:
        return real(resultado)
    return resultado


def dobro(valor, formatado=False):
    resultado = valor * 2
    if formatado:
        return real(resultado)
    return resultado


def metada(valor, formatado=False):
    resultado = valor * 0.5
    if formatado:
        return real(resultado)
    return resultado


def real(valor):
    return str(f'R$ {valor:.2f}')


def resumo(valor):
    header('Resumo das informações')
    print(f'{"Valor cadastrado:":<20} {real(valor):<10}')
    print(f'{"Dobro do preço:":<20} {dobro(valor, True):<10}')
    print(f'{"Metade do preço:":<20} {metada(valor, True):<10}')
    print(f'{"35% de aumento:":<20} {aumentar(valor, 35, True):<10}')
    print(f'{"25% de redução:":<20} {diminuir(valor, 25, True):<10}')
    print('-'*32)