def header(phase):
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)


# Main program
header('Hello world!')
header('Área do terreno')
header('Page')
header('O paralelepipedo é azul')
