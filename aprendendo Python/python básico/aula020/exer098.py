from time import sleep
def header(phase):
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    passo = abs(passo)
    if fim > inicio:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(i, end=' -> ')
    else:
        for i in range(inicio, fim - 1, passo * -1):
            sleep(0.5)
            print(i, end=' -> ')
    print('END')


# Main program
header('Contador')
contador(1, 10, 1)
contador(10, 0, 2)
inicioU = int(input('digite o inicio da contagem: '))
fimU = int(input('Digite o fim da contagem: '))
passoU = int(input('Digite o tamanho do passo da contagem: '))
contador(inicioU, fimU, passoU)
