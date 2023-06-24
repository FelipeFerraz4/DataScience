def fatorial(number=1, show=False):
    """
    -> Faz o calculo do fatorial de um número
    :param number: número o qual vai ter o seu fatorial
    :param show: variável (opicional) para mostrar o processo do calculo
    :return: o valor do fatorial
    """
    fat = 1
    for i in range(number, 0, -1):
        fat *= i
        if show:
            print(f'{i} ', end='')
            if i == 1:
                print('= ', end='')
            else:
                print('x ', end='')
    return fat


# Main program
print(fatorial(5, False))
help(fatorial)
