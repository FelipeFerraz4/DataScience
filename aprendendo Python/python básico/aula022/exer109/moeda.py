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
