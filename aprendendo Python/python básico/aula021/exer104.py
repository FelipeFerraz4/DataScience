def leiaint(phase):
    while True:
        numtext = input(phase)
        if numtext.isnumeric():
            return numtext
        else:
            print('Erro, não é númerico')


# Main program
num = leiaint('digite um número: ')
print(f'O número digitado é {num}')
