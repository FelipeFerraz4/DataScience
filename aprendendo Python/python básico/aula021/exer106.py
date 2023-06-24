def header(phase, cor):
    print(cor, end='')
    add = 10
    width = len(phase) + add
    print('-'*width)

    print(' ' * (add//2), end='')
    print(f'{phase}', end='')
    print(' ' * (add//2))

    print('-'*width)
    print('\033[m')


def pesquisa(nome):
    text = 'Acessando o manual do comando ' + nome
    header(text, '\033[0:44m')
    print('\033[7m')
    help(nome)
    print('\033[m')


# Main program
header('Ajuda o help do python', '\033[0:42m')
while True:
    search = str(input('Função ou bibloteca: ')).strip().lower()
    if search in 'fim':
        break
    pesquisa(search)
